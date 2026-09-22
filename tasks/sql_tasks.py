from tasks.execute_sql import execute_sql_file


def create_staging():
    execute_sql_file("/opt/airflow/sql/02_create_staging_table.sql")


def create_analytics():
    execute_sql_file("/opt/airflow/sql/03_create_analytics_tables.sql")