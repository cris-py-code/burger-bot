from data_access.database_connector import get_db_cursor

class RecordsRepository:
    """Clase responsable de todas las operaciones CRUD para la tabla de records."""

    def get_all_records(self):
        query = "SELECT id, manager_name, record_date, movement, cash FROM recods"
        with get_db_cursor() as cursor:
            cursor.execute(query)
            return cursor.fetall()

    def create_record(self, manager_name, record_date, movement, cash):
        query = "INSERT INTO records (manager_name, record_date, movement, cash) VALUES (%s, %s, %s, %s)"
        with get_db_cursor() as cursor:
            cursor.execute(query, (manager_name, record_date, movement, cash))
            # El commit se hace automáticamente en __exit__ del DBConnector
            return cursor.lastrowid
