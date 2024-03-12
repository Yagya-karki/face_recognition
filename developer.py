from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recongition system")
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("time new roman",35,"bold"),bg="Blue",fg="yellow")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"Image_detail/dev.jpg")
        img_top=img_top.resize((1530,720),Image.AFFINE)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=5,y=55,width=1530,height=720)

        #frame =============
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"Image_detail/image.jpg")
        img_top1=img_top1.resize((200,200),Image.AFFINE)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        #developer info.............
        dev_label=Label(main_frame,text="Hello, Everyone ",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="Facial Recognition system ",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        dev_label=Label(main_frame,text="Based On attendance system ",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=60)

        dev_label=Label(main_frame,text="Yagya bikram karki, Rakesh chaudhary",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=80)

        dev_label=Label(main_frame,text="Babaratna Bishal Sakya  are developer  ",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=100)

        img2=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail/download.jpg")
        img2=img2.resize((500,385),Image.AFFINE)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=385)

if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()        