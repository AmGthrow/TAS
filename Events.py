from abc import ABC, abstractclassmethod
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()


class KeyboardEvent:
    class Press:
        def __init__(self, key):
            self.key = key

        def execute(self):
            keyboard.press(self.key)

    class Release:
        def __init__(self, key):
            self.key = key

        def execute(self):
            keyboard.release(self.key)


class MouseEvent:
    class Move:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def execute(self):
            mouse.position = (self.x, self.y)
