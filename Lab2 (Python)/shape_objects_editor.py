import tkinter as tk
from tkinter import messagebox
from shape import Shape
from shape_editor import ShapeEditor

from point_editor import PointEditor
from line_editor import LineEditor
from rect_editor import RectEditor
from ellipse_editor import EllipseEditor


class ShapeObjectsEditor(Shape, ShapeEditor):
    def __init__(self, root):
        Shape.__init__(self)  # Ініціалізація базового класу Shape
        ShapeEditor.__init__(self)  # Ініціалізація класу ShapeEditor
        self.root = root
        self.root.title("Graphic editor")
        self.root.geometry("800x600")  # Задати початковий розмір вікна
        self.root.minsize(400, 300)  # Мінімальний розмір вікна
        self.root.maxsize(1600, 900)  # Максимальний розмір вікна

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Список для зберігання всіх намальованих фігур
        self.shapes = [None] * 112  # Масив з 112 елементів
        self.current_editor = None  # Змінна для поточного редактора

        self.shape_index = 0  # Індекс для додавання нових фігур

        # Меню
        menubar = tk.Menu(root)

        # Меню Файл
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Меню Фігури
        self.shape_menu = tk.Menu(menubar, tearoff=0)
        self.on_init_menu_popup(self.shape_menu)  # Викликаємо метод для заповнення меню
        menubar.add_cascade(label="Shapes", menu=self.shape_menu)

        # Меню Допомога
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        root.config(menu=menubar)

        # Прив'язує подію натискання лівої кнопки миші до методу on_mouse_down
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)

        # Прив'язує подію руху миші з натиснутою лівою кнопкою до методу on_mouse_move
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)

        # Прив'язує подію відпускання лівої кнопки миші до методу on_mouse_up
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def add_shape(self, shape):
        if shape is None:
            print("Error: Trying to add None as a shape")
            return

        max_shapes = 112
        if self.shape_index < max_shapes:
            if self.shape_index < len(self.shapes):
                self.shapes[self.shape_index] = shape
            else:
                self.shapes.append(shape)
            print(f"Added shape at index {self.shape_index}: {shape}")
            self.shape_index += 1
        else:
            print("Shape array is full")

    def on_init_menu_popup(self, menu):
        # Додаємо пункти меню для вибору фігур
        menu.add_radiobutton(label="Point", command=lambda: self.set_point_editor())
        menu.add_radiobutton(label="Line", command=lambda: self.set_line_editor())
        menu.add_radiobutton(label="Rectangle", command=lambda: self.set_rect_editor())
        menu.add_radiobutton(label="Ellipse", command=lambda: self.set_ellipse_editor())
        menu.add_separator()
        menu.add_command(label="Clear", command=lambda: self.clear_canvas())

    def set_point_editor(self):
        self.current_editor = PointEditor(self.canvas, self.shapes)

    def set_line_editor(self):
        self.current_editor = LineEditor(self.canvas, self.shapes)

    def set_rect_editor(self):
        self.current_editor = RectEditor(self.canvas, self.shapes)

    def set_ellipse_editor(self):
        self.current_editor = EllipseEditor(self.canvas, self.shapes)

    def on_mouse_down(self, event):
        if self.current_editor:
            self.current_editor.on_mouse_down(event)

    def on_mouse_move(self, event):
        if self.current_editor:
            self.current_editor.on_mouse_move(event)

    def on_mouse_up(self, event):
        if self.current_editor:
            new_shape = self.current_editor.on_mouse_up(event)
            self.add_shape(new_shape)  # Додаємо нову фігуру у масив

    def on_paint(self, canvas):
        pass

    def draw(self, canvas):
        pass

    def clear_canvas(self):
        self.canvas.delete("all")
        self.shapes = [None] * 112  # Очищуємо масив фігур
        self.shape_index = 0
        print("Canvas and shape array cleared")

    def show_about(self):
        messagebox.showinfo("About", "Lab2 version 1.0")
