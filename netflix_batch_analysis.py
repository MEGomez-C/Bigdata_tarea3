from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, explode, split, trim

# 1. Crear la Sesión de Spark
spark = SparkSession.builder \
    .appName("Analisis_Netflix_Batch") \
    .getOrCreate()

# Ajustar el nivel de log
spark.sparkContext.setLogLevel("ERROR")

print("=== CARGANDO Y EXPLORANDO EL DATASET DE NETFLIX ===")

# 2. Cargar el dataset netflix_titles.csv
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("netflix_titles.csv")

# Mostrar esquema y primeros registros
df.printSchema()
df.show(5)

# 3. Limpieza de datos (Manejo de nulos)
df_clean = df.fillna({
    "director": "Desconocido",
    "cast": "Desconocido",
    "country": "Desconocido",
    "rating": "Sin Clasificar"
})

print("=== 1. CONTEO POR TIPO DE CONTENIDO (Películas vs Series) ===")
df_type = df_clean.groupBy("type").count()
df_type.show()

print("=== 2. TOP 10 PAÍSES CON MÁS CONTENIDO EN NETFLIX ===")
# Un título puede tener varios países separados por coma; usamos split y explode
df_countries = df_clean.withColumn("country_single", explode(split(col("country"), ","))) \
                       .withColumn("country_single", trim(col("country_single"))) \
                       .filter(col("country_single") != "Desconocido") \
                       .groupBy("country_single") \
                       .agg(count("*").alias("total_titulos")) \
                       .sort(col("total_titulos").desc())

df_countries.show(10)

print("=== 3. CANTIDAD DE LANZAMIENTOS POR AÑO (Años recientes) ===")
df_years = df_clean.filter(col("release_year") >= 2010) \
                   .groupBy("release_year") \
                   .agg(count("*").alias("total_titulos")) \
                   .sort(col("release_year").desc())

df_years.show(15)

print("=== 4. CLASIFICACIÓN DE CONTENIDO POR EDAD (RATING) ===")
df_rating = df_clean.groupBy("rating") \
                    .agg(count("*").alias("total_titulos")) \
                    .sort(col("total_titulos").desc())

df_rating.show(10)

# Finalizar la sesión
spark.stop()
