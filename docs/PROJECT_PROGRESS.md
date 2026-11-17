# Employee Attrition Analytics & Prediction Pipeline

## Completed Phases

### 1. Data Ingestion
- Loaded employee CSV using Pandas.
- Inspected dataset structure and dimensions.

### 2. Data Profiling
- Analyzed missing values and duplicates.
- Inspected data types and unique values.
- Implemented business rule checks.

### 3. Data Cleaning
- Removed duplicate records.
- Identified constant columns.
- Removed EmployeeCount, Over18 and StandardHours.
- Preserved original raw dataset.
- Generated cleaned CSV.

## Cleaning Results

| Metric | Before | After |
|---|---:|---:|
| Records | 1470 | 1470 |
| Columns | 35 | 32 |
| Missing values | 0 | 0 |
| Duplicate rows | 0 | 0 |
### Phase 4: Data Transformation - Completed
- Standardized categorical columns.
- Created TenureGroup.
- Created ExperienceGroup.
- Generated transformed employee dataset.
- Preserved all 1470 employee records.

### Phase 5: Data Validation - Completed
- Validated required columns.
- Checked record counts.
- Checked missing values.
- Checked duplicate records and employee IDs.
- Validated age, income and experience.
- Validated Attrition values.
- Validated engineered features.
- All 12 validation checks passed.

### Next Phase: MySQL Integration
- Design database schema.
- Create employee database and tables.
- Connect Python with MySQL.
- Load validated employee records.
- Verify inserted records.

