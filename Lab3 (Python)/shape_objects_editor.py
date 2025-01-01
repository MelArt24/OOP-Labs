import tkinter as tk
from tkinter import messagebox
from shape import Shape
from shape_editor import ShapeEditor

from point_editor import PointEditor
from line_editor import LineEditor
from rect_editor import RectEditor
from ellipse_editor import EllipseEditor

from tooltip import ToolTip


def show_about():
    messagebox.showinfo("About", "Lab3 version 1.0")


class ShapeObjectsEditor(Shape, ShapeEditor):
    def __init__(self, root):
        Shape.__init__(self)  # Ініціалізація базового класу Shape
        ShapeEditor.__init__(self)  # Ініціалізація класу ShapeEditor
        self.selected_shape_var = None
        self.root = root
        self.root.title("Graphic editor")
        self.root.geometry("800x600")
        self.root.minsize(400, 300)
        self.root.maxsize(1600, 900)

        self.shapes = [None] * 112  # Статичний масив з 112 елементів
        self.current_editor = None

        self.shape_index = 0

        self.toolbar = tk.Frame(root)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.icon1 = tk.PhotoImage(file="C:/Users/User/Desktop/Матеріали для університету/2 курс 1 "
                                        "семестр/ООП/Лабораторні роботи/Лаба 3/Point.png")
        self.icon2 = tk.PhotoImage(file="C:/Users/User/Desktop/Матеріали для університету/2 курс 1 "
                                        "семестр/ООП/Лабораторні роботи/Лаба 3/Line.png")
        self.icon3 = tk.PhotoImage(file="C:/Users/User/Desktop/Матеріали для університету/2 курс 1 "
                                        "семестр/ООП/Лабораторні роботи/Лаба 3/Rectangle.png")
        self.icon4 = tk.PhotoImage(file="C:/Users/User/Desktop/Матеріали для університету/2 курс 1 "
                                        "семестр/ООП/Лабораторні роботи/Лаба 3/Ellipse.png")
        self.icon5 = tk.PhotoImage(file="C:/Users/User/Desktop/Матеріали для університету/2 курс 1 "
                                        "семестр/ООП/Лабораторні роботи/Лаба 3/Clear.png")

        # BUTTON 1
        self.button1_state = False

        def toggle_button1():
            if self.button1_state:
                self.button1_state = False
                self.button1.config(relief=tk.RAISED)
                self.selected_shape_var.set(0)
                self.current_editor = None
            else:
                self.button1_state = True
                self.button1.config(relief=tk.SUNKEN)
                self.selected_shape_var.set(1)
                self.set_point_editor()
        self.button1 = self.create_tool_button(self.icon1, "Point", toggle_button1)

        # BUTTON 2
        self.button2_state = False

        def toggle_button2():
            if self.button2_state:
                self.button2_state = False
                self.button2.config(relief=tk.RAISED)
                self.selected_shape_var.set(0)
                self.current_editor = None
            else:
                self.button2_state = True
                self.button2.config(relief=tk.SUNKEN)
                self.selected_shape_var.set(2)
                self.set_line_editor()

        self.button2 = self.create_tool_button(self.icon2, "Line", toggle_button2)

        # BUTTON 3
        self.button3_state = False  # Стан кнопки: False - не натиснута, True - натиснута

        def toggle_button3():
            if self.button3_state:
                self.button3_state = False
                self.button3.config(relief=tk.RAISED)  # Повертаємо вигляд кнопки до звичайного
                self.selected_shape_var.set(0)  # Знімаємо вибір з радіобатонів
                self.current_editor = None  # Вимикаємо редактор
            else:
                self.button3_state = True
                self.button3.config(relief=tk.SUNKEN)  # Змінюємо вигляд кнопки на зажату
                self.selected_shape_var.set(3)  # Встановлюємо вибір для Rectangle
                self.set_rect_editor()  # Активуємо редактор для прямокутника

        self.button3 = self.create_tool_button(self.icon3, "Rectangle", toggle_button3)

        # BUTTON 4
        self.button4_state = False

        def toggle_button4():
            if self.button4_state:
                self.button4_state = False
                self.button4.config(relief=tk.RAISED)
                self.selected_shape_var.set(0)
                self.current_editor = None
            else:
                self.button4_state = True
                self.button4.config(relief=tk.SUNKEN)
                self.selected_shape_var.set(4)
                self.set_ellipse_editor()
        self.button4 = self.create_tool_button(self.icon4, "Ellipse", toggle_button4)

        # BUTTON CLEAR
        self.button_clear = tk.Button(self.toolbar, image=self.icon5, command=self.clear_canvas)
        self.button_clear.pack(side=tk.LEFT, padx=5)
        ToolTip(self.button_clear, "Clear Canvas")
        # # padx=2, pady=2 - відступи

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Меню
        self.menubar = tk.Menu(root)
        self.create_menus()

        self.root.config(menu=self.menubar)

        # Прив'язує подію натискання лівої кнопки миші до методу on_mouse_down
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)

        # Прив'язує подію руху миші з натиснутою лівою кнопкою до методу on_mouse_move
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)

        # Прив'язує подію відпускання лівої кнопки миші до методу on_mouse_up
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def create_tool_button(self, icon, tooltip_text, command):
        button = tk.Button(self.toolbar, image=icon, relief=tk.RAISED, command=lambda: command())
        button.pack(side=tk.LEFT)
        ToolTip(button, tooltip_text)
        return button

    def create_menus(self):
        # Меню Файл
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="New...")
        file_menu.add_command(label="Open...")
        file_menu.add_command(label="Save as...")
        file_menu.add_separator()
        file_menu.add_command(label="Print")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=file_menu)

        # Меню Shapes
        self.selected_shape_var = tk.IntVar(value=0)

        shapes_menu = tk.Menu(self.menubar, tearoff=0)
        shapes_menu.add_radiobutton(label="Point", variable=self.selected_shape_var, value=1,
                                    command=lambda: self.set_point_editor())
        shapes_menu.add_radiobutton(label="Line", variable=self.selected_shape_var, value=2,
                                    command=lambda: self.set_line_editor())
        shapes_menu.add_radiobutton(label="Rectangle", variable=self.selected_shape_var, value=3,
                                    command=lambda: self.set_rect_editor())
        shapes_menu.add_radiobutton(label="Ellipse", variable=self.selected_shape_var, value=4,
                                    command=lambda: self.set_ellipse_editor())
        shapes_menu.add_separator()
        shapes_menu.add_command(label="Delete choice", command=lambda: self.clear_selection())
        shapes_menu.add_separator()
        shapes_menu.add_command(label="Clear", command=lambda: self.clear_canvas())
        self.menubar.add_cascade(label="Shapes", menu=shapes_menu)

        # Меню Допомога
        help_menu = tk.Menu(self.menubar, tearoff=0)
        help_menu.add_command(label="About", command=show_about)
        self.menubar.add_cascade(label="Help", menu=help_menu)

    def add_shape(self, shape):
        if shape is None:
            print("Error: Trying to add None as a shape")
            return

        max_shapes = len(self.shapes)

        if self.shape_index < max_shapes:
            self.shapes[self.shape_index] = shape
            print(f"Added shape at index {self.shape_index}: {shape}")
            self.shape_index += 1
        else:
            print("Shape array is full")

    def set_point_editor(self):
        self.clear_button_states()
        self.current_editor = PointEditor(self.canvas, self.shapes)
        self.button1_state = True  # Кнопка зажата
        self.button1.config(relief=tk.SUNKEN)  # Змінюємо вигляд кнопки на зажату
        self.selected_shape_var.set(1)  # Встановлюємо вибір для "Rectangle"

    def set_line_editor(self):
        self.clear_button_states()
        self.current_editor = LineEditor(self.canvas, self.shapes)
        self.button2_state = True
        self.button2.config(relief=tk.SUNKEN)
        self.selected_shape_var.set(2)

    def set_rect_editor(self):
        self.clear_button_states()
        self.current_editor = RectEditor(self.canvas, self.shapes)
        self.button3_state = True
        self.button3.config(relief=tk.SUNKEN)
        self.selected_shape_var.set(3)

    def set_ellipse_editor(self):
        self.clear_button_states()
        self.current_editor = EllipseEditor(self.canvas, self.shapes)
        self.button4_state = True
        self.button4.config(relief=tk.SUNKEN)
        self.selected_shape_var.set(4)

    def on_mouse_down(self, event):
        if self.current_editor:
            self.current_editor.on_mouse_down(event)

    def on_mouse_move(self, event):
        if self.current_editor:
            self.current_editor.on_mouse_move(event)

    def on_mouse_up(self, event):
        if self.current_editor:
            new_shape = self.current_editor.on_mouse_up(event)
            if new_shape is not None:
                if self.shape_index < len(self.shapes):
                    self.add_shape(new_shape)

    def on_paint(self, canvas):
        pass

    def draw(self, canvas):
        pass

    def clear_canvas(self):
        self.canvas.delete("all")
        self.shapes = [None] * 112
        self.shape_index = 0
        print("Canvas and shape array cleared")

        # Оновлюємо редактор, якщо він активний
        if self.current_editor:
            self.current_editor.shapes = self.shapes  # Оновлюємо масив у редакторі

    # Скидання вибору радіокнопок
    def clear_selection(self):
        self.current_editor = None

        self.clear_button_states()

        self.selected_shape_var.set(0)
        self.root.update_idletasks()
        print("Selection cleared")

    # Скидання станів кнопок
    def clear_button_states(self):
        self.button1_state = False
        self.button1.config(relief=tk.RAISED)  # Повертаємо кнопку до звичайного вигляду
        self.button2_state = False
        self.button2.config(relief=tk.RAISED)
        self.button3_state = False
        self.button3.config(relief=tk.RAISED)
        self.button4_state = False
        self.button4.config(relief=tk.RAISED)
