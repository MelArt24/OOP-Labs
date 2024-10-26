from shape import Shape


class EllipseShape(Shape):
    def draw(self, canvas, start_x=None, start_y=None, end_x=None, end_y=None, fill_color="yellow"):
        canvas.create_oval(
            start_x, start_y,
            end_x, end_y,
            outline="black", fill=fill_color
        )

    def __str__(self):
        return (f"EllipseShape (start=({self.start_x}, {self.start_y}), "
                f"end=({self.end_x}, {self.end_y}))")
