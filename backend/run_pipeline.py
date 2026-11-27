"""Run the complete employee attrition workflow from the repository root.

Expected input:
  data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv

The raw dataset is intentionally not committed. Obtain it from the IBM HR
Analytics Employee Attrition & Performance dataset and use the expected name.
"""
import subprocess
import sys


STEPS = [
    ("Profile raw data", [sys.executable, "-m", "backend.ingestion.load_data"]),
    ("Clean data", [sys.executable, "-m", "backend.transformation.clean_data"]),
    ("Transform data", [sys.executable, "-m", "backend.transformation.transform_data"]),
    ("Validate transformed data", [sys.executable, "-m", "backend.validation.validate_data"]),
    ("Load into MySQL", [sys.executable, "-m", "backend.ingestion.load_to_mysql"]),
    ("Train attrition baselines", [sys.executable, "-m", "backend.modeling.train_attrition"]),
]


def main() -> None:
    for label, command in STEPS:
        print(f"\n{'=' * 12} {label} {'=' * 12}", flush=True)
        subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
