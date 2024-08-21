from tkinter import *
from tkinter import messagebox

import pymongo
from PIL import Image
import customtkinter as ctk
from pymongo import MongoClient, collection, UpdateOne
from dashboard import *


def click():
    print("I was clicked")


def store_regi_credentials(username, password, con_pass):
    client = MongoClient("mongodb://localhost:27017")
    db = client.ClassCollab
    collection = db.Register_details
    login_data = {
        "username": username,
        "password": password,
        "con_pass": con_pass,
    }
    collection.insert_one(login_data)
    client.close()


def login():
    class MyFrame(ctk.CTkFrame):

        def regi_store(self):
            username = self.n_user.get()
            password = self.np_word.get()
            con_pass = self.rp_word.get()

            client = MongoClient("mongodb://localhost:27017")
            db = client.ClassCollab
            collection = db.Register_details

            existing_username = collection.find_one({"username": username})
            if existing_username:
                messagebox.showerror("Registration Failed", "Username already exists!")
            else:
                if password == con_pass:
                    store_regi_credentials(username, password, con_pass)
                    messagebox.showinfo("Registration Successful",
                                        f"{username} your account has been created successfully!")
                else:
                    messagebox.showerror("Registration Failed", "Passwords do not match!")

        def login_fetch(self):
            username = self.u_name.get()
            password = self.p_word.get()

            client = MongoClient("mongodb://localhost:27017")
            db = client.ClassCollab
            collection = db.Register_details

            user_data = collection.find_one({"username": username})
            if user_data:
                if user_data["password"] == password:
                    messagebox.showinfo("Login Successful", "Welcome, " + username)
                    dashboard()
                else:
                    messagebox.showerror("Login Failed", "Incorrect Password!")
            else:
                messagebox.showerror("Login Failed", "Username not found!")

            client.close()

        def forget_password(self):
            client = MongoClient("mongodb://localhost:27017")
            db = client.ClassCollab
            collection = db.Register_details
            # Retrieve username from forget password form field
            entered_username = self.f_user.get()

            # Find the user document based on username
            filter = {"username": entered_username}

            user = collection.find_one(filter)

            if not user:
                messagebox.showerror("Password Reset Unsuccessful!", "Check the username entered.")
            else:
                new_password = self.fp_word.get()
                confirm_password = self.rfp_word.get()

                if new_password != confirm_password:
                    messagebox.showerror("Password Reset Unsuccessful!", "Passwords do not match!")
                    return
                # Update the password field with a new value (obtained from user input)
                update = {"$set": {"password": new_password, "con_pass": confirm_password}}  # Replace new_password with user input
                updated_user = collection.find_one_and_update(filter, update)
                # Use find_one_and_update to find and update the document in one step
                if updated_user:
                    # Password update successful (updated user document returned)
                    # print("Password updated successfully!")
                    messagebox.showinfo("Password Reset Successful!", "Your Password was reset successfully.")
                    # else:
                    #     # User not found or update failed
                    #     # print("Error: Username not found or password update failed.")
                    #     messagebox.showerror("Password Reset Unsuccessful!", "Check the username or password entered.")
                else:
                    messagebox.showerror("Password Reset Unsuccessful!", "Check the username or password.")

        def clear(self):
            for widget in self.winfo_children():
                widget.destroy()

        def clear_frame(self):
            for widget in self.winfo_children():
                widget.destroy()
            self.registration()

        def forget(self):
            self.clear()
            arr = ctk.CTkImage(dark_image=Image.open("left_arr.png"), size=(25, 25))

            self.label = ctk.CTkLabel(self,
                                      text="RESET PASSWORD",
                                      font=("Segoe UI Variable Display Light", 38),
                                      text_color="#F89F63")
            self.label.place(x=175, y=85)

            self.back = ctk.CTkButton(self,
                                      text="",
                                      fg_color="#4A4A8F",
                                      hover_color="#4A4A8F",
                                      corner_radius=35,
                                      height=30,
                                      width=20,
                                      command=self.log,
                                      image=arr)
            self.back.place(x=5, y=25)

            self.f_user = ctk.CTkEntry(self,
                                       placeholder_text="Username",
                                       height=40,
                                       width=250,
                                       font=("Consolas", 20),
                                       fg_color="white",
                                       text_color="black",
                                       corner_radius=25
                                       )
            self.f_user.place(x=195, y=215)

            self.fp_word = ctk.CTkEntry(self,
                                        placeholder_text="Enter New Password",
                                        height=40,
                                        width=250,
                                        font=("Consolas", 20),
                                        fg_color="white",
                                        text_color="black",
                                        corner_radius=25,
                                        show="*",
                                        )
            self.fp_word.place(x=195, y=315)

            self.rfp_word = ctk.CTkEntry(self,
                                         placeholder_text="Confirm New Password",
                                         height=40,
                                         width=250,
                                         font=("Consolas", 18),
                                         fg_color="white",
                                         text_color="black",
                                         corner_radius=25,
                                         show="*",
                                         )
            self.rfp_word.place(x=195, y=415)

            self.confirm = ctk.CTkButton(self,
                                         text="Confirm",
                                         corner_radius=13,
                                         fg_color="#E6E6FA",
                                         font=("Berlin Sans FB", 20),
                                         height=30,
                                         width=125,
                                         hover_color="#CCCCFF",
                                         text_color="#722F37",
                                         border_width=3,
                                         border_color="#722F37",
                                         command=self.forget_password)
            self.confirm.place(x=255, y=500)

        def registration(self):

            arr = ctk.CTkImage(dark_image=Image.open("left_arr.png"), size=(25, 25))

            self.label = ctk.CTkLabel(self,
                                      text="CREATE AN ACCOUNT",
                                      font=("Segoe UI Variable Display Light", 38),
                                      text_color="#F89F63")
            self.label.place(x=140, y=85)

            self.back = ctk.CTkButton(self,
                                      text="",
                                      fg_color="#4A4A8F",
                                      hover_color="#4A4A8F",
                                      corner_radius=35,
                                      height=30,
                                      width=20,
                                      command=self.log,
                                      image=arr)
            self.back.place(x=5, y=25)

            self.n_user = ctk.CTkEntry(self,
                                       placeholder_text="Enter Username",
                                       height=40,
                                       width=250,
                                       font=("Consolas", 20),
                                       fg_color="white",
                                       text_color="black",
                                       corner_radius=25
                                       )
            self.n_user.place(x=195, y=215)

            self.np_word = ctk.CTkEntry(self,
                                        placeholder_text="Enter Password",
                                        height=40,
                                        width=250,
                                        font=("Consolas", 20),
                                        fg_color="white",
                                        text_color="black",
                                        corner_radius=25,
                                        show="*",
                                        )
            self.np_word.place(x=195, y=315)

            self.rp_word = ctk.CTkEntry(self,
                                        placeholder_text="Confirm Password",
                                        height=40,
                                        width=250,
                                        font=("Consolas", 20),
                                        fg_color="white",
                                        text_color="black",
                                        corner_radius=25,
                                        show="*",
                                        )
            self.rp_word.place(x=195, y=415)

            self.regi = ctk.CTkButton(self,
                                      text="Register",
                                      corner_radius=13,
                                      fg_color="#E6E6FA",
                                      font=("Berlin Sans FB", 20),
                                      height=30,
                                      width=125,
                                      hover_color="#CCCCFF",
                                      text_color="#722F37",
                                      border_width=3,
                                      border_color="#722F37",
                                      command=self.regi_store)
            self.regi.place(x=255, y=500)

        def log(self):
            self.clear()
            img = ctk.CTkImage(dark_image=Image.open("logo_name3.png"), size=(250, 85))

            # add widgets onto the frame, for example:
            self.label = ctk.CTkLabel(self,
                                      text="Welcome to",
                                      font=("Eras Demi ITC", 38),
                                      text_color="#F89F63",
                                      )
            self.label.place(x=100, y=75)

            self.img_label = ctk.CTkLabel(self, image=img, text="")
            self.img_label.place(x=323, y=52)

            self.u_name = ctk.CTkEntry(self,
                                       placeholder_text="Username",
                                       height=40,
                                       width=250,
                                       font=("Consolas", 20),
                                       fg_color="white",
                                       text_color="black",
                                       corner_radius=25)
            self.u_name.place(x=205, y=235)

            self.p_word = ctk.CTkEntry(self,
                                       placeholder_text="Password",
                                       height=40,
                                       width=250,
                                       font=("Consolas", 20),
                                       fg_color="white",
                                       text_color="black",
                                       corner_radius=25,
                                       show="*",
                                       )
            self.p_word.place(x=205, y=335)

            self.submit = ctk.CTkButton(self,
                                        text="Submit",
                                        corner_radius=13,
                                        fg_color="#E6E6FA",
                                        font=("Berlin Sans FB", 20),
                                        height=30,
                                        width=125,
                                        hover_color="#CCCCFF",
                                        text_color="#722F37",
                                        border_width=3,
                                        border_color="#722F37",
                                        command=self.login_fetch)
            self.submit.place(x=265, y=435)

            self.forgot_pwd = ctk.CTkLabel(self,
                                           text="Don't remember your password?",
                                           font=("Candara", 15),
                                           text_color="white")
            self.forgot_pwd.place(x=165, y=510)

            self.forget_pwd = ctk.CTkButton(self,
                                            text="Forget password",
                                            corner_radius=13,
                                            fg_color="#4A4A8F",
                                            font=("Berlin Sans FB", 15),
                                            height=25,
                                            width=75,
                                            hover=False,
                                            text_color="white",
                                            command=self.forget)
            self.forget_pwd.place(x=375, y=512)

            self.new_admin = ctk.CTkLabel(self,
                                          text="New Admin?",
                                          font=("Candara", 15),
                                          text_color="white")
            self.new_admin.place(x=245, y=540)

            self.reg_here = ctk.CTkButton(self,
                                          text="Register here",
                                          corner_radius=13,
                                          fg_color="#4A4A8F",
                                          font=("Berlin Sans FB", 15),
                                          height=25,
                                          width=75,
                                          hover=False,
                                          text_color="white",
                                          command=self.clear_frame)
            self.reg_here.place(x=325, y=542)

        def __init__(self, master, **kwargs):
            super().__init__(master, **kwargs)
            self.log()

            # self.label.grid(row=0, column=0, padx=20)

    class App(ctk.CTkToplevel):
        def __init__(self):
            super().__init__()
            self.geometry("1200x720+200+50")

            kid = ctk.CTkImage(dark_image=Image.open("login_kid.png"), size=(375, 375))
            kid_label = ctk.CTkLabel(master=self, image=kid, text="")
            kid_label.place(x=80, y=150)

            self.configure(fg_color="#242455")
            self.title("Login")
            # self.grid_rowconfigure(0, weight=1)  # configure grid system
            # self.grid_columnconfigure(0, weight=1)

            self.my_frame = MyFrame(master=self, width=620, height=680, corner_radius=30, fg_color="#4A4A8F")
            self.my_frame.place(x=560, y=20)
            # self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    app = App()
    app.mainloop()

# login()

# import pyautogui
#
# # Get the screen width and height
# screen_width, screen_height = pyautogui.size()
#
# print("Screen Width:", screen_width)
# print("Screen Height:", screen_height)
