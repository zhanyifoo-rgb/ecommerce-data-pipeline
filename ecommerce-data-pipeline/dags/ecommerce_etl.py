from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts.extract import extract
from scripts.load import load
from scripts.load_dimensions import load_dimensions

with DAG(
    dag_id="ecommerce_etl",
    start_date=datetime(2026, 7, 14),
    schedule=None,
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    load_dimensions_task = PythonOperator(
        task_id="load_dimensions",
        python_callable=load_dimensions,
    )

extract_task >> load_task >> load_dimensions_task