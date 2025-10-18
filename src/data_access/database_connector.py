# data_access/database_connector.py
import mysql.connector
from ..config.settings import DB_CONFIG

class DBConnector:
    """Clase para gestionar la conexión y el cursor de MySQL."""

    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        """Establece la conexión a la base de datos."""
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            self.cursor = self.connection.cursor(dictionary=True) # Devuelve resultados como diccionarios
            print("Conexión a MySQL establecida.")
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
            raise

    def close(self):
        """Cierra el cursor y la conexión."""
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión a MySQL cerrada.")

    # Uso de un Context Manager (patrón de diseño clave)
    def __enter__(self):
        self.connect()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.connection.rollback() # Revierte si hay error
        else:
            self.connection.commit() # Confirma si no hay error
        self.close()

# Función de utilidad para usar el Context Manager
def get_db_cursor():
    return DBConnector()