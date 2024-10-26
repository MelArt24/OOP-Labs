from shape import Shape


class RectShape(Shape):
    def __init__(self):
        super().__init__()
        self.center_x = None
        self.center_y = None

    def draw(self, canvas, start_x, start_y, end_x, end_y):
        self.center_x = (start_x + end_x) / 2
        self.center_y = (start_y + end_y) / 2

        left = start_x
        top = start_y
        right = end_x
        bottom = end_y

        canvas.create_rectangle(left, top, right, bottom, outline="black", fill="")

    def __str__(self):
        radius_x = abs(self.end_x - self.center_x)
        radius_y = abs(self.end_y - self.center_y)
        return (f"RectangleShape (center=({self.center_x}, {self.center_y}), "
                f"radius_x={radius_x}, radius_y={radius_y})")
