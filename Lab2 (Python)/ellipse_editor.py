from shape_editor import ShapeEditor
from ellipse_shape import EllipseShape


class EllipseEditor(ShapeEditor):
    def __init__(self, canvas, shapes):
        super().__init__()

        self.canvas = canvas  # Полотно для малювання

        self.shapes = shapes  # Список для зберігання всіх фігур
        self.shape = None
        self.drawing = False

    def on_mouse_down(self, event):
        self.shape = EllipseShape()

        # Встановлюємо центр еліпса
        self.shape.center_x = event.x
        self.shape.center_y = event.y
        self.drawing = True

        return self.shape  # Повертаємо створену фігур

    def on_mouse_move(self, event):
        if self.drawing:
            # Обчислюємо радіуси еліпса
            radius_x = abs(event.x - self.shape.center_x)
            radius_y = abs(event.y - self.shape.center_y)

            # Обчислюємо координати кута охоплюючого прямокутника
            left = self.shape.center_x - radius_x
            top = self.shape.center_y - radius_y
            right = self.shape.center_x + radius_x
            bottom = self.shape.center_y + radius_y

            # Очищаємо полотно та малюємо гумовий слід
            self.canvas.delete("temp_ellipse")  # Очищуємо полотно

            # Малюємо гумовий слід (тимчасовий еліпс)
            self.canvas.create_oval(left, top, right, bottom,
                                    outline="black", tags="temp_ellipse")

    def on_mouse_up(self, event):
        if self.drawing:
            self.shape.end_x = event.x
            self.shape.end_y = event.y
            self.drawing = False

            self.shapes.append(self.shape)  # Додаємо еліпс до списку фігур

            self.shape.draw(self.canvas)

            # Виводимо інформацію про доданий еліпс
#            print(f"Added shape: {self.shape}")

            result_shape = self.shape  # Зберігаємо фігуру для повернення
            self.shape = None  # Очищаємо shape для наступного малювання

            return result_shape  # Повертаємо створену фігуру

    def on_paint(self, canvas):
        if self.drawing:
            self.shape.draw(canvas)
