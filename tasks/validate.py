import pandas as pd


def validate_data(df: pd.DataFrame):
    """
    Validate the extracted DataFrame before loading.
    """

    print("Starting data validation...")

    # ----------------------------
    # Check if DataFrame is empty
    # ----------------------------
    if df.empty:
        raise ValueError("CSV file is empty.")

    # ----------------------------
    # Expected Columns
    # ----------------------------
    expected_columns = [
        "rpm_variation",
        "harsh_braking_count",
        "idling_time",
        "fuel_consumption",
        "acceleration_smoothness",
        "eco_score",
    ]

    if list(df.columns) != expected_columns:
        raise ValueError(
            f"Column mismatch.\nExpected: {expected_columns}\nFound: {list(df.columns)}"
        )

    # ----------------------------
    # Duplicate Columns
    # ----------------------------
    if df.columns.duplicated().any():
        raise ValueError("Duplicate column names found.")

    # ----------------------------
    # Missing Values
    # ----------------------------
    print("\nMissing Values:")
    print(df.isnull().sum())

    # ----------------------------
    # Data Types
    # ----------------------------
    print("\nData Types:")
    print(df.dtypes)

    # ----------------------------
    # Duplicate Rows
    # ----------------------------
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate Rows: {duplicates}")

    print("\nData validation completed successfully.")

    return df