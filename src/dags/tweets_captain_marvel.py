from core.execute_tweets import core_get_data, core_db_insert_to_db
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

SCHEDULE_INTERVAL = '@hourly'

default_args = {
    'owner': 'SkYe',
    'start_date': datetime(2019, 4, 20),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries':3,
    'retry_delay': timedelta(minutes=1)
}

DAG_VERSION = 'TweetsCaptainMarvel.0'

dag = DAG(DAG_VERSION,
          default_args=default_args,
          schedule_interval=SCHEDULE_INTERVAL,
          concurrency=1,
          max_active_runs=1)

get_data = PythonOperator(
    task_id = 'get_data',
    python_callable=core_get_data,
    retries=0,
    provide_context=True,
    dag=dag
)

db_insert_to_db = PythonOperator(
    task_id='db_insert_to_db',
    python_callable=core_db_insert_to_db,
    retries=0,
    provide_context=True,
    dag=dag
)

get_data >> db_insert_to_db