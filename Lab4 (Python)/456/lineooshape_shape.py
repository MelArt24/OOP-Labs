from line_shape import LineShape
from ellipse_shape import EllipseShape


# class LineOOShape(LineShape, EllipseShape):
#     def draw(self, canvas):
#         canvas.create_line(self.start_x, self.start_y, self.end_x, self.end_y, fill="black")
#
#         radius = 30
#
#         canvas.create_oval(self.start_x - radius, self.start_y - radius,
#                            self.start_x + radius, self.start_y + radius,
#                            fill="", outline="black")
#
#         canvas.create_oval(self.end_x - radius, self.end_y - radius,
#                            self.end_x + radius, self.end_y + radius,
#                            fill="", outline="black")
#
#     def __str__(self):
#         return f"LineOOShape (start=({self.start_x}, {self.start_y}), end=({self.end_x}, {self.end_y}))"

class LineOOShape(LineShape, EllipseShape):
    def draw(self, canvas, start_x=None, start_y=None, end_x=None, end_y=None):
        LineShape.draw(self, canvas, self.start_x, self.start_y, self.end_x, self.end_y)

        radius = 30
        EllipseShape.draw(self, canvas,
                          self.start_x - radius, self.start_y - radius,
                          self.start_x + radius, self.start_y + radius,
                          fill_color="")

        EllipseShape.draw(self, canvas,
                          self.end_x - radius, self.end_y - radius,
                          self.end_x + radius, self.end_y + radius,
                          fill_color="")

    def __str__(self):
        return f"LineOOShape (start=({self.start_x}, {self.start_y}), end=({self.end_x}, {self.end_y}))"
