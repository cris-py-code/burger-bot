from pathlib import Path
from typing import Optional

class FileUtility:
    """
    Utilidad para manejar operaciones de escritura de archivos en rutas relativas
    al proyecto. Por defecto, guarda en la carpeta 'data/' en la raíz del proyecto.
    """

    def __init__(self, folder_name: str = "data"):
        """
        Inicializa la utilidad de archivos con una carpeta de destino.

        :param folder_name: Nombre de la carpeta relativa a la raíz del proyecto
                            donde se guardarán los archivos (por defecto: "data").
        """
        # Calcula la ruta base: dos niveles arriba desde este archivo (sale de src/utils/)
        self._base_path = Path(__file__).parent.parent.parent / folder_name
        # Crea la carpeta si no existe
        self._base_path.mkdir(exist_ok=True)

    def save(self, file_name: str, data_to_save: str) -> bool:
        """
        Guarda una cadena de texto en un archivo dentro de la carpeta configurada.
        Si el archivo no existe, se crea. Si existe, se agrega al final (modo append).

        :param file_name: Nombre del archivo (ej: "ventas.txt").
        :param data_to_save: Contenido a guardar (una línea de texto).
        :return: True si se guardó con éxito, False en caso de error.
        :raises TypeError: Si los parámetros no son del tipo esperado.
        """
        # Validación de tipos
        if not isinstance(file_name, str) or not file_name.strip():
            raise TypeError("El nombre del archivo debe ser una cadena no vacía.")
        if not isinstance(data_to_save, str):
            raise TypeError("Los datos a guardar deben ser una cadena de texto.")

        try:
            complete_path = self._base_path / file_name
            with open(complete_path, "a", encoding="utf-8") as file:
                file.write(data_to_save + "\n")
            return True
            
        except PermissionError:
            print(f"Error: No se tienen permisos para escribir en {complete_path}")
            return False
        except OSError as e:
            print(f"Error del sistema al guardar en {complete_path}: {e}")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar archivo: {e}")
            return False