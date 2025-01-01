import tkinter as tk
from tkinter import messagebox

from editor import Editor

from shape import Line, Point, Ellipse, Rectangle, Cube, LineOOShape


class MyEditor(Editor):
    def __init__(self, root, canvas, shapes, toolbar, selected_shape_var):
        Editor.__init__(self, canvas, shapes)
        self.selected_shape_var = selected_shape_var
        self.root = root

        self.buttons = []

        self.shapes = shapes  # Статичний масив з 112 елементів

        self.shape_index = 0
        # -------------------------------------------
        self.drawing_shape = None
        self.current_shape_class = None
        # -------------------------------------------
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

    def start(self, shape_class, button, button_state_attr, shape_id):
        self.clear_button_states()
        self.current_shape_class = shape_class
        setattr(self, button_state_attr, True)
        button.config(relief=tk.SUNKEN)
        self.selected_shape_var.set(shape_id)

    def on_mouse_down(self, event):
        if self.current_shape_class:
            if self.shapes.count(None) == 0:
                print("Cannot draw new shape: shape array is full.")
                messagebox.showwarning("Warning", "Cannot draw new shape: shape array is full.")
                return
            self.drawing_shape = self.current_shape_class()
            self.drawing_shape.start_x = event.x
            self.drawing_shape.start_y = event.y

    def on_mouse_move(self, event):
        if self.drawing_shape:
            self.drawing_shape.end_x = event.x
            self.drawing_shape.end_y = event.y

            if isinstance(self.drawing_shape, Cube):
                self.canvas.delete("temp_cube")
                radius_x = abs(event.x - self.drawing_shape.start_x)
                radius_y = abs(event.y - self.drawing_shape.start_y)

                top_x = self.drawing_shape.start_x - radius_x
                top_y = self.drawing_shape.start_y - radius_y
                bottom_x = self.drawing_shape.start_x + radius_x
                bottom_y = self.drawing_shape.start_y + radius_y

                self.canvas.create_rectangle(top_x, top_y, bottom_x, bottom_y,
                                             outline="red", dash=(4, 2), tags="temp_cube")

                offset = 50
                self.canvas.create_rectangle(top_x + offset, top_y - offset, bottom_x + offset, bottom_y - offset,
                                             outline="red", dash=(4, 2), tags="temp_cube")

                self.canvas.create_line(top_x, top_y, top_x + offset, top_y - offset, fill="red", dash=(4, 2),
                                        tags="temp_cube")
                self.canvas.create_line(bottom_x, top_y, bottom_x + offset, top_y - offset, fill="red", dash=(4, 2),
                                        tags="temp_cube")
                self.canvas.create_line(top_x, bottom_y, top_x + offset, bottom_y - offset, fill="red", dash=(4, 2),
                                        tags="temp_cube")
                self.canvas.create_line(bottom_x, bottom_y, bottom_x + offset,
                                        bottom_y - offset, fill="red", dash=(4, 2),
                                        tags="temp_cube")

            elif isinstance(self.drawing_shape, LineOOShape):
                self.canvas.delete("temp_lineEllipse")
                self.canvas.create_line(self.drawing_shape.start_x, self.drawing_shape.start_y,
                                        self.drawing_shape.end_x, self.drawing_shape.end_y,
                                        fill="red", dash=(2, 2), tags="temp_lineEllipse")

                radius = 30
                self.canvas.create_oval(self.drawing_shape.start_x - radius, self.drawing_shape.start_y - radius,
                                        self.drawing_shape.start_x + radius, self.drawing_shape.start_y + radius,
                                        fill="", outline="red", dash=(2, 2), tags="temp_lineEllipse")

                self.canvas.create_oval(self.drawing_shape.end_x - radius, self.drawing_shape.end_y - radius,
                                        self.drawing_shape.end_x + radius, self.drawing_shape.end_y + radius,
                                        fill="", outline="red", dash=(2, 2), tags="temp_lineEllipse")

            elif isinstance(self.drawing_shape, Line):
                self.canvas.delete("temp_line")
                self.canvas.create_line(self.drawing_shape.start_x, self.drawing_shape.start_y,
                                        self.drawing_shape.end_x, self.drawing_shape.end_y,
                                        fill="red", dash=(4, 2), tags="temp_line")

            elif isinstance(self.drawing_shape, Point):
                self.canvas.delete("temp_point")
                self.canvas.create_oval(self.drawing_shape.start_x - 2, self.drawing_shape.start_y - 2,
                                        self.drawing_shape.start_x + 2, self.drawing_shape.start_y + 2,
                                        fill="red", tags="temp_point")

            elif isinstance(self.drawing_shape, Ellipse):
                self.canvas.delete("temp_ellipse")
                self.canvas.create_oval(self.drawing_shape.start_x, self.drawing_shape.start_y,
                                        self.drawing_shape.end_x, self.drawing_shape.end_y,
                                        outline="red", dash=(4, 2), tags="temp_ellipse")

            elif isinstance(self.drawing_shape, Rectangle):
                self.canvas.delete("temp_rectangle")

                radius_x = abs(event.x - self.drawing_shape.start_x)
                radius_y = abs(event.y - self.drawing_shape.start_y)

                top_x = self.drawing_shape.start_x - radius_x
                top_y = self.drawing_shape.start_y - radius_y
                bottom_x = self.drawing_shape.start_x + radius_x
                bottom_y = self.drawing_shape.start_y + radius_y

                self.canvas.create_rectangle(top_x, top_y, bottom_x, bottom_y,
                                             outline="red", dash=(4, 2), tags="temp_rectangle")

    def on_mouse_up(self, event):
        if self.drawing_shape:
            if isinstance(self.drawing_shape, Cube):
                radius_x = abs(event.x - self.drawing_shape.start_x)
                radius_y = abs(event.y - self.drawing_shape.start_y)

                top_x = self.drawing_shape.start_x
                top_y = self.drawing_shape.start_y
                bottom_x = self.drawing_shape.start_x + radius_x
                bottom_y = self.drawing_shape.start_y + radius_y

                self.drawing_shape.draw(self.canvas, top_x, top_y, bottom_x, bottom_y)

            elif isinstance(self.drawing_shape, Rectangle):
                radius_x = abs(event.x - self.drawing_shape.start_x)
                radius_y = abs(event.y - self.drawing_shape.start_y)

                top_x = self.drawing_shape.start_x - radius_x
                top_y = self.drawing_shape.start_y - radius_y
                bottom_x = self.drawing_shape.start_x + radius_x
                bottom_y = self.drawing_shape.start_y + radius_y

                self.drawing_shape.draw(self.canvas, top_x, top_y, bottom_x, bottom_y)

            else:
                self.drawing_shape.end_x = event.x
                self.drawing_shape.end_y = event.y
                self.drawing_shape.draw(self.canvas, self.drawing_shape.start_x, self.drawing_shape.start_y,
                                        self.drawing_shape.end_x, self.drawing_shape.end_y)

            self.add_shape(self.drawing_shape)

            self.drawing_shape = None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.shapes = [None] * 112
        self.shape_index = 0
        print("Canvas and shape array cleared")

        # Оновлюємо редактор, якщо він активний
        if self.current_shape_class:
            self.current_shape_class.shapes = self.shapes  # Оновлюємо масив у редакторі

    # Скидання вибору радіокнопок
    def clear_selection(self):
        self.current_shape_class = None

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
