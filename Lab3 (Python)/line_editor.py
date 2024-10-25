from tkinter import messagebox

from shape_editor import ShapeEditor
from line_shape import LineShape


class LineEditor(ShapeEditor):
    def __init__(self, canvas, shapes):
        super().__init__()
        self.canvas = canvas  # Полотно для малювання
        self.shapes = shapes  # Список для зберігання всіх фігур
        self.shape = None
        self.drawing = False

    def on_mouse_down(self, event):
        if self.shapes.count(None) == 0:
            print("Cannot draw new line: shape array is full.")
            messagebox.showwarning("Warning", "Cannot draw new line: shape array is full.")
            return

        self.shape = LineShape()

        self.shape.start_x = event.x
        self.shape.start_y = event.y
        self.drawing = True

        return self.shape

    def on_mouse_move(self, event):
        if self.drawing:
            self.shape.end_x = event.x
            self.shape.end_y = event.y

            # Очищаємо полотно та малюємо гумовий слід
            self.canvas.delete("temp_line")  # Очищуємо полотно

            # Малюємо гумовий слід (тимчасову лінію)
            self.canvas.create_line(self.shape.start_x, self.shape.start_y,
                                    self.shape.end_x, self.shape.end_y,
                                    fill="red", tags="temp_line")

    def on_mouse_up(self, event):
        if self.drawing:
            self.shape.end_x = event.x
            self.shape.end_y = event.y
            self.drawing = False

            self.shape.draw(self.canvas)

            result_shape = self.shape  # Зберігаємо фігуру для повернення
            self.shape = None  # Очищаємо shape для наступного малювання

            return result_shape  # Повертаємо створену фігуру

    def on_paint(self, canvas):
        if self.drawing:
            self.shape.draw(canvas)
