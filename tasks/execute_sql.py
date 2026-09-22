from pathlib import Path
from sqlalchemy import text

from tasks.db import engine


def execute_sql_file(file_path):
    """Execute a SQL script using SQLAlchemy."""

    sql = Path(file_path).read_text(encoding="utf-8")

    with engine.begin() as conn:
        conn.execute(text(sql))

    print(f"Executed: {file_path}")