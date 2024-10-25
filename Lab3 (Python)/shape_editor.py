from abc import ABC
from editor import Editor


class ShapeEditor(Editor, ABC):
    def __init__(self):
        super().__init__()

    def on_mouse_down(self, event):
        pass

    def on_mouse_up(self, event):
        pass

    def on_mouse_move(self, event):
        pass

    def on_paint(self, canvas):
        pass

    def clear_canvas(self):
        pass
