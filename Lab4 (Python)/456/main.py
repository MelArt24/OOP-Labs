import tkinter as tk
from tkinter import messagebox

from my_editor import MyEditor

from point_editor import PointEditor
from line_editor import LineEditor
from rect_editor import RectEditor
from ellipse_editor import EllipseEditor
from cube_editor import CubeEditor
from lineooshape_editor import LineOOShapeEditor


def show_about():
    messagebox.showinfo("About", "Lab4 version 1.0")


def main():
    root = tk.Tk()
    root.title("Graphic editor")
    root.geometry("800x600")
    root.minsize(400, 300)
    root.maxsize(1600, 900)

    toolbar = tk.Frame(root)
    toolbar.pack(side=tk.TOP, fill=tk.X)

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    selected_shape_var = tk.IntVar()

    icon1 = tk.PhotoImage(file="C:/Users/User/Desktop/Матеріали для університету/2 курс 1 "
                               "семестр/ООП/Лабораторні роботи/Лаба 3/Point.png")
    icon2 = tk.PhotoImage(file="C:/Users/User/Desktop/Матеріали для університету/2 курс 1 "
                               "семестр/ООП/Лабораторні роботи/Лаба 3/Line.png")
    icon3 = tk.PhotoImage(file="C:/Users/User/Desktop/Матеріали для університету/2 курс 1 "
                               "семестр/ООП/Лабораторні роботи/Лаба 3/Rectangle.png")
    icon4 = tk.PhotoImage(file="C:/Users/User/Desktop/Матеріали для університету/2 курс 1 "
                               "семестр/ООП/Лабораторні роботи/Лаба 3/Ellipse.png")
    icon5 = tk.PhotoImage(file="C:/Users/User/Desktop/Матеріали для університету/2 курс 1 "
                               "семестр/ООП/Лабораторні роботи/Лаба 3/Clear.png")
    icon6 = tk.PhotoImage(file="C:/Users/User/Desktop/Матеріали для університету/2 курс 1 "
                               "семестр/ООП/Лабораторні роботи/Лаба 3/Cube.png")
    icon7 = tk.PhotoImage(file="C:/Users/User/Desktop/Матеріали для університету/2 курс 1 "
                               "семестр/ООП/Лабораторні роботи/Лаба 3/LineOOShape.png")

    shapes = [None] * 112  # Масив для фігур
    editor = MyEditor(root, canvas, shapes, toolbar, selected_shape_var)

    # Меню
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # Меню Файл
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New...")
    file_menu.add_command(label="Open...")
    file_menu.add_command(label="Save as...")
    file_menu.add_separator()
    file_menu.add_command(label="Print")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)

    button_states = {
        'button1': False,
        'button2': False,
        'button3': False,
        'button4': False,
        'button5': False,
        'button6': False
    }

    def create_toggle_button(icon, text, editor_class, button_name, shape_id):
        def toggle_button():
            if button_states[button_name]:
                button_states[button_name] = False
                button.config(relief=tk.RAISED)
                editor.selected_shape_var.set(0)
                editor.current_editor = None
            else:
                button_states[button_name] = True
                button.config(relief=tk.SUNKEN)
                editor.selected_shape_var.set(shape_id)
                editor.start(editor_class, button, button_name, shape_id)

        button = editor.create_tool_button(icon, text, toggle_button)
        return button

    button1 = create_toggle_button(icon1, "Point", PointEditor, 'button1', 1)
    button2 = create_toggle_button(icon2, "Line", LineEditor, 'button2', 2)
    button3 = create_toggle_button(icon3, "Rectangle", RectEditor, 'button3', 3)
    button4 = create_toggle_button(icon4, "Ellipse", EllipseEditor, 'button4', 4)
    button5 = create_toggle_button(icon6, "Cube", CubeEditor, 'button5', 5)
    button6 = create_toggle_button(icon7, "LineOOShape", LineOOShapeEditor, 'button6', 6)

    button_clear = tk.Button(toolbar, image=icon5, command=editor.clear_canvas)
    button_clear.pack(side=tk.LEFT, padx=5)
    editor.ToolTip(button_clear, "Clear Canvas")
    editor.add_buttons([button1, button2, button3, button4, button5, button6])

    # Меню Shapes
    shapes_menu = tk.Menu(menubar, tearoff=0)
    shapes_menu.add_radiobutton(label="Point", variable=editor.selected_shape_var, value=1,
                                command=lambda: editor.start(PointEditor, button1, 'button1_state', 1))
    shapes_menu.add_radiobutton(label="Line", variable=editor.selected_shape_var, value=2,
                                command=lambda: editor.start(LineEditor, button2, 'button2_state', 2))
    shapes_menu.add_radiobutton(label="Rectangle", variable=editor.selected_shape_var, value=3,
                                command=lambda: editor.start(RectEditor, button3, 'button3_state', 3))
    shapes_menu.add_radiobutton(label="Ellipse", variable=editor.selected_shape_var, value=4,
                                command=lambda: editor.start(EllipseEditor, button4, 'button4_state', 4))
    shapes_menu.add_radiobutton(label="Cube", variable=editor.selected_shape_var, value=5,
                                command=lambda: editor.start(CubeEditor, button5, 'button5_state', 5))
    shapes_menu.add_radiobutton(label="LineOOShape", variable=editor.selected_shape_var, value=6,
                                command=lambda: editor.start(LineOOShapeEditor, button6, 'button6_state', 6))
    shapes_menu.add_separator()
    shapes_menu.add_command(label="Delete choice", command=editor.clear_selection)
    shapes_menu.add_separator()
    shapes_menu.add_command(label="Clear", command=editor.clear_canvas)
    menubar.add_cascade(label="Shapes", menu=shapes_menu)

    # Меню Допомога
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="About", command=show_about)
    menubar.add_cascade(label="Help", menu=help_menu)

    # Запуск
    root.mainloop()


if __name__ == "__main__":
    main()
