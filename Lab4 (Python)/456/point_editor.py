from tkinter import messagebox

from shape_editor import ShapeEditor
from point_shape import PointShape


class PointEditor(ShapeEditor):
    def __init__(self, canvas, shapes):
        super().__init__(canvas, shapes)
        self.shape = None  # Змінна для поточної фігури

        self.canvas = canvas  # Полотно для малювання
        self.shapes = shapes  # Список для зберігання фігур

    def on_mouse_down(self, event):
        if self.shapes.count(None) == 0:
            print("Cannot draw new point: shape array is full.")
            messagebox.showwarning("Warning", "Cannot draw new point: shape array is full.")
            return

        self.shape = PointShape()
        self.shape.start_x = event.x
        self.shape.start_y = event.y
        self.shape.draw(event.widget)

        return self.shape

    def on_mouse_up(self, event):
        if self.shape:
            result_shape = self.shape
            self.shape = None

            return result_shape

    def on_mouse_move(self, event):
        pass

    def on_paint(self, canvas):
        pass
