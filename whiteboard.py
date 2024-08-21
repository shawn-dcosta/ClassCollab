from tkinter import *
import time
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageDraw
from tkinter import filedialog
import os

from PIL import ImageGrab


def white_brd():
    root = Toplevel()
    root.title('WHITE BOARD')
    root.geometry("1050x570+150+50")
    root.config(bg="#f2f3f5")
    root.resizable(False, False)

    cur_x = 0
    cur_y = 0
    # color = "black"

    def locate_xy(work):
        global cur_x, cur_y
        cur_x = work.x
        cur_y = work.y

    def addline(work):
        global cur_x, cur_y
        canvas.create_line((cur_x, cur_y, work.x, work.y), width=get_cur_value(), fill=color, capstyle=ROUND,
                           smooth=True)
        cur_y, cur_x = work.y, work.x

    def show_color(new_color):
        global color

        color = new_color

    def new_canvas():
        canvas.delete("all")
        display_pallete()

    def insertimage():
        global filename
        global f_img

        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                              filetype=(("PNG file", "*.png"), ("All file", "new.txt")))

        f_img = tk.PhotoImage(file=filename)
        my_img = canvas.create_image(180, 50, image=f_img, anchor="nw")
        canvas.bind("<B3-Motion>", my_callback)

    def my_callback(event):
        global f_img

        f_img = tk.PhotoImage(file=filename)
        my_img = canvas.create_image(event.x, event.y, image=f_img)

    def save_canvas():
        # Calculate coordinates relative to the canvas
        x = root.winfo_rootx() + canvas.winfo_rootx()
        y = root.winfo_rooty() + canvas.winfo_rooty()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()

        # Grab the image using the calculated coordinates
        image = ImageGrab.grab((x - 160, y - 85, x1 - 160, y1 - 85))
        timestamp = int(time.time())  # current timestamp
        fe = f"drawing_{timestamp}.png"

        # Save the image to a file in the specified folder
        image.save(
            f"C:\\Users\\Shawn Dcosta\\Desktop\\Shawn\\Sem - 4\\Python MPR Final\\ClassCollab\\Whiteboard Contents\\{fe}")
        print("Drawing saved successfully.")

        # x = root.winfo_rootx() + canvas.winfo_x()
        # y = root.winfo_rooty() + canvas.winfo_y()
        # x1 = x + canvas.winfo_width()
        # y1 = y + canvas.winfo_height()
        # image = ImageGrab.grab((x, y, x1, y1))
        # timestamp = int(time.time())  # current timestamp
        # fe = f"drawing_{timestamp}.png"
        #
        # # Save the image to a file in the specified folder
        # image.save(f"C:\\Users\\Shawn Dcosta\\Desktop\\Shawn\\Sem - 4\\Python MPR Final\\ClassCollab\\Whiteboard Contents\\{fe}")
        # print("Drawing saved successfully.")

    image_icon = PhotoImage(file="logo (1).png")
    root.iconphoto(False, image_icon)

    color_box = PhotoImage(file="color section.png")
    Label(root, image=color_box, bg="#f2f3f5").place(x=10, y=20)

    eraser = PhotoImage(file="eraser.png")
    Button(root, image=eraser, bg="#f2f3f5", command=new_canvas).place(x=30, y=410)

    save = PhotoImage(file="save2.png")
    Button(root, image=save, bg="white", command=save_canvas).place(x=30, y=450)

    colors = Canvas(root, bg="#fff", width=37, height=300, bd=0)
    colors.place(x=30, y=60)

    add = PhotoImage(file="addimage.png")
    addimage = Button(root, image=add, command=insertimage, padx=3.5)
    addimage.place(x=31, y=370)

    def display_pallete():
        id = colors.create_rectangle((10, 10, 30, 30), fill="black")
        colors.tag_bind(id, "<Button-1>", lambda x: show_color("black"))

        id = colors.create_rectangle((10, 40, 30, 60), fill="grey")
        colors.tag_bind(id, "<Button-1>", lambda x: show_color("grey"))

        id = colors.create_rectangle((10, 70, 30, 90), fill="yellow")
        colors.tag_bind(id, "<Button-1>", lambda x: show_color("yellow"))

        id = colors.create_rectangle((10, 100, 30, 120), fill="brown4")
        colors.tag_bind(id, "<Button-1>", lambda x: show_color("brown4"))

        id = colors.create_rectangle((10, 130, 30, 150), fill="red")
        colors.tag_bind(id, "<Button-1>", lambda x: show_color("red"))

        id = colors.create_rectangle((10, 160, 30, 180), fill="orange")
        colors.tag_bind(id, "<Button-1>", lambda x: show_color("orange"))

        id = colors.create_rectangle((10, 190, 30, 210), fill="green")
        colors.tag_bind(id, "<Button-1>", lambda x: show_color("green"))

        id = colors.create_rectangle((10, 220, 30, 240), fill="blue")
        colors.tag_bind(id, "<Button-1>", lambda x: show_color("blue"))

        id = colors.create_rectangle((10, 250, 30, 270), fill="purple")
        colors.tag_bind(id, "<Button-1>", lambda x: show_color("purple"))

    display_pallete()

    canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
    canvas.place(x=100, y=10)

    canvas.bind('<Button-1>', locate_xy)
    canvas.bind('<B1-Motion>', addline)

    cur_value = tk.DoubleVar()

    def get_cur_value():
        return '{: .2f}'.format(cur_value.get())

    def slider_changed(event):
        value_label.configure(text=get_cur_value())

    slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=slider_changed, variable=cur_value)
    slider.place(x=30, y=530)

    value_label = ttk.Label(root, text=get_cur_value())
    value_label.place(x=27, y=550)

    root.mainloop()
