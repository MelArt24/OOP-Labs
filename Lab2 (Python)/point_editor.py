from shape_editor import ShapeEditor
from point_shape import PointShape


class PointEditor(ShapeEditor):
    def __init__(self, canvas, shapes):
        super().__init__()
        self.shape = None  # Змінна для поточної фігури

        self.canvas = canvas  # Полотно для малювання
        self.shapes = shapes  # Список для зберігання фігур

    def on_mouse_down(self, event):

        self.shape = PointShape()
        self.shape.start_x = event.x
        self.shape.start_y = event.y
        self.shape.draw(event.widget)

        return self.shape

    def on_mouse_up(self, event):
        if self.shape:
            # Додаємо точку до списку фігур
            self.shapes.append(self.shape)
            # Виводимо фігуру для перевірки
#            print(f"Added shape: {self.shape}")

            result_shape = self.shape
            self.shape = None

            return result_shape

    def on_mouse_move(self, event):
        pass

    def on_paint(self, canvas):
        pass
