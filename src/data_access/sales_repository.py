# data_access/repository.py
from data_access.database_connector import get_db_cursor

class SalesRepository:
    """Clase responsable de todas las operaciones CRUD para la tabla de sales."""

    def get_all_sales(self):
        query = "SELECT id, customer_name, sale_date, combo_s, combo_d, combo_t, flurby, total FROM sales"
        with get_db_cursor() as cursor:
            cursor.execute(query)
            sales = cursor.fetchone()
            return sales
    
    def create_sale(self, customer_name, sale_date, combo_s, combo_d, combo_t, flurby, total):
        query = "INSERT INTO sales (customer_name, sale_date, combo_s, combo_d, combo_t, flurby, total) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        with get_db_cursor() as cursor:
            cursor.execute(query, (customer_name, sale_date, combo_s, combo_d, combo_t, flurby, total))
            # El commit se hace automáticamente en __exit__ del DBConnector
            return cursor.lastrowid
