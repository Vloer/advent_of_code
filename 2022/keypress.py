from pynput import keyboard

count = 0
keys_pressed = []
with keyboard.Events() as k:
    for e in k:
        if e.key == keyboard.Key.scroll_lock:
            print(count)
            print(keys_pressed)
            break
        if isinstance(e, keyboard.Events.Press):
            count += 1
            keys_pressed.append(e.key)






