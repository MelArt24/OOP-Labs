from tkinter import messagebox

from shape_editor import ShapeEditor
from rect_shape import RectShape


class RectEditor(ShapeEditor):
    def __init__(self, canvas, shapes):
        super().__init__()

        self.canvas = canvas  # Полотно для малювання
        self.shapes = shapes  # Список для зберігання всіх фігур

        self.shape = None
        self.drawing = False

    def on_mouse_down(self, event):
        if self.shapes.count(None) == 0:
            print("Cannot draw new rectangle: shape array is full.")
            messagebox.showwarning("Warning", "Cannot draw new rectangle: shape array is full.")
            return

        self.shape = RectShape()

        self.shape.center_x = event.x
        self.shape.center_y = event.y

        self.drawing = True

        return self.shape

    def on_mouse_move(self, event):
        if self.drawing:
            # Обчислюємо відстані від центру до поточного положення миші
            radius_x = abs(event.x - self.shape.center_x)
            radius_y = abs(event.y - self.shape.center_y)

            # Обчислюємо координати кута охоплюючого прямокутника
            left = self.shape.center_x - radius_x
            top = self.shape.center_y - radius_y
            right = self.shape.center_x + radius_x
            bottom = self.shape.center_y + radius_y

            # Очищаємо гумовий слід
            self.canvas.delete("temp_rectangle")

            # Малюємо гумовий слід (тимчасовий прямокутник)
            self.canvas.create_rectangle(left, top, right, bottom,
                                         outline="red", tags="temp_rectangle")

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
