from product import Product
from order import Order
from datetime import date

class Menu:
    def __init__(self):
        self._products: list['Product'] = Product.get_combos()
        self._desserts: list['Product'] = Product.get_desserts()
        self._manager: str = None

    @property
    def manager(self) -> str:
        return self._manager
    

    def get_manager(self):
        print("Bienvenido a Hamburguesas IT")
        manager = input("Ingrese su nombre encargad@: ")
        self._manager = manager
        return manager
    
    def print_menu_inicial(self):
        option = 0
        
        print()
        print("Hamburguesas IT")
        print(f"Encargad@ -> {self.manager}")
        print("Recuerda, siempre hay que recibir al")
        print("cliente con una sonrisa :)")
        print()
        print("1 - Ingreso nuevo pedido")
        print("2 - Cambio de turno")
        print("3 - Apagar sistema")
        print()

        try:
            option = int(input("Ingrese una opción (1-3): "))
        except ValueError as e:
            print(f"Entrada inválida. Por favor ingrese un número: {e}")
                
        return option
    
    def print_menu_opcion_1(self):
        while True:
            print()
            print("Menú:")
            for product in self._products:
                print(f"* {product.name} ({product.description}) costo {product.cost} usd")

            print()
            print("Postre:")
            for dessert in self._desserts:
                print(f"* {product.name} ({product.description}) costo {product.cost} usd")

            try:
                print()
                name = input("Ingrese nombre del cliente: ")
                q_combo_s = int(input("Ingrese cantidad Combo S: "))
                q_combo_d = int(input("Ingrese cantidad Combo D: "))
                q_combo_t = int(input("Ingrese cantidad Combo T: "))
                q_flurby = int(input("Ingrese cantidad Flurby: "))
                
                combo_s = self._products[0]
                combo_d = self._products[1]
                combo_t = self._products[2]
                flurby = self._desserts[0]

                total = combo_s.cost * q_combo_s + combo_d.cost * q_combo_d + combo_t.cost * q_combo_t + flurby.cost * q_flurby
                print()
                print(f"Total ${total}")
                abono = int(input("Abona con $ "))
                print(f"Vuelto $ {abono - total}")
                print()

                q_perproduct_list = [q_combo_s, q_combo_d, q_combo_t, q_flurby]
                order = Order(name, date.today(), q_perproduct_list, total)

                confirma = input("¿Confirma pedido? Y/N : ")
                if confirma == "Y":
                    order.save()

                break
            except ValueError as ve:
                print(f"Error en el valor ingresado: {ve}")
        