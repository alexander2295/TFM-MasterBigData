
##Este Archivo Tendra las Funciones parametrizadas del proyecto ##

import mysql.connector
from db_config import db_configMaria
from pyspark.sql import SparkSession

def get_params_full(entidad, ambiente=1):
    conn = mysql.connector.connect(
        host=db_configMaria["server"],
        user=db_configMaria["user"],
        password=db_configMaria["password"],
        database=db_configMaria["database"],
        port=db_configMaria["port"]
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT PARAMETRO, VALOR, ORDEN
        FROM params_des
        WHERE ENTIDAD = %s AND AMBIENTE = %s
        ORDER BY ORDEN
    """, (entidad, ambiente))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_params(entidad, ambiente=1):
    """
    Devuelve los parámetros como diccionario {PARAMETRO: VALOR}.
    """
    rows = get_params_full(entidad, ambiente)
    return {row["PARAMETRO"]: row["VALOR"] for row in rows}





def init_spark(ambiente=1, app_name="ProyectoHive"):
    # 1. Recuperar parámetros desde MariaDB
    spark_params = get_params("SPARK", ambiente)

    # 2. Construir el SparkSession con esos parámetros
    builder = SparkSession.builder.appName(app_name)
    for key, value in spark_params.items():
        builder = builder.config(key, value)

    # 3. Crear sesión
    spark = builder.getOrCreate()
    return spark

def get_hdfs_paths(ambiente=1):
    """
    Devuelve un diccionario con las rutas HDFS parametrizadas
    desde la tabla params_des en MariaDB.
    """
    return get_params("HDFS", ambiente)




##Conexion a sql##
def get_sqlserver_connection(ambiente=1):
    """
    Devuelve el jdbc_url y properties para conectarse a SQL Server.
    Los valores se leen de la tabla params_des (entidad SQLSERVER).
    """
    sql_params = get_params("SQLSERVER", ambiente)

    jdbc_url = sql_params["sqlserver.url"]
    properties = {
        "user": sql_params["sqlserver.user"],
        "password": sql_params["sqlserver.password"],
        "driver": sql_params["sqlserver.driver"]
    }

    return jdbc_url, properties