from scipy.io import arff
import pandas as pd
from pathlib import Path

RAW_FILE = Path("data/raw/student.arff")
PROCESSED_DIR = Path("data/processed")
OUTPUT_FILE = PROCESSED_DIR / "cleaned_student_data.csv"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

data, metadata = arff.loadarff(RAW_FILE)

df = pd.DataFrame(data)

print("Original shape:", df.shape)


# --------------------------------------------------
# 4. Convert byte/string values to normal strings
# --------------------------------------------------

for column in df.columns:
    if df[column].dtype == "object":
        df[column] = df[column].apply(
            lambda x: x.decode("utf-8")
            if isinstance(x, bytes)
            else x
        )


# --------------------------------------------------
# 5. Display missing values before cleaning
# --------------------------------------------------

print("\nMissing values before cleaning:")
print(df.isnull().sum())


# --------------------------------------------------
# 6. Remove duplicate rows
# --------------------------------------------------

duplicates = df.duplicated().sum()

print("\nDuplicate rows:", duplicates)

if duplicates > 0:
    df = df.drop_duplicates()


# --------------------------------------------------
# 7. Remove completely empty rows
# --------------------------------------------------

empty_rows = df.isnull().all(axis=1).sum()

print("Completely empty rows:", empty_rows)

if empty_rows > 0:
    df = df.dropna(how="all")


# --------------------------------------------------
# 8. Remove rows missing the target variable
# --------------------------------------------------

target = "Performance"

missing_target = df[target].isnull().sum()

print("Rows missing Performance:", missing_target)

if missing_target > 0:
    df = df.dropna(subset=[target])


# --------------------------------------------------
# 9. Check final missing values
# --------------------------------------------------

print("\nMissing values after cleaning:")
print(df.isnull().sum())


# --------------------------------------------------
# 10. Save cleaned dataset
# --------------------------------------------------

df.to_csv(OUTPUT_FILE, index=False)

print("\nCleaned shape:", df.shape)
print(f"\nCleaned dataset saved to: {OUTPUT_FILE}")