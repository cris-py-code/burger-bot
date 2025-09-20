from menu import Menu

class Main:
    def __init__(self):
        self._menu = Menu()

    def run(self):
        manager = self._menu.get_manager()
        
        while True:
            option = self._menu.print_menu_inicial()

            if option == 1:
                self._menu.print_menu_opcion_1()
            elif option == 2:
                print("Opción por definir")
            elif option == 3:
                print("Apagando sistema. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    app = Main()
    app.run()