from pathlib import Path
from sqlalchemy import text

from tasks.db import engine


def create_raw_table():

    sql_path = Path("/opt/airflow/sql/01_create_raw_table.sql")

    with open(sql_path, "r") as file:
        sql = file.read()

    with engine.begin() as connection:
        connection.execute(text(sql))

    print("✅ raw_eco_driving table created successfully.")