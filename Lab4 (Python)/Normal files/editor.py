from abc import ABC, abstractmethod


class Editor(ABC):
    def __init__(self, canvas, shapes):
        self.canvas = canvas
        self.shapes = shapes

    @abstractmethod
    def on_mouse_down(self, event):
        pass

    @abstractmethod
    def on_mouse_up(self, event):
        pass

    @abstractmethod
    def on_mouse_move(self, event):
        pass

    @abstractmethod
    def clear_canvas(self):
        pass
