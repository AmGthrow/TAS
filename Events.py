from abc import ABC, abstractclassmethod
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController


class Event(ABC):
    @abstractclassmethod
    def execute(self):
        pass
