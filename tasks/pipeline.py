from tasks.extract import extract_csv
from tasks.validate import validate_data
from tasks.load import load_raw_data
from tasks.execute_sql import execute_sql_file


def run_etl():
    """
    Complete ETL Pipeline
    """

    print("========== DriveSense ETL Started ==========")

    # Extract
    df = extract_csv()

    # Validate
    df = validate_data(df)

    # Load
    load_raw_data(df)

    print("========== ETL Completed Successfully ==========")