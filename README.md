# Airflow_HW
Tugas: Menjalankan Pekerjaan PySpark Menggunakan SparkSubmitOperator di Airflow
Tujuan: Membuat DAG di Airflow untuk menjalankan pekerjaan PySpark menggunakan 
SparkSubmitOperator.
Instruksi:
1. Persiapkan Airflow: Pastikan Airflow telah terinstal dan dikonfigurasi dengan benar di lingkungan 
Anda.
2. Buat Skrip PySpark:
a. Buatlah sebuah skrip PySpark sederhana dengan nama wordcount.py yang 
menghitung jumlah kemunculan setiap kata dalam file teks book.txt.
3. Buat DAG Baru:
a. Buatlah file Python baru dengan nama pyspark_dag.py di dalam direktori dags 
Airflow Anda.
4. Definisikan DAG:
a. Buat sebuah DAG yang dijadwalkan untuk berjalan setiap hari.
5. Gunakan SparkSubmitOperator:
a. Tambahkan tugas menggunakan SparkSubmitOperator untuk menjalankan skrip 
PySpark wordcount.py.
6. Konfigurasi Dependensi:
7. Pastikan tugas dalam DAG memiliki dependensi yang benar.
8. Jalankan dan Verifikasi:
9. Jalankan DAG dan verifikasi bahwa pekerjaan PySpark berhasil dijalankan