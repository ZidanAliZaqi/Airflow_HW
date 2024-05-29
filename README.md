# Airflow_HW
Tugas: Menjalankan Pekerjaan PySpark Menggunakan SparkSubmitOperator di Airflow
Tujuan: Membuat DAG di Airflow untuk menjalankan pekerjaan PySpark menggunakan 
SparkSubmitOperator.
Instruksi:
1. Persiapkan Airflow: Pastikan Airflow telah terinstal dan dikonfigurasi dengan benar di lingkungan 
Anda.
2. Buat Skrip PySpark:
   ![wc](https://github.com/ZidanAliZaqi/Airflow_HW/assets/97864880/a1b6a010-fce6-4b1e-8ef0-979d33ba507f)
a. Buatlah sebuah skrip PySpark sederhana dengan nama wordcount.py yang 
menghitung jumlah kemunculan setiap kata dalam file teks book.txt.
4. Buat DAG Baru:
   ![pyspa](https://github.com/ZidanAliZaqi/Airflow_HW/assets/97864880/e270ecf2-96ca-48ec-99a3-83b9af32d526)
a. Buatlah file Python baru dengan nama pyspark_dag.py di dalam direktori dags 
Airflow Anda.
6. Definisikan DAG:
   ![jalan tiap hari](https://github.com/ZidanAliZaqi/Airflow_HW/assets/97864880/737a08ce-77d7-41fb-88e5-7ed404ac25bd)
a. Buat sebuah DAG yang dijadwalkan untuk berjalan setiap hari.
8. Gunakan SparkSubmitOperator:
   ![spark submit](https://github.com/ZidanAliZaqi/Airflow_HW/assets/97864880/ec8f600e-be9d-4c5a-a6dd-9e15c80bba83)
a. Tambahkan tugas menggunakan SparkSubmitOperator untuk menjalankan skrip 
PySpark wordcount.py.
9. Konfigurasi Dependensi:
10. Pastikan tugas dalam DAG memiliki dependensi yang benar.
11. Jalankan dan Verifikasi:
12. Jalankan DAG dan verifikasi bahwa pekerjaan PySpark berhasil dijalankan
    ![Screenshot (756)](https://github.com/ZidanAliZaqi/Airflow_HW/assets/97864880/025a4602-e477-4ec1-a293-32d48f8e3802)
    ![Screenshot (757)](https://github.com/ZidanAliZaqi/Airflow_HW/assets/97864880/b9ef4e16-a45f-4895-913b-c51ba106f577)
    ![add conn](https://github.com/ZidanAliZaqi/Airflow_HW/assets/97864880/cbd0a8e4-36ee-4e4e-b132-0c9ed689a3a4)
    Mohon maaf, namun saya mengalami error dalam menjalankan program karena terdapat beberapa kesalahan yang belum dapat saya perbaiki. Mengingat bahwa batas waktu sudah mendekati, dengan segala keterbatasan yang ada, saya akan mengumpulkan apa yang telah saya kerjakan. Terima kasih.
    ![error](https://github.com/ZidanAliZaqi/Airflow_HW/assets/97864880/c188f6df-e1bd-4f99-8981-5aa2b6008ee3)
Berikut Errornya:
```bash
/opt/airflow/logs/dag_id=pyspark_dag/run_id=manual__2024-05-29T16:13:25.821502+00:00/task_id=wordcount/attempt=1.log
[2024-05-29, 16:14:04 UTC] {taskinstance.py:1157} INFO - Dependencies all met for dep_context=non-requeueable deps ti=<TaskInstance: pyspark_dag.wordcount manual__2024-05-29T16:13:25.821502+00:00 [queued]>
[2024-05-29, 16:14:05 UTC] {taskinstance.py:1157} INFO - Dependencies all met for dep_context=requeueable deps ti=<TaskInstance: pyspark_dag.wordcount manual__2024-05-29T16:13:25.821502+00:00 [queued]>
[2024-05-29, 16:14:05 UTC] {taskinstance.py:1359} INFO - Starting attempt 1 of 1
[2024-05-29, 16:14:05 UTC] {taskinstance.py:1380} INFO - Executing <Task(SparkSubmitOperator): wordcount> on 2024-05-29 16:13:25.821502+00:00
[2024-05-29, 16:14:05 UTC] {standard_task_runner.py:57} INFO - Started process 299 to run task
[2024-05-29, 16:14:05 UTC] {standard_task_runner.py:84} INFO - Running: ['***', 'tasks', 'run', 'pyspark_dag', 'wordcount', 'manual__2024-05-29T16:13:25.821502+00:00', '--job-id', '3', '--raw', '--subdir', 'DAGS_FOLDER/pyspark_dag.py', '--cfg-path', '/tmp/tmp83602abw']
[2024-05-29, 16:14:05 UTC] {standard_task_runner.py:85} INFO - Job 3: Subtask wordcount
[2024-05-29, 16:14:05 UTC] {task_command.py:415} INFO - Running <TaskInstance: pyspark_dag.wordcount manual__2024-05-29T16:13:25.821502+00:00 [running]> on host b2d55fc25a46
[2024-05-29, 16:14:06 UTC] {taskinstance.py:1660} INFO - Exporting env vars: AIRFLOW_CTX_DAG_OWNER='Zidan Ali Zaqi' AIRFLOW_CTX_DAG_ID='pyspark_dag' AIRFLOW_CTX_TASK_ID='wordcount' AIRFLOW_CTX_EXECUTION_DATE='2024-05-29T16:13:25.821502+00:00' AIRFLOW_CTX_TRY_NUMBER='1' AIRFLOW_CTX_DAG_RUN_ID='manual__2024-05-29T16:13:25.821502+00:00'
[2024-05-29, 16:14:06 UTC] {base.py:73} INFO - Using connection ID 'spark-conn' for task execution.
[2024-05-29, 16:14:06 UTC] {spark_submit.py:401} INFO - Spark-Submit cmd: spark-submit --master spark://spark-master:7077 --files jobs/python/book.txt --name arrow-spark --deploy-mode client jobs/python/wordcount.py
[2024-05-29, 16:14:06 UTC] {spark_submit.py:571} INFO - /home/***/.local/lib/python3.11/site-packages/pyspark/bin/load-spark-env.sh: line 68: ps: command not found
[2024-05-29, 16:14:06 UTC] {spark_submit.py:571} INFO - /home/***/.local/lib/python3.11/site-packages/pyspark/bin/spark-class: line 71: /usr/lib/jvm/java-11-openjdk-arm64/bin/java: No such file or directory
[2024-05-29, 16:14:06 UTC] {spark_submit.py:571} INFO - /home/***/.local/lib/python3.11/site-packages/pyspark/bin/spark-class: line 97: CMD: bad array subscript
[2024-05-29, 16:14:06 UTC] {taskinstance.py:1935} ERROR - Task failed with exception
Traceback (most recent call last):
  File "/home/airflow/.local/lib/python3.11/site-packages/airflow/providers/apache/spark/operators/spark_submit.py", line 174, in execute
    self._hook.submit(self.application)
  File "/home/airflow/.local/lib/python3.11/site-packages/airflow/providers/apache/spark/hooks/spark_submit.py", line 502, in submit
    raise AirflowException(
airflow.exceptions.AirflowException: Cannot execute: spark-submit --master spark://spark-master:7077 --files jobs/python/book.txt --name arrow-spark --deploy-mode client jobs/python/wordcount.py. Error code is: 1.
[2024-05-29, 16:14:06 UTC] {taskinstance.py:1398} INFO - Marking task as FAILED. dag_id=pyspark_dag, task_id=wordcount, execution_date=20240529T161325, start_date=20240529T161404, end_date=20240529T161406
[2024-05-29, 16:14:06 UTC] {standard_task_runner.py:104} ERROR - Failed to execute job 3 for task wordcount (Cannot execute: spark-submit --master spark://spark-master:7077 --files jobs/python/book.txt --name arrow-spark --deploy-mode client jobs/python/wordcount.py. Error code is: 1.; 299)
[2024-05-29, 16:14:06 UTC] {local_task_job_runner.py:228} INFO - Task exited with return code 1
[2024-05-29, 16:14:06 UTC] {taskinstance.py:2776} INFO - 0 downstream tasks scheduled from follow-on schedule check


    

    
