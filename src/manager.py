from typing import Literal
from utils.fileUtility import FileUtility
from datetime import date

class Manager:
    """
    Representa a un encargado o cajero del local, con su nombre, total recaudado
    y estado de actividad (IN = activo/en turno, OUT = inactivo/fuera de turno).
    """
    def __init__(self, name: str):
        """
        Constructor de la clase Manager.
        
        :param name: Nombre del encargado.
        """
        self._name = name      # Usa el setter para validación

    def save(self, total: int = 0, status: Literal['IN', 'OUT'] = 'IN'):
        """
        :param total: Total recaudado por este encargado (por defecto 0).
        :param status: Estado del encargado, solo puede ser 'IN' o 'OUT' (por defecto 'IN').
        """
        today_date = date.today().strftime("%a %b %d %H:%M:%S %Y")
        data = f"{status} {today_date} Encargad@ {self.name}"

        if status == "OUT":
            data += f" {total}"
            data += "\n##################################################"

        fileUtility = FileUtility()
        fileUtility.save("registro.txt", data)

    # === GETTERS Y SETTERS ===

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self._name = value.strip()
