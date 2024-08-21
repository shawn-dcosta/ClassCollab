import threading
from tkinter import *
import customtkinter as ct
from PIL import Image, ImageTk
from login import *


def close():
    load.destroy()


# ct.set_appearance_mode("light")
# ct.set_default_color_theme("dark-blue")

load = Tk()
# screen_width = load.winfo_screenwidth()
# screen_height = load.winfo_screenheight()
# load.geometry(f"{screen_width}x{screen_height}+0+0")
load.geometry("850x550+280+150")
# load.attributes("-maximize", True)
load.config(background="#242455")
load.iconbitmap("Logo.ico")
load.title("")

gif_frame = []

frame_delay = 0


def ready_gif():
    global frame_delay
    gif_file = Image.open('sq_logo_resize.gif')

    for r in range(0, gif_file.n_frames):
        gif_file.seek(r)
        gif_frame.append(gif_file.copy())

    frame_delay = gif_file.info['duration']
    play_gif()


frame_count = -1


def play_gif():
    global frame_count, current_frame

    if frame_count >= len(gif_frame) - 1:
        frame_count = -1
        play_gif()
    else:
        frame_count += 1
        current_frame = ImageTk.PhotoImage(gif_frame[frame_count])
        gif_lb.config(image=current_frame)
        load.after(frame_delay, play_gif)


gif_lb = Label(load,
               pady=50,
               bg="#242455")
gif_lb.place(x=325, y=150)

threading.Thread(target=ready_gif).start()

# Schedule the login function
load.after(7000, login)

# Schedule the window to withdraw after 5 seconds
load.after(7000, load.withdraw)

load.mainloop()
