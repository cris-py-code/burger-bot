from menu import Menu
from manager import Manager

class Main:
    def __init__(self):
        self.menu = Menu()

    def run(self):
        manager_name = self.menu.get_manager()
        manager = Manager(manager_name)
        manager.save()
        
        while True:
            option = self.menu.print_menu_inicial()

            if option == 1:
                self.menu.print_menu_opcion_1()
            elif option == 2:
                total = self.menu.get_total_manager()
                manager.save(total, "OUT")
                manager_name = self.menu.get_manager()
                manager = Manager(manager_name)
                manager.save()
            elif option == 3:
                total = self.menu.get_total_manager()
                manager.save(total, "OUT")
                print("Apagando sistema. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    app = Main()
    app.run()