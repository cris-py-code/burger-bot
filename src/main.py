from menu import Menu
from datetime import datetime
from data_access.records_repository import RecordsRepository

class Main:
    def __init__(self):
        self.menu = Menu()

    def run(self):
        manager_name = self.menu.get_manager()
        
        records_repository = RecordsRepository()
        records_repository.create_record(manager_name, datetime.now(), "IN", 0)
        
        while True:
            option = self.menu.print_menu_inicial()

            if option == 1:
                self.menu.print_menu_opcion_1()
            elif option == 2:
                total = self.menu.get_total_manager()
                records_repository.create_record(manager_name, datetime.now(), "OUT", total)
                manager_name = self.menu.get_manager()
                records_repository.create_record(manager_name, datetime.now(), "IN", 0)
            elif option == 3:
                total = self.menu.get_total_manager()
                records_repository.create_record(manager_name, datetime.now(), "OUT", total)
                print("Apagando sistema. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    app = Main()
    app.run()