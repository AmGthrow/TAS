"""Class objects symboling MouseEvents (Click, Scroll, Move) and KeyboardEvents
(Press, Release).

All the Event objects have two methods: 
 - __init__() which is called whenever the event happens 
    (Creating a Press(Key.ctrl_l) event logs "Pressing Key.ctrl_l")
 - execute() which simulates executing the event again
    (calling Press(Key.ctrl_l).execute() automatically presses left control
    and logs "Pressed Key.ctrl_l")

__init__() is intended to be called when the user performs an event and 
execute() is intended to be called when the computer intends to re-perform it
    """

from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
import logging

# Log all events (both creation and execution) into the terminal
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s')

keyboard = KeyboardController()
mouse = MouseController()


class Event:
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

        class Tap:
            def __init__(self, key):
                self.key = key
                logging.info(f"Tapping {self.key}")

            def execute(self):
                logging.info(f"Tapped {self.key}")
                keyboard.tap(self.key)

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
                if self.dy > 0:
                    direction += "Up"
                elif self.dy < 0:
                    direction += "Down"

                if self.dx > 0:
                    direction += "Right"
                elif self.dx < 0:
                    direction += "Left"
                logging.info(
                    f"Scrolled {self.direction}: ({self.x}, {self.y})")
