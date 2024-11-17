from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task

with DAG(
    dag_id="dags_task_test",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2024, 11, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    @task(task_id="task11")
    def task1():
        return "Step 1"

    @task(task_id="task22")
    def task2():
        return "Step 2"

    @task(task_id="task33")
    def task3():
        return "Step 3"
    t1 = task1()
    t2 = task2()
    t3 = task3()

    t1 >> [t2, t3]