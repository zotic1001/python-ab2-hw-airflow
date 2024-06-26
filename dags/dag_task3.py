from airflow.decorators import dag, task
from airflow import DAG
from airflow.operators.email import EmailOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta, datetime


# Функция, которую мы хотим выполнить
def my_python_function():
    print('Python operator')


@dag(start_date=datetime(2022, 11, 1),
     schedule="@daily",
     catchup=False)
def etl3():
    send_email = EmailOperator(
        task_id='send_email',
        to='email@example.com',
        subject='Airflow',
        html_content="""<h3>Email Operator Test</h3>""",
    )

    run_bash_task = BashOperator(
        task_id='run_bash',
        bash_command='echo "Bash output"'
    )

    run_python_task = PythonOperator(
        task_id='run_python',
        python_callable=my_python_function
    )

    run_bash_task >> send_email >> run_python_task


dag3 = etl3()
