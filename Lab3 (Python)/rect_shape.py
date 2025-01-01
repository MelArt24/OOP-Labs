from shape import Shape


class RectShape(Shape):
    def __init__(self):
        super().__init__()
        self.center_x = None
        self.center_y = None

    def draw(self, canvas):
        # Обчислюємо радіуси від центру
        radius_x = abs(self.end_x - self.center_x)
        radius_y = abs(self.end_y - self.center_y)

        # Малюємо прямокутник через центр і радіуси
        canvas.create_rectangle(
            self.center_x - radius_x,
            self.center_y - radius_y,
            self.center_x + radius_x,
            self.center_y + radius_y,
            outline="black", fill=""
        )

    def __str__(self):
        radius_x = abs(self.end_x - self.center_x)
        radius_y = abs(self.end_y - self.center_y)
        return (f"RectangleShape (center=({self.center_x}, {self.center_y}), "
                f"radius_x={radius_x}, radius_y={radius_y})")
