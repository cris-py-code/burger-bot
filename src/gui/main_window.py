import tkinter as tk
from tkinter import ttk
from .widgets.order_frame import OrderFrame
from ..data_access.records_repository import RecordsRepository
from datetime import datetime

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Burger Bot")
        self.geometry("800x600")

        self.manager_name = tk.StringVar()
        self.total = 0

        self.create_login_screen()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_login_screen(self):
        self.login_frame = ttk.Frame(self)
        self.login_frame.pack(pady=20)

        ttk.Label(self.login_frame, text="Bienvenido a Hamburguesas IT").pack(pady=10)
        ttk.Label(self.login_frame, text="Ingrese su nombre encargad@:").pack(pady=5)
        
        manager_entry = ttk.Entry(self.login_frame, textvariable=self.manager_name)
        manager_entry.pack(pady=5)

        login_button = ttk.Button(self.login_frame, text="Login", command=self.login)
        login_button.pack(pady=10)

    def login(self):
        if self.manager_name.get():
            records_repository = RecordsRepository()
            records_repository.create_record(self.manager_name.get(), datetime.now(), "IN", 0)
            self.login_frame.destroy()
            self.create_main_screen()

    def on_closing(self):
        records_repository = RecordsRepository()
        records_repository.create_record(self.manager_name.get(), datetime.now(), "OUT", self.total)
        self.destroy()

    def create_main_screen(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(pady=20)

        ttk.Label(self.main_frame, text=f"Encargad@ -> {self.manager_name.get()}").pack(pady=10)

        new_order_button = ttk.Button(self.main_frame, text="Ingreso nuevo pedido", command=self.create_new_order)
        new_order_button.pack(pady=5)

        change_shift_button = ttk.Button(self.main_frame, text="Cambio de turno", command=self.change_shift)
        change_shift_button.pack(pady=5)

        exit_button = ttk.Button(self.main_frame, text="Apagar sistema", command=self.on_closing)
        exit_button.pack(pady=5)

    def create_new_order(self):
        order_frame = OrderFrame(self)
        self.wait_window(order_frame)

    def change_shift(self):
        records_repository = RecordsRepository()
        records_repository.create_record(self.manager_name.get(), datetime.now(), "OUT", self.total)
        self.total = 0
        self.main_frame.destroy()
        self.create_login_screen()