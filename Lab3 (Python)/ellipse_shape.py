from shape import Shape


class EllipseShape(Shape):
    def __init__(self):
        super().__init__()
        # self.center_y = None
        # self.center_x = None

    def draw(self, canvas):

        canvas.create_oval(
            self.start_x, self.start_y,
            self.end_x, self.end_y,
            outline="black", fill="yellow"  # Без заповнення
        )

    def __str__(self):
        return (f"EllipseShape (start=({self.start_x}, {self.start_y}), "
                f"end=({self.end_x}, {self.end_y}))")
