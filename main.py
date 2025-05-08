import tkinter as tk
from recorder import record_clicks
from player import play_clicks, stop_clicks
import threading

def start_recording():
    threading.Thread(target=record_clicks).start()

def start_playing():
    threading.Thread(target=play_clicks).start()

def stop_playing():
    stop_clicks()

root = tk.Tk()
root.title("Auto Clicker GUI")

tk.Label(root, text="Auto Clicker by Zaluce", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Rekam Klik", width=25, command=start_recording).pack(pady=5)
tk.Button(root, text="Mainkan Klik (Loop)", width=25, command=start_playing).pack(pady=5)
tk.Button(root, text="Hentikan Pemutaran", width=25, command=stop_playing, fg="red").pack(pady=5)

tk.Label(root, text="Klik kanan untuk hentikan perekaman.\nKlik 'Hentikan Pemutaran' untuk stop loop.", font=("Arial", 9)).pack(pady=10)

root.mainloop()
