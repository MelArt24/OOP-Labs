from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0

    @abstractmethod
    def draw(self, canvas, start_x, start_y, end_x, end_y):
        pass


class Line(Shape):
    def draw(self, canvas, start_x, start_y, end_x, end_y):
        start_x = start_x if start_x is not None else self.start_x
        start_y = start_y if start_y is not None else self.start_y
        end_x = end_x if end_x is not None else self.end_x
        end_y = end_y if end_y is not None else self.end_y

        canvas.create_line(start_x, start_y, end_x, end_y, fill="black")

    def __str__(self):
        return f"Line (start_x={self.start_x}, start_y={self.start_y}, end_x={self.end_x}, end_y={self.end_y})"


class Point(Shape):
    def draw(self, canvas, start_x, start_y, end_x=None, end_y=None):
        canvas.create_oval(start_x - 2, start_y - 2, start_x + 2, start_y + 2, fill="black")

    def __str__(self):
        return f"Point at ({self.start_x}, {self.start_y})"


class Ellipse(Shape):
    def draw(self, canvas, start_x, start_y, end_x, end_y, fill_color="yellow"):
        canvas.create_oval(start_x, start_y, end_x, end_y, outline="black", fill=fill_color)

    def __str__(self):
        return (f"EllipseShape (start=({self.start_x}, {self.start_y}), "
                f"end=({self.end_x}, {self.end_y}))")


class Rectangle(Shape):
    center_x = None
    center_y = None

    def draw(self, canvas, start_x, start_y, end_x, end_y):
        self.center_x = (start_x + end_x) / 2
        self.center_y = (start_y + end_y) / 2

        canvas.create_rectangle(start_x, start_y, end_x, end_y, outline="black", fill="")

    def __str__(self):
        radius_x = abs(self.end_x - self.center_x)
        radius_y = abs(self.end_y - self.center_y)
        return (f"RectangleShape (center=({self.center_x}, {self.center_y}), "
                f"radius_x={radius_x}, radius_y={radius_y})")


class Cube(Line, Rectangle):
    center_x = None
    center_y = None

    def __init__(self):
        super().__init__()
        self.top_x = None
        self.top_y = None

    def draw(self, canvas, center_x, center_y, end_x, end_y):
        top_x = center_x - abs(end_x - center_x)
        top_y = center_y - abs(end_y - center_y)
        bottom_x = center_x + abs(end_x - center_x)
        bottom_y = center_y + abs(end_y - center_y)

        Rectangle.draw(self, canvas, top_x, top_y, bottom_x, bottom_y)

        offset = 50

        second_top_x = top_x + offset
        second_top_y = top_y - offset
        second_bottom_x = bottom_x + offset
        second_bottom_y = bottom_y - offset

        Rectangle.draw(self, canvas, second_top_x, second_top_y, second_bottom_x, second_bottom_y)

        Line.draw(self, canvas, top_x, top_y, second_top_x, second_top_y)
        Line.draw(self, canvas, bottom_x, top_y, second_bottom_x, second_top_y)
        Line.draw(self, canvas, top_x, bottom_y, second_top_x, second_bottom_y)
        Line.draw(self, canvas, bottom_x, bottom_y, second_bottom_x, second_bottom_y)


class LineOOShape(Line, Ellipse):
    def draw(self, canvas, start_x=None, start_y=None, end_x=None, end_y=None):
        start_x = start_x if start_x is not None else self.start_x
        start_y = start_y if start_y is not None else self.start_y
        end_x = end_x if end_x is not None else self.end_x
        end_y = end_y if end_y is not None else self.end_y

        Line.draw(self, canvas, start_x, start_y, end_x, end_y)

        radius = 30

        Ellipse.draw(self, canvas,
                     self.start_x - radius, self.start_y - radius,
                     self.start_x + radius, self.start_y + radius,
                     fill_color="")

        Ellipse.draw(self, canvas,
                     self.end_x - radius, self.end_y - radius,
                     self.end_x + radius, self.end_y + radius,
                     fill_color="")

    def __str__(self):
        return f"LineOOShape (start_x={self.start_x}, start_y={self.start_y}, end_x={self.end_x}, end_y={self.end_y})"
