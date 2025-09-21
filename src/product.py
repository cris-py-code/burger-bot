class Product:
    """
    Clase para representar un producto con nombre, descripción y costo.
    """
    def __init__(self, name: str, description: str, cost: int):
        self._name: str = name
        self._description: str = description
        self._cost: int = cost

    # --- Propiedades (Getters y Setters Idiomáticos de Python) ---

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, new_description: str) -> None:
        self._description = new_description

    @property
    def cost(self) -> int:
        return self._cost

    @cost.setter
    def cost(self, new_cost: int) -> None:
        if new_cost >= 0:
            self._cost = new_cost
        
    # --- Métodos de Clase (Fábricas de Objetos) ---
    # Usamos @classmethod y 'cls' en lugar de 'self'

    @classmethod
    def get_combos(cls) -> list['Product']:
        """
        Método de fábrica que retorna una lista de combos predefinidos.
        Usa 'cls' para instanciar la clase (cls(...) es equivalente a Product(...)).
        """
        single_combo = cls("Combo Simple", "Hamburguesa simple + Bebida + Fritas", 5)
        double_combo = cls("Combo Doble", "Hamburguesa doble + Bebida + Fritas", 6)
        triple_combo = cls("Combo Triple", "Hamburguesa Triple + Bebida + Fritas", 7)

        # Corregido el NameError, retornando las variables correctas
        return [single_combo, double_combo, triple_combo]

    @classmethod
    def get_desserts(cls) -> list['Product']:
        """
        Método de fábrica que retorna los postres predefinido.
        """
        mc_flurby_dessert = cls("McFlurby", "Helado de dulce de leche", 2)
        return [mc_flurby_dessert]
    
    def __repr__(self):
        """Representación formal del objeto para debugging."""
        return f"Product(name='{self.name}', cost={self.cost})"