import tkinter as tk
from tkinter import ttk
from ...product import Product
from ...data_access.sales_repository import SalesRepository
from datetime import date

from .payment_dialog import PaymentDialog

class OrderFrame(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Nuevo Pedido")
        self.geometry("400x500")

        self.products = Product.get_combos()
        self.desserts = Product.get_desserts()

        self.customer_name = tk.StringVar()
        self.combo_s_qty = tk.IntVar()
        self.combo_d_qty = tk.IntVar()
        self.combo_t_qty = tk.IntVar()
        self.flurby_qty = tk.IntVar()

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Ingrese nombre del cliente:").pack(pady=5)
        ttk.Entry(self, textvariable=self.customer_name).pack(pady=5)

        ttk.Label(self, text="Combos:").pack(pady=10)
        for product in self.products:
            frame = ttk.Frame(self)
            frame.pack(pady=2)
            ttk.Label(frame, text=f"{product.name} (${product.cost})").pack(side=tk.LEFT, padx=5)
            if "Simple" in product.name:
                ttk.Entry(frame, textvariable=self.combo_s_qty, width=5).pack(side=tk.RIGHT, padx=5)
            elif "Doble" in product.name:
                ttk.Entry(frame, textvariable=self.combo_d_qty, width=5).pack(side=tk.RIGHT, padx=5)
            elif "Triple" in product.name:
                ttk.Entry(frame, textvariable=self.combo_t_qty, width=5).pack(side=tk.RIGHT, padx=5)
        ttk.Label(self, text="Postre:").pack(pady=10)
        for dessert in self.desserts:
            frame = ttk.Frame(self)
            frame.pack(pady=2)
            ttk.Label(frame, text=f"{dessert.name} (${dessert.cost})").pack(side=tk.LEFT, padx=5)
            ttk.Entry(frame, textvariable=self.flurby_qty, width=5).pack(side=tk.RIGHT, padx=5)
        confirm_button = ttk.Button(self, text="Confirmar Pedido", command=self.confirm_order)
        confirm_button.pack(pady=20)

    def confirm_order(self):
        total = (self.products[0].cost * self.combo_s_qty.get() +
                 self.products[1].cost * self.combo_d_qty.get() +
                 self.products[2].cost * self.combo_t_qty.get() +
                 self.desserts[0].cost * self.flurby_qty.get())

        payment_dialog = PaymentDialog(self, total)
        self.wait_window(payment_dialog)

        sales_repository = SalesRepository()
        if sales_repository.create_sale(self.customer_name.get(), date.today(), self.combo_s_qty.get(), self.combo_d_qty.get(), self.combo_t_qty.get(), self.flurby_qty.get(), total):
            print("Registro de venta guardado correctamente ....")
            self.master.total += total
            self.master.total += total

        self.destroy()
