from tkinter import messagebox

from ellipse_editor import EllipseEditor
from line_editor import LineEditor
from lineooshape_shape import LineOOShape


class LineOOShapeEditor(LineEditor, EllipseEditor):
    def __init__(self, canvas, shapes):
        LineEditor.__init__(self, canvas, shapes)
        EllipseEditor.__init__(self, canvas, shapes)
        self.canvas = canvas
        self.shapes = shapes
        self.shape = None
        self.drawing = False

    def on_mouse_down(self, event):
        if self.shapes.count(None) == 0:
            print("Cannot draw new lineooshape: shape array is full.")
            messagebox.showwarning("Warning", "Cannot draw new lineooshape: shape array is full.")
            return

        self.shape = LineOOShape()

        self.shape.start_x = event.x
        self.shape.start_y = event.y

        self.drawing = True

        return self.shape

    def on_mouse_move(self, event):
        if self.drawing:
            self.canvas.delete("temp_line")

            self.shape.end_x = event.x
            self.shape.end_y = event.y

            self.canvas.create_line(self.shape.start_x, self.shape.start_y,
                                    self.shape.end_x, self.shape.end_y,
                                    fill="red", dash=(2, 2), tags="temp_line")

            radius = 30
            self.canvas.create_oval(self.shape.start_x - radius, self.shape.start_y - radius,
                                    self.shape.start_x + radius, self.shape.start_y + radius,
                                    fill="", outline="red", dash=(2, 2), tags="temp_line")

            self.canvas.create_oval(self.shape.end_x - radius, self.shape.end_y - radius,
                                    self.shape.end_x + radius, self.shape.end_y + radius,
                                    fill="", outline="red", dash=(2, 2), tags="temp_line")

    def on_mouse_up(self, event):
        if self.drawing:
            self.shape.end_x = event.x
            self.shape.end_y = event.y
            self.drawing = False

            self.shape.draw(self.canvas)

            result_shape = self.shape
            self.shape = None

            return result_shape

    def on_paint(self, canvas):
        if self.drawing:
            self.shape.draw(canvas)
