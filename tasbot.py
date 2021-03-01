from pynput import mouse
from pynput import keyboard


class TASbot:
    def __init__(self):
        self.recording = False

    # Collect events until released
    # Release by pressing esc, see on_release()
    def start_recording(self):
        self.recording = True
        with keyboard.Listener(on_release=on_release, on_press=on_press) as self.k_listener,\
                mouse.Listener(on_click=on_click, on_scroll=on_scroll) as self.m_listener:
            self.k_listener.join()
            self.m_listener.join()

    def stop_recording(self):
        self.recording = False
        self.k_listener.stop()
        self.m_listener.stop()

    def toggle_recording(self):
        if self.recording:
            self.stop_recording()
        else:
            self.start_recording()


def on_click(x, y, button, pressed):
    did_press = "Press" if pressed else "Release"
    print(f"{did_press}: ({x}, {y})")


def on_scroll(x, y, dx, dy):
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


def on_press(key):
    print(f"{key} pressed")


def on_release(key):
    print(f"{key} released")
    if key == keyboard.Key.esc:
        # Stop mouse listener
        m_listener.stop()
        # Stop keyboard listener
        return False


# Collect events until released
# Release by pressing esc, see on_release()
with keyboard.Listener(on_release=on_release, on_press=on_press) as k_listener,\
        mouse.Listener(on_click=on_click, on_scroll=on_scroll) as m_listener:
    k_listener.join()
    m_listener.join()

# from pynput import keyboard
# from pynput import mouse


# def on_press(key):
#     try:
#         print(f"alphanumeric key {key.char} pressed")
#     except AttributeError:
#         print(f"special key {key} pressed")


# def on_release(key):
#     print(f"{key} released")
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False


# with keyboard.Events() as kb_events, mouse.Events() as ms_events:
#     print("started recording")
#     for kb_event in kb_events:
#         if kb_event.key == keyboard.Key.esc:
#             break
#         else:
#             print(f"Received event {kb_event}")
#     for ms_event in ms_events:
#         print(f"Received event {ms_event}")
