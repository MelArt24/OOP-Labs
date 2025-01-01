from shape import Shape


class LineShape(Shape):
    def draw(self, canvas, start_x, start_y, end_x, end_y):
        start_x = start_x if start_x is not None else self.start_x
        start_y = start_y if start_y is not None else self.start_y
        end_x = end_x if end_x is not None else self.end_x
        end_y = end_y if end_y is not None else self.end_y

        canvas.create_line(start_x, start_y, end_x, end_y, fill="black")

    def __str__(self):
        return f"LineShape (start_x={self.start_x}, start_y={self.start_y}, end_x={self.end_x}, end_y={self.end_y})"
