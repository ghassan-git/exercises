from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import random
import string

# def hello_world():
#     print("Hello world")
#
#
# myDAG = DAG('myFirstBag', description='Airflow example DAG', start_date=datetime(2021, 9, 10),
#             schedule_interval='@daily')
# task = PythonOperator(task_id='hello_world', python_callable=hello_world, dag=myDAG)

SIZE = 10


def return_10_integers():
    return list(range(0, SIZE))


def return_10_strings():
    result = []
    for i in range(0, SIZE):
        result.append(''.join(
            random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in
            range(5)))
    return result


def combine_strings_and_integers(strings: list, integers: list) -> list:
    result = []
    for index in range(SIZE):
        result.append((strings[index], integers[index]))
    return result


myDAG = DAG('myFirstBag', description='Airflow example DAG', start_date=datetime(2021, 9, 30),
            schedule_interval='@hourly')
# print(combine_strings_and_integers(return_10_strings(), return_10_integers()))
int_task = PythonOperator(task_id='generate_integers', python_callable=return_10_integers, dag=myDAG)
string_task = PythonOperator(task_id='generate_strings', python_callable=return_10_strings, dag=myDAG)
combine_task = PythonOperator(task_id='combine_everything', python_callable=combine_strings_and_integers, dag=myDAG)

[int_task, string_task] >> combine_task