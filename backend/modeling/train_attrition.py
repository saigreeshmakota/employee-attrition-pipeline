"""Train baseline models for IBM HR employee attrition.

Run from the repository root:
    python -m backend.modeling.train_attrition
The script expects data/processed/transformed_employee_attrition.csv.
"""
from pathlib import Path
import json

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = ROOT / "data" / "processed" / "transformed_employee_attrition.csv"
OUTPUT_DIR = ROOT / "reports" / "models"

TARGET = "Attrition"
DROP_COLUMNS = ["EmployeeNumber", "Attrition"]


def build_preprocessor(frame: pd.DataFrame) -> ColumnTransformer:
    categorical = frame.select_dtypes(include=["object", "category", "string"]).columns.tolist()
    numeric = frame.select_dtypes(include=["number", "bool"]).columns.tolist()
    return ColumnTransformer(
        transformers=[
            ("numeric", Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scale", StandardScaler()),
            ]), numeric),
            ("categorical", Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ]), categorical),
        ],
        remainder="drop",
    )


def main() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}. Run the ingestion, cleaning and "
            "transformation steps first. The raw dataset is not committed to Git."
        )

    df = pd.read_csv(DATA_FILE)
    if TARGET not in df.columns:
        raise ValueError(f"Required target column '{TARGET}' is missing.")
    if df[TARGET].nunique() != 2:
        raise ValueError("Attrition target must contain both Yes and No classes.")

    y = df[TARGET].map({"No": 0, "Yes": 1})
    if y.isna().any():
        raise ValueError("Attrition contains values other than Yes/No.")

    X = df.drop(columns=[column for column in DROP_COLUMNS if column in df.columns])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    models = {
        "logistic_regression": LogisticRegression(
            max_iter=2000, class_weight="balanced", random_state=42
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=300, class_weight="balanced", random_state=42,
            min_samples_leaf=2,
        ),
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = {}
    for name, estimator in models.items():
        pipeline = Pipeline([
            ("preprocess", build_preprocessor(X_train)),
            ("model", estimator),
        ])
        pipeline.fit(X_train, y_train)
        predictions = pipeline.predict(X_test)
        probabilities = pipeline.predict_proba(X_test)[:, 1]
        results[name] = {
            "positive_class": "Yes",
            "precision_yes": precision_score(y_test, predictions, zero_division=0),
            "recall_yes": recall_score(y_test, predictions, zero_division=0),
            "f1_yes": f1_score(y_test, predictions, zero_division=0),
            "roc_auc": roc_auc_score(y_test, probabilities),
            "confusion_matrix_labels": ["No", "Yes"],
            "confusion_matrix": confusion_matrix(y_test, predictions).tolist(),
            "classification_report": classification_report(
                y_test, predictions, target_names=["No", "Yes"],
                output_dict=True, zero_division=0,
            ),
        }
        print(f"\n{name}")
        print(f"Precision (Attrition=Yes): {results[name]['precision_yes']:.3f}")
        print(f"Recall (Attrition=Yes):    {results[name]['recall_yes']:.3f}")
        print(f"F1 (Attrition=Yes):        {results[name]['f1_yes']:.3f}")
        print(f"ROC AUC:                   {results[name]['roc_auc']:.3f}")

    output_file = OUTPUT_DIR / "baseline_metrics.json"
    output_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nMetrics saved to {output_file}")


if __name__ == "__main__":
    main()
