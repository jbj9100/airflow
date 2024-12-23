from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from airflow.decorators import task
from common.common_func import regist

with DAG(
    dag_id="dags_python_with_op_args_copy",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:

    @task(task_id="regist_t1")
    def task_regist():
        return regist('hjkim','man','kr','seoul')
    regist_t1 = task_regist()
