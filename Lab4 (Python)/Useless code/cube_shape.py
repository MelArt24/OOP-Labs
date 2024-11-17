from line_shape import LineShape
from rect_shape import RectShape


# class CubeShape(LineShape, RectShape):
#     def draw(self, canvas):
#         # Обчислюємо координати основи куба
#         left = self.center_x - abs(self.end_x - self.center_x)  # Ліва сторона
#         top = self.center_y - abs(self.end_y - self.center_y)  # Верхня сторона
#         right = self.center_x + abs(self.end_x - self.center_x)  # Права сторона
#         bottom = self.center_y + abs(self.end_y - self.center_y)  # Нижня сторона
#
#         # Малюємо основний прямокутник (основа куба)
#         canvas.create_rectangle(left, top, right, bottom, outline="black")
#
#         # Обчислюємо координати верхнього прямокутника
#         top_left = (left - 50, top - 50)
#         top_right = (right - 50, top - 50)
#
#         # Малюємо верхній прямокутник
#         canvas.create_rectangle(top_left[0], top_left[1], top_right[0], top_left[1] + (bottom - top), outline="black")
#
#         # З'єднуємо вершини
#         canvas.create_line(left, top, top_left[0], top_left[1], fill="black")
#         canvas.create_line(right, top, top_right[0], top_right[1], fill="black")
#         canvas.create_line(left, bottom, left - 50, bottom - 50, fill="black")
#         canvas.create_line(right, bottom, right - 50, bottom - 50, fill="black")
#
#     def __str__(self):
#         return f"CubeShape (center=({self.center_x}, {self.center_y}), end=({self.end_x}, {self.end_y}))"

class CubeShape(LineShape, RectShape):
    def draw(self, canvas, center_x=None, center_y=None, end_x=None, end_y=None):
        self.center_x = center_x
        self.center_y = center_y
        self.end_x = end_x
        self.end_y = end_y

        left = self.center_x - abs(self.end_x - self.center_x)
        top = self.center_y - abs(self.end_y - self.center_y)
        right = self.center_x + abs(self.end_x - self.center_x)
        bottom = self.center_y + abs(self.end_y - self.center_y)

        RectShape.draw(self, canvas, left, top, right, bottom)

        offset = 50
        second_left = left - offset
        second_top = top - offset
        second_right = right - offset
        second_bottom = bottom - offset

        # Малюємо другий прямокутник
        RectShape.draw(self, canvas, second_left, second_top, second_right, second_bottom)

        # Малюємо лінії, що з'єднують вершини
        LineShape.draw(self, canvas, left, top, second_left, second_top)  # Зверху зліва
        LineShape.draw(self, canvas, right, top, second_right, second_top)  # Зверху справа
        LineShape.draw(self, canvas, left, bottom, second_left, second_bottom)  # Знизу зліва
        LineShape.draw(self, canvas, right, bottom, second_right, second_bottom)  # Знизу справа

        # # Малюємо другий прямокутник
        # RectShape.draw(self, canvas, second_left, second_top, second_right, second_bottom)

    # def __str__(self):
    #     return f"CubeShape (center=({self.center_x}, {self.center_y}), end=({self.end_x}, {self.end_y}))"

    def __str__(self):
        left = self.center_x - abs(self.end_x - self.center_x)
        top = self.center_y - abs(self.end_y - self.center_y)
        right = self.center_x + abs(self.end_x - self.center_x)
        bottom = self.center_y + abs(self.end_y - self.center_y)
        return (f"CubeShape (center=({self.center_x}, {self.center_y}), end=({self.end_x}, {self.end_y}), "
                f"left = {left}), top = {top}), right = {right}), bottom = {bottom})")
