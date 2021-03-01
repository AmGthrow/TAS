from pynput import mouse
from pynput import keyboard
import threading
from EventRecorder import EventRecorder
import Events
import winsound

TOGGLE_RECORDING_HOTKEY = '<ctrl>+<shift>+<f1>'
START_PLAYBACK_HOTKEY = '<ctrl>+<shift>+<f2>'


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
            winsound.Beep(200, 100)
            self.stop_recording()
        else:
            winsound.Beep(600, 300)
            self.start_recording()

    def play_recording(self):
        # ! For some insane reason, calling play_recording() directly
        # ! In the hotkey will make it look infinitely. Somehow, containing
        # ! play_recording() in a thread solves that. So that's why
        # ! I have toggle_playing() but god why does it loop???
        for event in self.events:
            event.execute()

        # Release all held keyboard keys (usually dangling "Press" keys)
        for key in keyboard.HotKey.parse(START_PLAYBACK_HOTKEY):
            Events.KeyboardEvent.Release(key).execute()

    def toggle_playing(self):
        self.replay = threading.Thread(target=self.play_recording)
        self.replay.start()

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
        TOGGLE_RECORDING_HOTKEY: recorder.toggle_recording,
        START_PLAYBACK_HOTKEY: recorder.toggle_playing,
        '<ctrl>+<shift>+<esc>': exit}) as h:
    h.join()
