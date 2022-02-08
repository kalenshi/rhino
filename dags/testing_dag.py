from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator

default_args = {

}

with DAG(
        dag_id="testing_dag",
        start_date=datetime(2022, 1, 24),
        schedule_interval=None,
        catchup=False
) as dag:
    test_task = DummyOperator(
        task_id="test_task"
    )
