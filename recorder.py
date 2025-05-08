from pynput import mouse
import time

clicks = []

def record_clicks(save_path="click_log.txt"):
    print("Recording... (right click to stop recording)")

    def on_click(x, y, button, pressed):
        nonlocal last_time
        if pressed:
            current_time = time.time()
            delay = current_time - last_time
            last_time = current_time
            clicks.append((delay, x, y, button.name))
            print(f"Klik {button.name} di ({x}, {y}) setelah {delay:.2f} detik")
        if not pressed and button.name == "right":
            return False

    last_time = time.time()
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    with open(save_path, "w") as f:
        for click in clicks:
            f.write(f"{click}\n")
    print(f"Recording completed. Saved in {save_path}")
