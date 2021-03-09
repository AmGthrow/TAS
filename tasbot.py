"""Contains the script which performs recording and playback
of macros.

Press <TOGGLE_RECORDING_HOTKEY> to start/stop recording
Press <START_PLAYBACK_HOTKEY> to replay the recording
"""

from pynput import mouse
from pynput import keyboard
import threading
from EventRecorder import EventRecorder
from Events import Event
import winsound

TOGGLE_RECORDING_HOTKEY = '<ctrl>+<shift>+<f1>'
START_PLAYBACK_HOTKEY = '<ctrl>+<shift>+<f2>'


class TASbot:
    def __init__(self):
        self.recording = False
        self.events = EventRecorder()

    def start_recording(self):
        """Clears whatever's been previously recorded and starts
        recording from scratch using new Keyboard and Mouse listeners
        """
        self.events.clear_events()

        self.recording = True

        self.k_listener = keyboard.Listener(
            on_release=self.on_release, on_press=self.on_press)
        self.m_listener = mouse.Listener(
            on_click=self.on_click, on_scroll=self.on_scroll)

        self.k_listener.start()
        self.m_listener.start()

    def stop_recording(self):
        """Stops the Keyboard and Mouse listeners and ends
        the current recording
        """
        self.recording = False
        self.k_listener.stop()
        self.m_listener.stop()

        # PROBLEM: say toggle_recording_hotkey is ctrl+shift+F1
        # When I stop recording, I need to press ctrl+shift+F1 but
        # The keyboard listener actually records that.
        # So when I play the recording back, it presses ctrl+shift+F1
        # At the end and inadvertently starts a new recording.
        # I solve this by popping the last event since its guaranteed
        # to be a part of the hotkey anyway, since the hotkey
        # immediately stops recording after that last button
        self.events.events.pop()

    def toggle_recording(self):
        """Calls start_recording() with a high-pitched beep if 
        we're currently not recording OR calls stop_recording
        with a low-pitched beep if we're currently recording.
        """
        if self.recording:
            winsound.Beep(200, 100)
            self.stop_recording()
        else:
            winsound.Beep(600, 300)
            self.start_recording()

    def play_recording(self):
        """Creates a Thread which controls
        the Mouse & Keyboard to execute the recorded events
        """
        self.replay = threading.Thread(target=self.events.execute)
        self.replay.start()

    def toggle_playback(self):
        self.events.playing = not self.events.playing
        if self.events.playing:
            self.play_recording()

    def on_click(self, x, y, button, pressed):
        event = Event.MouseEvent.Click(x, y, button, pressed)
        self.events.add_event(event)

    def on_scroll(self, x, y, dx, dy):
        event = Event.MouseEvent.Scroll(x, y, dx, dy)
        self.events.add_event(event)

    def on_press(self, key):
        event = Event.KeyboardEvent.Press(key)
        self.events.add_event(event)

    def on_release(self, key):
        event = Event.KeyboardEvent.Release(key)
        self.events.add_event(event)


recorder = TASbot()


# Start/stop recording when pressing the hotkey ctrl + shift + F1
# Play recording when pressing the hotkey ctrl + shift + F2
# Immediately panic and shut everything down when pressing ctrl + shift + esc
with keyboard.GlobalHotKeys({
        TOGGLE_RECORDING_HOTKEY: recorder.toggle_recording,
        START_PLAYBACK_HOTKEY: recorder.toggle_playback,
        '<ctrl>+<shift>+<esc>': exit}) as h:
    h.join()
