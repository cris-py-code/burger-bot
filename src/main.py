from menu import Menu
from manager import Manager

class Main:
    def __init__(self):
        self._menu = Menu()

    def run(self):
        manager_name, total = self._menu.get_manager()
        manager = Manager(manager_name)
        manager.save()
        
        while True:
            option = self._menu.print_menu_inicial()

            if option == 1:
                self._menu.print_menu_opcion_1()
            elif option == 2:
                manager_name, total = self._menu.get_manager()
                manager.save(total, "OUT")
                manager = Manager(manager_name)
                manager.save()
            elif option == 3:
                print("Apagando sistema. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    app = Main()
    app.run()