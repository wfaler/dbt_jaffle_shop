
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 4, 8),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("dbt_dag", default_args=default_args, schedule_interval="@daily")

dbt_run = BashOperator(
    task_id="dbt_run",
    bash_command="cd /opt/airflow/dags/dbt && /home/airflow/.local/bin/dbt run", 
    dag=dag,
)
