from shape import Shape


class EllipseShape(Shape):
    def __init__(self):
        super().__init__()
        self.center_y = None
        self.center_x = None

    def draw(self, canvas):

        radius_x = abs(self.end_x - self.center_x)
        radius_y = abs(self.end_y - self.center_y)

        # Малюємо еліпс без заповнення
        canvas.create_oval(
            self.center_x - radius_x,
            self.center_y - radius_y,
            self.center_x + radius_x,
            self.center_y + radius_y,
            outline="black", fill=""  # Без заповнення
        )

    def __str__(self):
        radius_x = abs(self.end_x - self.center_x)
        radius_y = abs(self.end_y - self.center_y)
        return f"EllipseShape (center=({self.center_x}, {self.center_y}), radius_x={radius_x}, radius_y={radius_y})"
