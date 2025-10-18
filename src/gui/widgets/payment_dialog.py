import tkinter as tk
from tkinter import ttk

class PaymentDialog(tk.Toplevel):
    def __init__(self, master, total):
        super().__init__(master)
        self.title("Pagar")
        self.geometry("300x200")
        self.total = total

        self.amount_paid = tk.IntVar()

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text=f"Total a pagar: ${self.total}").pack(pady=10)

        ttk.Label(self, text="Abona con:").pack(pady=5)
        ttk.Entry(self, textvariable=self.amount_paid).pack(pady=5)

        calculate_change_button = ttk.Button(self, text="Calcular Vuelto", command=self.calculate_change)
        calculate_change_button.pack(pady=10)

        self.change_label = ttk.Label(self, text="")
        self.change_label.pack(pady=5)

        confirm_button = ttk.Button(self, text="Confirmar Pago", command=self.confirm_payment)
        confirm_button.pack(pady=10)

    def confirm_payment(self):
        self.destroy()
    def calculate_change(self):
        change = self.amount_paid.get() - self.total
        self.change_label.config(text=f"Vuelto: ${change}")
