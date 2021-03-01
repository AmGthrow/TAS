from pynput import mouse
from pynput import keyboard
from EventRecorder import EventRecorder
import Events


class TASbot:
    def __init__(self):
        self.recording = False
        self.events = EventRecorder()

    def start_recording(self):
        # Remove all recorded events and start from scratch
        self.events.clear_events()

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

    # ! MAJOR BUG: FOR SOME REASON, THIS LOOPS INDEFINITELY WHEN 
    # ! YOU HIT CTRL SHIFT F12
    def play_recording(self):
        for event in self.events:
            event.execute()

    def on_click(self, x, y, button, pressed):
        event = Events.MouseEvent.Click(x, y, button, pressed)
        self.events.add_event(event)

    def on_scroll(self, x, y, dx, dy):
        event = Events.MouseEvent.Scroll(x, y, dx, dy)
        self.events.add_event(event)

    def on_press(self, key):
        event = Events.KeyboardEvent.Press(key)
        self.events.add_event(event)

    def on_release(self, key):
        event = Events.KeyboardEvent.Release(key)
        self.events.add_event(event)


recorder = TASbot()


# Start/stop recording when pressing the hotkey ctrl + shift + F1
# Play recording when pressing the hotkey ctrl + shift + F
with keyboard.GlobalHotKeys({
        '<ctrl>+<shift>+<f1>': recorder.toggle_recording,
        '<ctrl>+<shift>+<f2>': recorder.play_recording}) as h:
    h.join()
