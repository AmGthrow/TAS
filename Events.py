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


class MouseEvent(Event):
    mouse = MouseController()
