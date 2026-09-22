import sys

sys.path.append("/opt/airflow")

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from tasks.pipeline import run_etl
from tasks.sql_tasks import create_staging, create_analytics

default_args = {
    "owner": "Pragya",
    "retries": 1,
}

with DAG(
    dag_id="drivesense_etl",
    description="DriveSense Analytics ETL Pipeline",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["ETL", "DriveSense"],
) as dag:

    etl_task = PythonOperator(
        task_id="run_python_etl",
        python_callable=run_etl,
    )

    staging_task = PythonOperator(
        task_id="create_staging_table",
        python_callable=create_staging,
    )

    analytics_task = PythonOperator(
        task_id="create_analytics_tables",
        python_callable=create_analytics,
    )

    etl_task >> staging_task >> analytics_task