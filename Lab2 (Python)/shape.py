from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0

    @abstractmethod
    def draw(self, canvas):
        pass
