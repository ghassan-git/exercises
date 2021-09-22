from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def hello_world():
    print("Hello world")


myDAG = DAG('myFirstBag', description='Airflow example DAG', start_date=datetime(2021, 9, 10),
            schedule_interval='@daily')
task = PythonOperator(task_id='hello_world', python_callable=hello_world, dag=myDAG)
