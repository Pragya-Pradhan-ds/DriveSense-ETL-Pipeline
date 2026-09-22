import pandas as pd
from pathlib import Path


def extract_csv():
    """
    Read the source CSV file and return a DataFrame.
    """

    csv_path = Path("/opt/airflow/data/eco_driving_score.csv")

    df = pd.read_csv(csv_path)

    print(f"Successfully extracted {len(df)} rows.")

    return df