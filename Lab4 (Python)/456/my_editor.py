import tkinter as tk

from shape import Shape
from shape_editor import ShapeEditor


class MyEditor(Shape, ShapeEditor):
    def __init__(self, root, canvas, shapes, toolbar, selected_shape_var):
        Shape.__init__(self)  # Ініціалізація базового класу Shape
        ShapeEditor.__init__(self, canvas, shapes)  # Ініціалізація класу ShapeEditor
        self.selected_shape_var = selected_shape_var
        self.root = root

        self.buttons = []

        self.shapes = shapes  # Статичний масив з 112 елементів
        self.current_editor = None

        self.shape_index = 0

        self.toolbar = toolbar

        self.canvas = canvas
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Прив'язує подію натискання лівої кнопки миші до методу on_mouse_down
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)

        # Прив'язує подію руху миші з натиснутою лівою кнопкою до методу on_mouse_move
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)

        # Прив'язує подію відпускання лівої кнопки миші до методу on_mouse_up
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def add_buttons(self, buttons):
        self.buttons.extend(buttons)

    def create_tool_button(self, icon, tooltip_text, command):
        button = tk.Button(self.toolbar, image=icon, relief=tk.RAISED, command=lambda: command())
        button.pack(side=tk.LEFT)
        self.ToolTip(button, tooltip_text)
        return button

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

    def start(self, editor_class, button, button_state_attr, shape_id):
        self.clear_button_states()
        self.current_editor = editor_class(self.canvas, self.shapes)
        setattr(self, button_state_attr, True)
        button.config(relief=tk.SUNKEN)
        self.selected_shape_var.set(shape_id)

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

    def draw(self, canvas, start_x, start_y, end_x, end_y):
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
        for button in self.buttons:
            button.state = False
            button.config(relief=tk.RAISED)

    class ToolTip:
        def __init__(self, widget, text):
            self.widget = widget
            self.text = text
            self.tip_window = None
            self.widget.bind("<Enter>", self.show_tip)
            self.widget.bind("<Leave>", self.hide_tip)

        def show_tip(self, event=None):
            if self.tip_window or not self.text:
                return
            x, y, _, _ = self.widget.bbox("insert")
            x += self.widget.winfo_rootx() + 25
            y += self.widget.winfo_rooty() + 25

            self.tip_window = tw = tk.Toplevel(self.widget)
            tw.wm_overrideredirect(True)
            tw.wm_geometry(f"+{x}+{y}")

            label = tk.Label(tw, text=self.text, background="white", relief=tk.SOLID, borderwidth=1)
            label.pack()

        def hide_tip(self, event=None):
            tw = self.tip_window
            self.tip_window = None
            if tw:
                tw.destroy()
