# from pynput import mouse
# from pynput import keyboard


# def on_click(x, y, button, pressed):
#     did_press = "Press" if pressed else "Release"
#     print(f"{did_press}: ({x}, {y})")


# def on_release(key):
#     print("{0} released".format(key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False


# # Collect events until released
# with keyboard.Listener(on_release=on_release) as k_listener, mouse.Listener(
#     on_click=on_click
# ) as m_listener:
#     k_listener.join()
#     m_listener.join()

from pynput import keyboard


def on_press(key):
    try:
        print("alphanumeric key {0} pressed".format(key.char))
    except AttributeError:
        print("special key {0} pressed".format(key))


def on_release(key):
    print("{0} released".format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()