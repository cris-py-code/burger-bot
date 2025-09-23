from datetime import date
from utils.fileUtility import FileUtility

class Order:
    """
    Representa un pedido realizado por un cliente en la hamburguesería.
    """
    def __init__(self, client_name: str, order_date: date, q_perproduct_list: list['int'], total: int):
        self.client = client_name
        self.date = order_date
        self._q_perproduct_list = q_perproduct_list
        self._total = total

    def save(self):
        data = f"{self.client}; {self.date_str}; {'; '.join(str(num) for num in self.q_perproduct_list)}; {self.total}"
        fileUtility = FileUtility()
        fileUtility.save("ventas.txt", data)

    # ============ GETTERS Y SETTERS (PROPIEDADES) ============
    
    @property
    def date_str(self) -> str:
        """
        Obtiene la fecha y hora del pedido como string en formato:
        'Sat Oct 23 10:18:18 2021'
        """
        return self.date.strftime("%a %b %d %H:%M:%S %Y")

    @property
    def q_perproduct_list(self) -> list['int']:
        return self._q_perproduct_list.copy()  # Devuelve copia para evitar mutaciones externas

    @q_perproduct_list.setter
    def q_perproduct_list(self, q_perproduct_list: list['int']):
        if not isinstance(value, list):
            raise TypeError("Los productos deben ser una lista.")
        for value in q_perproduct_list:
            if not isinstance(value, int):
                raise ValueError("No es un número.")
        self._q_perproduct_list = q_perproduct_list.copy()

    @property
    def total(self) -> int:
        return self._total

    @total.setter
    def total(self, value: int):
        if not isinstance(value, (int, int)) or value < 0:
            raise ValueError("El total debe ser un número positivo.")
        self._total = int(value)
    