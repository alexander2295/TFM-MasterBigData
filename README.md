📊 TFM-Proyecto-Hadoop

Proyecto de análisis de datos con arquitectura Big Data basada en Hadoop, Spark y Hive, que permite la extracción, procesamiento, limpieza y almacenamiento
de datos desde distintas fuentes hacia un Data Lake (HDFS) y su exposición final en MySQL para análisis y visualización.

📖 Índice

🔧 Requisitos previos

🧱 Arquitectura del proyecto

📂 Estructura del repositorio

⚙️ Instalación y configuración

🚀 Ejecución de procesos ETL

🧠 Procesamiento en Spark

💾 Persistencia y consultas con Hive y MySQL

📈 Buenas prácticas y optimización

🧰 Troubleshooting (problemas comunes)

🔧 Requisitos previos

Antes de ejecutar el proyecto asegúrate de contar con:

Componente	Versión recomendada	Descripción

✅ Docker & Docker Compose	≥ 20.10	Contenedores del ecosistema Hadoop

✅ Python	≥ 3.10	Scripts de control y pruebas locales

✅ Apache Spark	3.5.x	Motor de procesamiento distribuido

✅ Apache Hive	3.x	Metastore y capa SQL sobre HDFS

✅ HDFS (Hadoop)	3.x	Sistema distribuido de archivos

✅ MySQL Server	≥ 8.x	Base de datos relacional para resultados

✅ Git	-	Control de versiones del proyecto

📂 Estructura del proyecto

TFM-Proyecto-Hadoop/

│── docker-compose.yml         # Levanta HDFS, Spark y Hive

│── spark/                     # Configuración de Spark y scripts ETL

│   ├── etl_bronze_pedidos.py  # Extracción y carga en capa Bronze

│   ├── etl_silver_clientes.py # Limpieza y enriquecimiento

│   ├── etl_gold_reportes.py   # Agregaciones finales

│   ├── create_bronze_tables.sql
│   ├── create_silver_tables.sql
│── mysql/                     # Exportadores y conexión a MySQL

│── notebooks/                 # Notebooks de análisis exploratorio

│── data/                      # Datos fuente (si aplica)

│── requirements.txt           # Dependencias Python

│── README.md                  # Documentación del proyecto

│── .env                       # Variables de entorno del cluster



⚙️ Instalación y configuración

1️⃣ Clona el repositorio

git clone https://github.com/alexander2295/TFM-Proyecto-Hadoop.git
cd TFM-Proyecto-Hadoop


2️⃣ Levanta el ecosistema Hadoop

docker-compose up -d


Esto iniciará:

namenode, datanode → HDFS

spark-master, spark-worker → Spark Cluster

hive-metastore, hive-server → Catálogo SQL

mysql → Persistencia final

3️⃣ Verifica que los servicios estén activos

docker ps


4️⃣ Instala dependencias locales

pip install -r requirements.txt


