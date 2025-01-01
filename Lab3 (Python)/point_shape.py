from shape import Shape


class PointShape(Shape):
    def draw(self, canvas):
        canvas.create_oval(self.start_x - 2, self.start_y - 2, self.start_x + 2, self.start_y + 2, fill="black")

    def __str__(self):
        return f"PointShape at ({self.start_x}, {self.start_y})"
