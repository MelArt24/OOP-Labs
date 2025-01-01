from tkinter import messagebox

from line_editor import LineEditor
from rect_editor import RectEditor
from cube_shape import CubeShape


class CubeEditor(LineEditor, RectEditor):
    def __init__(self, canvas, shapes):
        LineEditor.__init__(self, canvas, shapes)
        RectEditor.__init__(self, canvas, shapes)
        self.canvas = canvas
        self.shapes = shapes
        self.shape = None
        self.drawing = False

    def on_mouse_down(self, event):
        if self.shapes.count(None) == 0:
            print("Cannot draw new cube: shape array is full.")
            messagebox.showwarning("Warning", "Cannot draw new cube: shape array is full.")
            return

        self.shape = CubeShape()

        self.shape.center_x = event.x
        self.shape.center_y = event.y

        self.drawing = True

        return self.shape

    def on_mouse_move(self, event):
        if self.drawing:
            radius_x = abs(event.x - self.shape.center_x)
            radius_y = abs(event.y - self.shape.center_y)

            left = self.shape.center_x - radius_x
            top = self.shape.center_y - radius_y
            right = self.shape.center_x + radius_x
            bottom = self.shape.center_y + radius_y

            self.canvas.delete("temp_cube")

            self.canvas.create_rectangle(left, top, right, bottom, outline="red", dash=(2, 2), tags="temp_cube")

            top_left = (left - 50, top - 50)
            top_right = (right - 50, top - 50)

            self.canvas.create_rectangle(top_left[0], top_left[1], top_right[0], top_left[1] + (bottom - top),
                                         outline="red", dash=(2, 2), tags="temp_cube")

            self.canvas.create_line(left, top, top_left[0], top_left[1], fill="red", dash=(2, 2), tags="temp_cube")
            self.canvas.create_line(right, top, top_right[0], top_right[1], fill="red", dash=(2, 2), tags="temp_cube")
            self.canvas.create_line(left, bottom, left - 50, bottom - 50, fill="red", dash=(2, 2), tags="temp_cube")
            self.canvas.create_line(right, bottom, right - 50, bottom - 50, fill="red", dash=(2, 2), tags="temp_cube")

    def on_mouse_up(self, event):
        if self.drawing:
            self.shape.end_x = event.x
            self.shape.end_y = event.y
            self.drawing = False

            self.shape.draw(self.canvas, self.shape.center_x, self.shape.center_y, self.shape.end_x, self.shape.end_y)

            result_shape = self.shape
            self.shape = None

            return result_shape

    def on_paint(self, canvas):
        if self.drawing:
            self.shape.draw(canvas, self.shape.center_x, self.shape.center_y, self.shape.end_x, self.shape.end_y)
