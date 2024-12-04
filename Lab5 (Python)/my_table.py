import tkinter as tk
from tkinter import ttk


class Table:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Table of Shapes")
        self.window.geometry("600x400")
        self.window.protocol("WM_DELETE_WINDOW", self.hide)  # Немодальне вікно

        self.tree = None
        self.create_table()

    def create_table(self):
        columns = ("shape", "x1", "y1", "x2", "y2")

        frame = tk.Frame(self.window)
        frame.grid(row=0, column=0, sticky="nsew")

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=15)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        self.tree.heading("shape", text="Shape Name")
        self.tree.heading("x1", text="X1")
        self.tree.heading("y1", text="Y1")
        self.tree.heading("x2", text="X2")
        self.tree.heading("y2", text="Y2")

        self.tree.column("shape", width=150, anchor="center")
        self.tree.column("x1", width=100, anchor="center")
        self.tree.column("y1", width=100, anchor="center")
        self.tree.column("x2", width=100, anchor="center")
        self.tree.column("y2", width=100, anchor="center")

    def add_row(self, shape_name, x1, y1, x2, y2):
        self.tree.insert("", tk.END, values=(shape_name, x1, y1, x2, y2))

    def hide(self):
        self.window.withdraw()

    def show(self):
        self.window.deiconify()

    def clear(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
