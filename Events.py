from abc import ABC, abstractclassmethod
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s')

keyboard = KeyboardController()
mouse = MouseController()


class KeyboardEvent:
    class Press:
        def __init__(self, key):
            self.key = key
            logging.info(f"Pressing {self.key}")

        def execute(self):
            logging.info(f"Pressed {self.key}")
            keyboard.press(self.key)

    class Release:
        def __init__(self, key):
            self.key = key
            logging.info(f"Releasing {self.key}")

        def execute(self):
            logging.info(f"Released {self.key}")
            keyboard.release(self.key)


class MouseEvent:
    class Move:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            logging.info(f"Moving to ({self.x}, {self.y})")

        def execute(self):
            logging.info(f"Moved to ({self.x}, {self.y})")
            mouse.position = (self.x, self.y)

    class Click:
        def __init__(self, x, y, button, pressed):
            self.x = x
            self.y = y
            self.button = button
            self.pressed = pressed
            logging.info(f"Moving to ({self.x}, {self.y})")
            did_press = "Pressing" if self.pressed else "Releasing"
            logging.info(f"{did_press} {self.button}")

        def execute(self):
            mouse.position = (self.x, self.y)
            if self.pressed:
                mouse.press(self.button)
            else:
                mouse.release(self.button)
            logging.info(f"Moved to ({self.x}, {self.y})")
            did_press = "Pressed" if self.pressed else "Released"
            logging.info(f"{did_press} {self.button}")

    class Scroll:
        def __init__(self, x, y, dx, dy):
            self.x = x
            self.y = y
            self.dx = dx
            self.dy = dy
            logging.info(f"Moving to ({self.x}, {self.y})")
            direction = ""
            if dy > 0:
                direction += "Up"
            elif dy < 0:
                direction += "Down"

            if dx > 0:
                direction += "Right"
            elif dx < 0:
                direction += "Left"
            logging.info(f"Scrolling {direction}: ({self.x}, {self.y})")

        def execute(self):
            mouse.position = (self.x, self.y)
            mouse.scroll(self.dx, self.dy)
            logging.info(f"Moved to ({self.x}, {self.y})")
            direction = ""
            if dy > 0:
                direction += "Up"
            elif dy < 0:
                direction += "Down"

            if dx > 0:
                direction += "Right"
            elif dx < 0:
                direction += "Left"
            logging.info(f"Scrolled {direction}: ({x}, {y})")
