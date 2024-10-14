from abc import ABC, abstractmethod


class Editor(ABC):
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
    def on_paint(self, canvas):
        pass
