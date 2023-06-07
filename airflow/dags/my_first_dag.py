from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from lib.google_data_fetcher import fetch_data_from_twitter

with DAG(
       'my_first_dag',
       default_args={
           'depends_on_past': False,
           'email': ['airflow@example.com'],
           'email_on_failure': False,
           'email_on_retry': False,
           'retries': 1,
           'retry_delay': timedelta(seconds=15),
       },
       description='A first DAG.py',
       schedule=None,
       start_date=datetime(2021, 1, 1),
       catchup=False,
       tags=['example'],
) as dag:
   dag.doc_md = """
       This is my first DAG.py in airflow.
       I can write documentation in Markdown here with **bold text** or __bold text__.
   """

   task = PythonOperator(
       task_id='fetch_data_from_twitter',
       python_callable=fetch_data_from_twitter,
       op_kwargs={'task_number': 'task1'}
   )






