import os
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv("/etc/credenciales/.env", override=True)

# Configuración de MariaDB
db_configMaria = {
    "server": os.getenv("MB_HOST", "mariadb"),
    "port": int(os.getenv("MB_PORT", "3306")),
    "database": os.getenv("MB_DATABASE", "etl_config"),
    "user": os.getenv("MB_USER", "root"),
    "password": os.getenv("MB_PASSWORD", "StrongPass123")
}
