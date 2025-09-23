from product import Product
from order import Order
from datetime import date

class Menu:
    def __init__(self):
        self.products: list['Product'] = Product.get_combos()
        self.desserts: list['Product'] = Product.get_desserts()
        self.manager: str = None
        self.total: int = 0
    
    def get_manager(self):
        print("Bienvenido a Hamburguesas IT")
        self.manager = input("Ingrese su nombre encargad@: ")
        self.total = 0
        return self.manager
    
    def get_total_manager(self):                
        return self.total
    
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
            for product in self.products:
                print(f"* {product.name} ({product.description}) costo {product.cost} usd")

            print()
            print("Postre:")
            for dessert in self.desserts:
                print(f"* {product.name} ({product.description}) costo {product.cost} usd")

            try:
                print()
                name = input("Ingrese nombre del cliente: ")
                q_combo_s = int(input("Ingrese cantidad Combo S: "))
                q_combo_d = int(input("Ingrese cantidad Combo D: "))
                q_combo_t = int(input("Ingrese cantidad Combo T: "))
                q_flurby = int(input("Ingrese cantidad Flurby: "))
                
                combo_s = self.products[0]
                combo_d = self.products[1]
                combo_t = self.products[2]
                flurby = self.desserts[0]

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
                    self.total += total
                    order.save()

                break
            except ValueError as ve:
                print(f"Error en el valor ingresado: {ve}")
   
        