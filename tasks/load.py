from sqlalchemy import text

from tasks.db import engine
from tasks.create_tables import create_raw_table


def load_raw_data(df):
    """
    Load the validated DataFrame into PostgreSQL.
    """

    # Ensure the table exists
    create_raw_table()
    
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE raw_eco_driving;"))

    # Load DataFrame into PostgreSQL
    df.to_sql(
        name="raw_eco_driving",
        con=engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=1000,
    )

    print(f"Successfully loaded {len(df)} rows into raw_eco_driving.")