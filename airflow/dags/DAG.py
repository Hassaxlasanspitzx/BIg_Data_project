
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from lib.google_data_fetcher import fetch_data_from_twitter

with DAG(
       'DAG',
       default_args={
           'depends_on_past': False,
           'email': ['airflow@example.com'],
           'email_on_failure': False,
           'email_on_retry': False,
           'retries': 1,
           'retry_delay': timedelta(minutes=5),
       },
       description='A first DAG',
       schedule=None,
       start_date=datetime(2021, 1, 1),
       catchup=False,
       tags=['example'],
) as dag:
   dag.doc_md = """
       This is my first DAG in airflow.
       I can write documentation in Markdown here with *bold text* or _bold text_.
   """


   def extraction1():
       print("Hello Airflow - This is Task 1")

   def extraction2():
       print("Hello Airflow - This is Task 2")

   def formatting1():
       print("Hello Airflow - This is Task ")

   def formatting2():
       print("Hello Airflow - This is Task ")

   def combination():
       print("Hello Airflow - This is Task 4")
   def indexing():
       print("Hello Airflow - This is Task 5")

   t1 = PythonOperator(
       task_id='extraction1',
       python_callable=extraction1,
   )

   t2 = PythonOperator(
       task_id='extraction2',
       python_callable=extraction2
   )

   t3 = PythonOperator(
       task_id='formatting1',
       python_callable=formatting1
   )

   t4 = PythonOperator(
       task_id='formatting2',
       python_callable=formatting2
   )

   t5 = PythonOperator(
       task_id='combination',
       python_callable=combination
   )

   t6 = PythonOperator(
       task_id='indexing',
       python_callable=indexing
   )

t1 >> t3 >> t5 >> t6
t2 >> t4 >> t5 >> t6