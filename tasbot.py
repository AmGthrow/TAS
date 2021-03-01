from pynput import mouse
from pynput import keyboard
from EventRecorder import EventRecorder


class TASbot:
    def __init__(self):
        self.recording = False
        self.events = EventRecorder()

    def start_recording(self):
        self.recording = True

        self.k_listener = keyboard.Listener(
            on_release=self.on_release, on_press=self.on_press)
        self.m_listener = mouse.Listener(
            on_click=self.on_click, on_scroll=self.on_scroll)

        self.k_listener.start()
        self.m_listener.start()

    def stop_recording(self):
        self.recording = False
        self.k_listener.stop()
        self.m_listener.stop()

    def toggle_recording(self):
        if self.recording:
            self.stop_recording()
        else:
            self.start_recording()

    def play_recording(self):
        for event in self.events:
            print(event)

    def on_click(self, x, y, button, pressed):
        did_press = "Press" if pressed else "Release"
        print(f"{did_press}: ({x}, {y})")

    def on_scroll(self, x, y, dx, dy):
        direction = ""
        if dy > 0:
            direction += "Up"
        elif dy < 0:
            direction += "Down"

        if dx > 0:
            direction += "Right"
        elif dx < 0:
            direction += "Left"
        print(f"{direction}: ({x}, {y})")

    def on_press(self, key):
        print(f"{key} pressed")

    def on_release(self, key):
        print(f"{key} released")


recorder = TASbot()


# Start/stop recording when pressing the hotkey ctrl + shift + F1
with keyboard.GlobalHotKeys({
        '<ctrl>+<shift>+<f1>': recorder.toggle_recording}) as h:
    h.join()
