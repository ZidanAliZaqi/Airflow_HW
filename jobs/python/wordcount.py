from pyspark.sql import SparkSession

# Inisialisasi sesi Spark
spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()

# Membaca file teks dari folder jobs dan python
file_path = "jobs/python/book.txt"
text_file = spark.sparkContext.textFile(file_path)

# Melakukan split teks menjadi kata-kata
words = text_file.flatMap(lambda line: line.split(" "))

# Melakukan map dan reduce untuk menghitung kata
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# Mengumpulkan dan menampilkan hasil
for wc in wordCounts.collect():
    print(wc[0], wc[1])

# Menghentikan sesi Spark
spark.stop()
