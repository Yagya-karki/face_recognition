from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2

class HelpDesk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System Help Desk")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="blue", fg="yellow")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"Image_detail/helpdesk.jpg")
        img_top = img_top.resize((1530, 720), Image.AFFINE)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=5, y=55, width=1530, height=720)

        help_label = Label(f_lbl, text="Email: karkibikram786@gmail.com", font=("times new roman", 25, "bold"), bg="white")
        help_label.place(x=600, y=450)

if __name__ == "__main__":
    root = Tk()
    obj = HelpDesk(root)
    root.mainloop()