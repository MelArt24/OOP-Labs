from shape import Shape


class LineShape(Shape):
    def draw(self, canvas):
        canvas.create_line(self.start_x, self.start_y, self.end_x, self.end_y, fill="black")

    def __str__(self):
        return f"LineShape (start_x={self.start_x}, start_y={self.start_y}, end_x={self.end_x}, end_y={self.end_y})"
