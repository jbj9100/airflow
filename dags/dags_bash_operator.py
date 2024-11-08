from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",                    # dag의 이름, 파이썬 이름과는 상관없다.하지만 dag이름과 파이썬 이름 일치시키는게 좋다.
    schedule="0 0 * * *",                           # 크론 스케줄로 dag이 도는 시간 - 분,시,일,월,요        
    start_date=pendulum.datetime(2024, 11, 8, tz="Asia/Seoul"),  # dag의 시작 시간
    catchup=False,                                 # 만약 start date가 1월1일이고부터 현재 11/08일까지 누락된 기간을 동시에 다 돌린다, false면 11/08일 오늘부터 돌린다.
    # dagrun_timeout=datetime.timedelta(minutes=60), # dag이 60분 이상돌련 실패로 처리
    # tags=["example", "example2"],               # dag를 그룹화하고 필터링하는 옵션
    # params={"example_key": "example_value"},    # task 들한테 공통적으로 넘겨줄 파라미터들
) as dag:
    bash_t1 = BashOperator(                      # 오퍼레이터를 통해서만든 객체이름 : bash_t1, task이름과는 관계없음
        task_id="bash_t1",                       # graph에서 보이는 task이름 부분으로 객체이름과 동일하게 만들면 찾기 쉬움
        bash_command="echo whoami",             # 어떤 쉘스크립트를 실행할지
    )

    bash_t2 = BashOperator(                      
        task_id="bash_t2",                       
        bash_command="echo $HOSTNAME",  
    )
    bash_t1 >> bash_t2                          # task들의 수행 관계로 t1다음 t2가 돌겠다.