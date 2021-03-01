from abc import ABC, abstractclassmethod
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController


class Event(ABC):
    @abstractclassmethod
    def execute(self):
        pass


class KeyboardEvent(Event):
    keyboard = KeyboardController()

    class Press:
        def __init__(self, key):
            self.key = key

        def execute(self):
            keyboard.press(key)

    class Release:
        def __init__(self, key):
            self.key = key

        def execute(self):
            keyboard.release(key)
