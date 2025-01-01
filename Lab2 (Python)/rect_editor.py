from shape_editor import ShapeEditor
from rect_shape import RectShape


class RectEditor(ShapeEditor):
    def __init__(self, canvas, shapes):
        super().__init__()

        self.canvas = canvas  # Полотно для малювання
        self.shapes = shapes  # Список для зберігання всіх фігур

        self.shape = None
        self.drawing = False

    def on_mouse_down(self, event):
        self.shape = RectShape()

        self.shape.start_x = event.x
        self.shape.start_y = event.y
        self.drawing = True

        return self.shape

    def on_mouse_move(self, event):
        if self.drawing:
            self.shape.end_x = event.x
            self.shape.end_y = event.y

            # Очищаємо гумовий слід
            self.canvas.delete("temp_rectangle")

            # Обчислюємо координати кута охоплюючого прямокутника
            left = min(self.shape.start_x, self.shape.end_x)
            top = min(self.shape.start_y, self.shape.end_y)
            right = max(self.shape.start_x, self.shape.end_x)
            bottom = max(self.shape.start_y, self.shape.end_y)

            # Малюємо гумовий слід (тимчасовий прямокутник)
            self.canvas.create_rectangle(left, top, right, bottom,
                                         outline="black", tags="temp_rectangle")

    def on_mouse_up(self, event):
        if self.drawing:
            self.shape.end_x = event.x
            self.shape.end_y = event.y
            self.drawing = False

            # Додаємо прямокутник до списку фігур
            self.shapes.append(self.shape)
            self.shape.draw(self.canvas)

            # Виводимо інформацію про доданий еліпс
#            print(f"Added shape: {self.shape}")

            result_shape = self.shape  # Зберігаємо фігуру для повернення
            self.shape = None  # Очищаємо shape для наступного малювання

            return result_shape  # Повертаємо створену фігуру

    def on_paint(self, canvas):
        if self.drawing:
            self.shape.draw(canvas)
