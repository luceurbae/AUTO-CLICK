from pynput.mouse import Controller, Button
import time
import random

# Flag global untuk kontrol dari GUI
is_playing = False

def play_clicks(load_path="klik_log.txt", min_delay=10, max_delay=20):
    global is_playing
    mouse = Controller()

    try:
        with open(load_path, "r") as f:
            lines = f.readlines()
        clicks = [eval(line.strip()) for line in lines]

        is_playing = True
        while is_playing:
            for delay, x, y, button in clicks:
                if not is_playing:
                    print("🛑 Pemutaran dihentikan.")
                    return
                time.sleep(delay)
                mouse.position = (x, y)
                btn = Button.left if button == "left" else Button.right
                mouse.click(btn)

            pause = random.uniform(min_delay, max_delay)
            print(f"🔁 Satu siklus selesai. Menunggu {pause:.2f} detik...")
            for _ in range(int(pause)):
                if not is_playing:
                    print("🛑 Pemutaran dihentikan saat jeda.")
                    return
                time.sleep(1)

    except Exception as e:
        print("❌ Terjadi error:", e)

def stop_clicks():
    global is_playing
    is_playing = False
