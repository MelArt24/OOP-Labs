from shape import Shape


class RectShape(Shape):
    def draw(self, canvas):
        canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y, fill="yellow", outline="black")

    def __str__(self):
        return (f"RectangleShape (start_x={self.start_x}, start_y={self.start_y}, "
                f"end_x={self.end_x}, end_y={self.end_y})")
