import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id = "pyspark_dag",
    default_args={
        "owner": "Zidan Ali Zaqi",
        "start_date": airflow.utils.dates.days_ago(0)
    },
    schedule_interval = "0 0 * * *"
)

start = PythonOperator(
    task_id = 'start',
    python_callable = lambda: print("Jobs Started"),
    dag=dag
)


wordcount = SparkSubmitOperator(
    task_id = 'wordcount',
    conn_id = "spark-conn",
    application = "jobs/python/wordcount.py",
    files="jobs/python/book.txt",
    dag=dag
)

end = PythonOperator(
    task_id = 'end',
    python_callable = lambda: print("Jobs completed"),
    dag=dag
)

start >> [wordcount] >> end