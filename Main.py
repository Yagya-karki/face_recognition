from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from train import train
from student import Student
from Face_Recognition import Face_Recogntion
from time import strptime
from datetime import datetime
import os
import mysql.connector
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recongition system")
        
        img=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail\rk.jpg")
        img=img.resize((500,130),Image.AFFINE)
        self.photoimg=ImageTk.PhotoImage(img)
         
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        
        img1=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail\second.jpg")
        img1=img1.resize((550,130),Image.AFFINE)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=500,height=130)
        
        
        
        img2=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail\third.jpg")
        img2=img2.resize((600,130),Image.AFFINE)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1020,y=0,width=500,height=130)
        
        #bg img#
        img3=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail\background.jpg")
        img3=img3.resize((1530,710),Image.AFFINE)
        self.photoimg3=ImageTk.PhotoImage(img3)
         
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #---------- time ----------
       # def time():
       #      string = strftime('%H:%M:%S %p')
       #      lbl.config(text = string)
       #      lbl.after(1000, time)
       # lbl = Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
       # lbl.place(x=0,y=0,width=110,height=50)
        #time() 
            



        
        #student buttom#
        img4=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail\st.jpg")
        img4=img4.resize((250,250),Image.AFFINE)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=90,width=310,height=250)
        
        b1_1=Button(bg_img,text="Student Detail",command=self.student_details,cursor="hand2",font=("time new roman",25,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=325,width=310,height=38)
        
        
        #detect face #
        img5=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail\231.jpg")
        img5=img5.resize((250,250),Image.AFFINE)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.Face_data)
        b1.place(x=430,y=90,width=310,height=250)
        
        b1_1=Button(bg_img,text="Face Recognition",cursor="hand2",command=self.Face_data,font=("time new roman",25,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=430,y=325,width=310,height=38)
        
        # attendance system#
        img6=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail/R.jpg")
        img6=img6.resize((250,250),Image.AFFINE)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=770,y=90,width=310,height=250)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("time new roman",25,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=770,y=325,width=310,height=38)
        
        #train data #
        
        img7=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail/train.jpg")
        img7=img7.resize((250,250),Image.AFFINE)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_data)
        b1.place(x=1100,y=90,width=310,height=250)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("time new roman",25,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=325,width=310,height=38)
        
        
        #Photos #
        img8=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail/st.jpg")
        img8=img8.resize((250,250),Image.AFFINE)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b1.place(x=100,y=395,width=310,height=250)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("time new roman",25,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=610,width=310,height=38)
        
        #Developer#
        img9=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail\dev.jpg")
        img9=img9.resize((250,250),Image.AFFINE)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.developer_data)
        b1.place(x=430,y=395,width=310,height=250)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("time new roman",25,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=430,y=610,width=310,height=38)
        
        #help desk#
        img10=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail/help.jpg")
        img10=img10.resize((250,250),Image.AFFINE)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.help_data)
        b1.place(x=770,y=395,width=310,height=250)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("time new roman",25,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=770,y=610,width=310,height=38)
        
        #Exit#
        img11=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail/exit.jpg")
        img11=img11.resize((250,250),Image.AFFINE)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.IExit)
        b1.place(x=1100,y=395,width=310,height=250)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.IExit,font=("time new roman",25,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=610,width=310,height=38)

    def open_img(self):
         os.startfile("data")  
    def IExit(self):
         self.IExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
         if  self.IExit >0:
              self.root.destroy()
         else:
              return     

        # function .....

    def student_details(self):
         self.new_window=Toplevel(self.root)
         self.app=Student(self.new_window)

    def train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=train(self.new_window)
    def Face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_Recogntion(self.new_window)   
    def attendance_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendance(self.new_window)     
    def developer_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Developer(self.new_window)     
    def help_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Help(self.new_window)     
                                         
        
            
        
if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
    
