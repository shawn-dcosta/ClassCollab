import csv

from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
from pymongo import MongoClient
from add_faces import *
from whiteboard import *


def store_profile_credentials(name, surname, email, gender, phone_number):
    client = MongoClient("mongodb://localhost:27017")
    db = client.ClassCollab
    collection = db.Profile_details
    profile_data = {
        "name": name,
        "surname": surname,
        "email": email,
        "gender": gender,
        "phone_number": phone_number
    }
    collection.insert_one(profile_data)
    client.close()


class MainFrame(CTkFrame):
    def clear(self):
        for widget in self.frm.winfo_children():
            widget.destroy()

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # def clear_frame(self):
        #     for widget in self.winfo_children():
        #         widget.destroy()

        self.frm = CTkFrame(master=self, width=1200, height=820, fg_color="#4A4A8F")
        self.frm.place(x=100, y=0)

        def home():
            self.clear()
            self.filler_img = CTkImage(dark_image=Image.open("Filler.png"), size=(1200, 780))

            self.home_label = CTkLabel(self.frm,
                                       text="",
                                       image=self.filler_img,
                                       fg_color="#4A4A8F"
                                       )
            self.home_label.place(x=0, y=0)

        home()

        self.profile_img = CTkImage(dark_image=Image.open("Icon-User.png"), size=(35, 35))
        self.add_user_img = CTkImage(dark_image=Image.open("add-user.png"), size=(35, 35))
        self.whiteboard_img = CTkImage(dark_image=Image.open("Icon-Whiteboard.png"), size=(35, 35))
        self.face_recog_img = CTkImage(dark_image=Image.open("Icon-Face-recog.png"), size=(35, 35))
        self.logout_img = CTkImage(dark_image=Image.open("Icon-Logout.png"), size=(35, 35))

        self.side_frame = CTkFrame(master=self, width=100, height=820, fg_color="#242455")
        self.side_frame.place(x=0, y=0)

        self.logo_i = CTkImage(dark_image=Image.open("sq_logo_resize.gif"), size=(65, 65))

        # def home_frame(self):
        #     self.clear()
        #     home_label = CTkLabel(self,
        #                           text="",
        #                           image=self.filler_img)

        self.home = CTkButton(self.side_frame,
                              width=50,
                              text="",
                              fg_color="#242455",
                              hover_color="#4A4A8F",
                              image=self.logo_i,
                              command=home)
        self.home.place(x=10, y=10)

        self.prof = CTkButton(self.side_frame,
                              text="Profile",
                              font=("Montserrat Regular", 13),
                              width=50,
                              text_color="white",
                              fg_color="#242455",
                              hover_color="#4A4A8F",
                              image=self.profile_img,
                              compound="top",
                              command=self.profile_frame)
        self.prof.place(x=25, y=150)

        self.add = CTkButton(self.side_frame,
                             text="Add Member",
                             font=("Montserrat Regular", 13),
                             width=50,
                             height=5,
                             text_color="white",
                             fg_color="#242455",
                             image=self.add_user_img,
                             compound="top",
                             hover_color="#4A4A8F",
                             command=self.add_mem
                             )
        self.add.place(x=7, y=250)

        self.board = CTkButton(self.side_frame,
                               text="White Board",
                               font=("Montserrat Regular", 13),
                               width=50,
                               height=5,
                               text_color="white",
                               fg_color="#242455",
                               image=self.whiteboard_img,
                               compound="top",
                               hover_color="#4A4A8F",
                               command=white_brd
                               )
        self.board.place(x=7, y=350)

        self.attend = CTkButton(self.side_frame,
                                text="Attendance",
                                font=("Montserrat Regular", 13),
                                width=50,
                                height=5,
                                text_color="white",
                                fg_color="#242455",
                                image=self.face_recog_img,
                                compound="top",
                                hover_color="#4A4A8F",
                                command=stud_attendance
                                )
        self.attend.place(x=7, y=450)

        self.logout = CTkButton(self.side_frame,
                                text="Logout",
                                font=("Montserrat Regular", 13),
                                width=20,
                                text_color="white",
                                fg_color="#242455",
                                hover_color="#4A4A8F",
                                image=self.logout_img,
                                compound="top",
                                command=self.logout)
        self.logout.place(x=20, y=550)

        self.prof_sf = CTkScrollableFrame(master=self.frm, width=500, height=500, fg_color="#CBC3E3")

        self.label1 = CTkLabel(self.prof_sf,
                               text="ENTER YOUR DETAILS",
                               font=("Segoe UI Variable Display Light", 38),
                               text_color="black")
        self.label1.pack()

        # self.username = CTkEntry(self.prof_sf,
        #                          placeholder_text="Will be fetched from DB",
        #                          height=40,
        #                          width=250,
        #                          font=("Consolas", 20),
        #                          fg_color="white",
        #                          text_color="black",
        #                          corner_radius=25,
        #                          )
        # self.username.insert(0, "Fetched From DB")
        # self.username.configure(state="disable")
        # self.username.pack(pady=30)

        self.name = CTkEntry(self.prof_sf,
                             placeholder_text="Enter your name",
                             height=40,
                             width=250,
                             font=("Consolas", 20),
                             fg_color="white",
                             text_color="black",
                             corner_radius=25
                             )
        self.name.pack(pady=30)

        self.surname = CTkEntry(self.prof_sf,
                                placeholder_text="Enter your surname",
                                height=40,
                                width=250,
                                font=("Consolas", 20),
                                fg_color="white",
                                text_color="black",
                                corner_radius=25
                                )
        self.surname.pack(pady=30)

        self.email = CTkEntry(self.prof_sf,
                              placeholder_text="Enter your email",
                              height=40,
                              width=250,
                              font=("Consolas", 20),
                              fg_color="white",
                              text_color="black",
                              corner_radius=25
                              )
        self.email.pack(pady=30)

        self.gender = CTkLabel(self.prof_sf,
                               text="Gender:",
                               font=("Segoe UI Variable Display Medium", 20),
                               text_color="black")
        self.gender.pack()

        self.radio_var = StringVar(value="null")

        self.male = CTkRadioButton(self.prof_sf,
                                   text="Male",
                                   value="M",
                                   variable=self.radio_var,
                                   text_color="black",
                                   radiobutton_width=18,
                                   radiobutton_height=18,
                                   font=("Consolas", 20),
                                   border_color="#722F37",
                                   fg_color="#A95C68",
                                   hover_color="white")
        self.male.pack(pady=10)

        self.female = CTkRadioButton(self.prof_sf,
                                     text="Female",
                                     value="F",
                                     variable=self.radio_var,
                                     text_color="black",
                                     radiobutton_width=18,
                                     radiobutton_height=18,
                                     font=("Consolas", 20),
                                     border_color="#722F37",
                                     fg_color="#A95C68",
                                     hover_color="white")
        self.female.pack(pady=10)

        self.phn_no = CTkEntry(self.prof_sf,
                               placeholder_text="Enter your Phone No.",
                               height=40,
                               width=250,
                               font=("Consolas", 20),
                               fg_color="white",
                               text_color="black",
                               corner_radius=25
                               )
        self.phn_no.pack(pady=30)

        self.save = CTkButton(self.prof_sf,
                              text="Save",
                              corner_radius=13,
                              fg_color="#E6E6FA",
                              font=("Berlin Sans FB", 20),
                              height=30,
                              width=125,
                              hover_color="#CCCCFF",
                              text_color="#722F37",
                              border_width=3,
                              border_color="#722F37",
                              command=self.profile_details_save
                              )
        self.save.pack()

    def logout(self):
        messagebox.showinfo("Log out", "Logged out Successfully!")
        self.master.destroy()

    def add_mem(self):
        self.clear()

        self.add_user_img2 = CTkImage(dark_image=Image.open("add_user_img.png"), size=(1200, 780))

        self.add_user_label = CTkLabel(self.frm,
                                       text="",
                                       image=self.add_user_img2)
        self.add_user_label.place(x=0, y=0)

        self.label = CTkLabel(self.frm,
                              text="Generate Email IDs and Passwords for New Members",
                              font=("Segoe UI Variable Display Regular", 35),
                              text_color="white")
        self.label.place(x=175, y=20)
        # self.label.pack()

        self.num_members_label = CTkLabel(self.frm,
                                          text="Enter the number of new members:",
                                          font=("Segoe UI Variable Display Regular", 30),
                                          text_color="white")
        self.num_members_label.place(x=350, y=250)
        # self.num_members_label.pack(pady=40)

        self.num_members_entry = CTkEntry(self.frm,
                                          placeholder_text="Enter the number",
                                          height=40,
                                          width=250,
                                          font=("Consolas", 20),
                                          fg_color="white",
                                          text_color="black",
                                          corner_radius=15)
        self.num_members_entry.place(x=450, y=350)
        # self.num_members_entry.pack()

        self.generate_button = CTkButton(self.frm,
                                         text="Generate",
                                         corner_radius=10,
                                         fg_color="#E6E6FA",
                                         font=("Berlin Sans FB", 16),
                                         height=40,
                                         width=125,
                                         hover_color="#CCCCFF",
                                         text_color="#722F37",
                                         border_width=3,
                                         border_color="#722F37",
                                         command=self.generate_emails_passwords)
        self.generate_button.place(x=513, y=450)
        # self.generate_button.pack(pady=30)

    def generate_emails_passwords(self):

        # Password Generator Project
        import random
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        num_members = int(self.num_members_entry.get())
        generated_data = []
        for i in range(num_members):

            password_list = []

            for char in range(1, 5):
                password_list.append(random.choice(letters))
            # print(password_list)

            for symbol in range(1, 2):
                password_list.append(random.choice(symbols))
            # print(password_list)

            for num in range(1, 4):
                password_list.append(random.choice(numbers))

            # print(password_list)
            random.shuffle(password_list)
            # print(password_list)
            passwrd = ''.join(password_list)
            email = f"tsec100{i + 1}@ccmail.com"
            password = passwrd  # You can generate a random password here if needed
            generated_data.append({"email": email, "password": password})

        # You can do something with the generated data, such as displaying it or storing it in a database
        # for data in generated_data:
        #     print(f"Email: {data['email']}, Password: {data['password']}")

        # with open('output.csv', 'w', newline='') as csvfile:
        output_file_path = "C:\\Users\\Shawn Dcosta\\Desktop\\Shawn\\Sem - 4\\Python MPR Final\\ClassCollab\\Generated Emails\\output.csv"
        with open(output_file_path, 'w', newline='') as csvfile:
            fieldnames = ['email', 'password']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for data in generated_data:
                writer.writerow(data)

    def profile_details_save(self):
        n_name = self.name.get()
        n_surname = self.surname.get()
        n_email = self.email.get()
        n_gender = self.radio_var.get()
        n_phn_no = self.phn_no.get()

        store_profile_credentials(n_name, n_surname, n_email, n_gender, n_phn_no)

        self.name.configure(state="disabled")
        self.surname.configure(state="disabled")
        self.email.configure(state="disabled")
        self.male.configure(state="disabled")
        self.female.configure(state="disabled")
        self.phn_no.configure(state="disabled")

        messagebox.showinfo("Registration Successful", f"{n_name}, your profile has been saved successfully!")

    def profile_frame(self):
        self.clear()

        # self.frm.place(x=100,y=0)
        # self.side_frame.place(x=0, y=0)

        def pic_fetch():
            filename = filedialog.askopenfilename(title="Select Image", filetypes=(
                ("Image files", ".png;.jpg;.jpeg;.gif"), ("All files", ".")))
            if filename:
                image = Image.open(filename)
                photo = CTkImage(image, size=(450, 450))
                profile_pic_button.configure(image=photo)
                profile_pic_button.image = photo
                profile_pic_button.configure(text="")

        profile_pic_img = CTkImage(dark_image=Image.open("profile_pic.png"), size=(400, 400))
        profile_pic_button = CTkButton(self.frm,
                                       text="Upload Profile Photo",
                                       font=("Montserrat Regular", 25),
                                       text_color="black",
                                       image=profile_pic_img,
                                       width=450,
                                       height=450,
                                       hover=False,
                                       fg_color="white",
                                       compound=TOP,
                                       command=pic_fetch)
        profile_pic_button.place(x=75, y=180)

        self.prof_sf = CTkScrollableFrame(master=self.frm, width=500, height=500, fg_color="#CBC3E3")

        self.label1 = CTkLabel(self.prof_sf,
                               text="ENTER YOUR DETAILS",
                               font=("Segoe UI Variable Display Light", 38),
                               text_color="black")
        self.label1.pack()

        # self.username = CTkEntry(self.prof_sf,
        #                          placeholder_text="Will be fetched from DB",
        #                          height=40,
        #                          width=250,
        #                          font=("Consolas", 20),
        #                          fg_color="white",
        #                          text_color="black",
        #                          corner_radius=25,
        #                          )
        # self.username.insert(0, "Fetched From DB")
        # self.username.configure(state="disable")
        # self.username.pack(pady=30)

        self.name = CTkEntry(self.prof_sf,
                             placeholder_text="Enter your name",
                             height=40,
                             width=250,
                             font=("Consolas", 20),
                             fg_color="white",
                             text_color="black",
                             corner_radius=25
                             )
        self.name.pack(pady=30)

        self.surname = CTkEntry(self.prof_sf,
                                placeholder_text="Enter your surname",
                                height=40,
                                width=250,
                                font=("Consolas", 20),
                                fg_color="white",
                                text_color="black",
                                corner_radius=25
                                )
        self.surname.pack(pady=30)

        self.email = CTkEntry(self.prof_sf,
                              placeholder_text="Enter your email",
                              height=40,
                              width=250,
                              font=("Consolas", 20),
                              fg_color="white",
                              text_color="black",
                              corner_radius=25
                              )
        self.email.pack(pady=30)

        self.gender = CTkLabel(self.prof_sf,
                               text="Gender:",
                               font=("Segoe UI Variable Display Medium", 20),
                               text_color="black")
        self.gender.pack()

        self.radio_var = StringVar(value="null")

        self.male = CTkRadioButton(self.prof_sf,
                                   text="Male",
                                   value="M",
                                   variable=self.radio_var,
                                   text_color="black",
                                   radiobutton_width=18,
                                   radiobutton_height=18,
                                   font=("Consolas", 20),
                                   border_color="#722F37",
                                   fg_color="#A95C68",
                                   hover_color="white")
        self.male.pack(pady=10)

        self.female = CTkRadioButton(self.prof_sf,
                                     text="Female",
                                     value="F",
                                     variable=self.radio_var,
                                     text_color="black",
                                     radiobutton_width=18,
                                     radiobutton_height=18,
                                     font=("Consolas", 20),
                                     border_color="#722F37",
                                     fg_color="#A95C68",
                                     hover_color="white")
        self.female.pack(pady=10)

        self.phn_no = CTkEntry(self.prof_sf,
                               placeholder_text="Enter your Phone No.",
                               height=40,
                               width=250,
                               font=("Consolas", 20),
                               fg_color="white",
                               text_color="black",
                               corner_radius=25
                               )
        self.phn_no.pack(pady=30)

        self.save = CTkButton(self.prof_sf,
                              text="Save",
                              corner_radius=13,
                              fg_color="#E6E6FA",
                              font=("Berlin Sans FB", 20),
                              height=30,
                              width=125,
                              hover_color="#CCCCFF",
                              text_color="#722F37",
                              border_width=3,
                              border_color="#722F37",
                              command=self.profile_details_save
                              )
        self.save.pack()

        self.prof_sf.place(x=600, y=150, in_=self.frm)


class App(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("1300x780+125+0")
        self.title("Dashboard")

        self.main_frame = MainFrame(master=self, width=1300, height=780, fg_color="white")
        self.main_frame.place(x=0, y=0)  # 4A4A8F


def dashboard():
    app = App()
    app.mainloop()

# dashboard()
