# config/settings.py

import os
from dotenv import load_dotenv

# Carga las variables de entorno del archivo .env
# Si no se encuentra .env, usa las variables de entorno del sistema (producción)
load_dotenv()

# --- Configuración de la Base de Datos MySQL ---

DB_CONFIG = {
    # Utilizamos os.getenv() para leer las variables del entorno.
    # El segundo argumento es un valor por defecto si la variable no existe.
    # ¡Asegúrate de cambiar los valores por defecto si los usas!
    "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
    "user": os.getenv("MYSQL_USER", "usuario_default"),
    "password": os.getenv("MYSQL_PASSWORD", "password_default"),
    "database": os.getenv("MYSQL_DATABASE", "db_default"),
    # Opcional: Puerto, se convierte a int si es necesario
    "port": int(os.getenv("MYSQL_PORT", 3306)),
    # Opcional: Otras configuraciones del conector de MySQL
    "charset": "utf8mb4",
    "collation": "utf8mb4_unicode_ci"
}

# --- Otras Configuraciones (ej. Paths, Modos) ---

# Define el entorno de la aplicación para lógica condicional
ENVIRONMENT = os.getenv("ENV", "development")

# Ruta base del proyecto (útil para paths relativos)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Bandera para activar/desactivar el modo de depuración
DEBUG = ENVIRONMENT == "development"