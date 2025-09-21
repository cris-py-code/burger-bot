from datetime import date
from utils.fileUtility import FileUtility

class Order:
    """
    Representa un pedido realizado por un cliente en la hamburguesería.
    """
    def __init__(self, client_name: str, order_date: date, q_perproduct_list: list['int'], total: int):
        self._client = client_name
        self._date = order_date
        self._q_perproduct_list = q_perproduct_list
        self._total = total

    def save(self):
        data = f"{self.client}; {self.date_str}; {'; '.join(str(num) for num in self.q_perproduct_list)}; {self.total}"
        fileUtility = FileUtility()
        fileUtility.save("ventas.txt", data)

    # ============ GETTERS Y SETTERS (PROPIEDADES) ============

    @property
    def client(self) -> str:
        return self._client

    @client.setter
    def client(self, value: str):
        if not isinstance(value, str):
            raise TypeError("El cliente debe ser una cadena de texto.")
        self._client = value.strip()

    @property
    def date(self) -> date:
        return self._date
    
    @property
    def date_str(self) -> str:
        """
        Obtiene la fecha y hora del pedido como string en formato:
        'Sat Oct 23 10:18:18 2021'
        """
        return self._date.strftime("%a %b %d %H:%M:%S %Y")

    @date.setter
    def date(self, value: date):
        if not isinstance(value, date):
            raise TypeError("La fecha debe ser de tipo 'datetime.date'.")
        self._date = value

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
    