from shape_editor import ShapeEditor
from line_shape import LineShape


class LineEditor(ShapeEditor):
    def __init__(self, canvas, shapes):
        super().__init__()
        self.canvas = canvas  # Полотно для малювання
        self.shapes = shapes  # Список для зберігання всіх фігур
        self.shape = None
        self.drawing = False

    def on_mouse_down(self, event):
        self.shape = LineShape()

        self.shape.start_x = event.x
        self.shape.start_y = event.y
        self.drawing = True

        return self.shape

    def on_mouse_move(self, event):
        if self.drawing:
            self.shape.end_x = event.x
            self.shape.end_y = event.y

            # Очищаємо полотно та малюємо гумовий слід
            self.canvas.delete("temp_line")  # Очищуємо полотно

            # Малюємо гумовий слід (тимчасову лінію)
            self.canvas.create_line(self.shape.start_x, self.shape.start_y,
                                    self.shape.end_x, self.shape.end_y,
                                    fill="black", tags="temp_line")

    def on_mouse_up(self, event):
        if self.drawing:
            self.shape.end_x = event.x
            self.shape.end_y = event.y
            self.drawing = False

            self.shapes.append(self.shape)  # Додаємо лінію до списку фігур

            self.shape.draw(self.canvas)

#            print(f"Added shape: {self.shape}")

            result_shape = self.shape  # Зберігаємо фігуру для повернення
            self.shape = None  # Очищаємо shape для наступного малювання

            return result_shape  # Повертаємо створену фігуру

    def on_paint(self, canvas):
        if self.drawing:
            self.shape.draw(canvas)
