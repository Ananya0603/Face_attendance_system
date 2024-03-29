from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Face_Recognition_System:
    def _init_(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #bg img
        img = Image.open(r"D:\Face_Recognition_System\Face-Recognition-Student-Attendance-System\Project imgs\bgimg.png")
        img = img.resize((1530,790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image = self.photoimg)
        bg_img.place(x = 0, y= 0, width = 1400, height = 790)
        
        title_lbl = Label(bg_img, text = "FACE RECOGNITION ATTENDANCE SYSTEM", font=("georgia", 35,"bold"), bg= "black", fg="white")
        title_lbl.place(x=0, y=0, width= 1400, height= 45)

        # student button
        img1 = Image.open(r"D:\Face_Recognition_System\Face-Recognition-Student-Attendance-System\Project imgs\stu.png")
        img1 = img1.resize((150,150), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1= Button(bg_img, image= self.photoimg1, cursor= "hand2")
        b1.place(x=300, y=200, width= 150, height= 150)

        b1_1= Button(bg_img, text= "Student Details", cursor= "hand2", font=("georgia", 13,"bold"), bg= "black", fg="white")
        b1_1.place(x=300, y=350, width= 150, height= 40)

        # face recognition button
        img2 = Image.open(r"D:\Face_Recognition_System\Face-Recognition-Student-Attendance-System\Project imgs\face1.png")
        img2 = img2.resize((150,150), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2= Button(bg_img, image= self.photoimg2, cursor= "hand2")
        b2.place(x=600, y=200, width= 150, height= 150)

        b2_1= Button(bg_img, text= "Face Detector", cursor= "hand2", font=("georgia", 13,"bold"), bg= "black", fg="white")
        b2_1.place(x=600, y=350, width= 150, height= 40)

        # Attendance button
        img3 = Image.open(r"D:\Face_Recognition_System\Face-Recognition-Student-Attendance-System\Project imgs\attendance1.png")
        img3 = img3.resize((150,150), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3= Button(bg_img, image= self.photoimg3, cursor= "hand2")
        b3.place(x=900, y=200, width= 150, height= 150)

        b3_1= Button(bg_img, text= "Attendance", cursor= "hand2", font=("georgia", 13,"bold"), bg= "black", fg="white")
        b3_1.place(x=900, y=350, width= 150, height= 40)

        # Developer button
        img4 = Image.open(r"D:\Face_Recognition_System\Face-Recognition-Student-Attendance-System\Project imgs\dev.png")
        img4 = img4.resize((150,150), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4= Button(bg_img, image= self.photoimg4, cursor= "hand2")
        b4.place(x=300, y=450, width= 150, height= 150)

        b4_1= Button(bg_img, text= "Developer", cursor= "hand2", font=("georgia", 13,"bold"), bg= "black", fg="white")
        b4_1.place(x=300, y=600, width= 150, height= 40)

        # Help desk button
        img5 = Image.open(r"D:\Face_Recognition_System\Face-Recognition-Student-Attendance-System\Project imgs\help.png")
        img5 = img5.resize((150,150), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b5= Button(bg_img, image= self.photoimg5, cursor= "hand2")
        b5.place(x=600, y=450, width= 150, height= 150)

        b5_1= Button(bg_img, text= "Help Desk", cursor= "hand2", font=("georgia", 13,"bold"), bg= "black", fg="white")
        b5_1.place(x=600, y=600, width= 150, height= 40)

        # Exit button
        img6 = Image.open(r"D:\Face_Recognition_System\Face-Recognition-Student-Attendance-System\Project imgs\exit1.png")
        img6 = img6.resize((150,150), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6= Button(bg_img, image= self.photoimg6, cursor= "hand2")
        b6.place(x=900, y=450, width= 150, height= 150)

        b6_1= Button(bg_img, text= "Exit", cursor= "hand2", font=("georgia", 13,"bold"), bg= "black", fg="white")
        b6_1.place(x=900, y=600, width= 150, height= 40)

#=================================FUNCTIONS BUTTON=================================================================================================================#
def student_details(self):
    self.new_window= Toplevel(self.root)
    self.app= student(self.new_window)

if _name_ == "_main_":
            root = Tk()
            obj = Face_Recognition_System(root)
            root.mainloop()
