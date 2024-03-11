from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogintion System")

        #============= Variabl=====================
        self.var_attend_Id=StringVar()
        self.var_attend_Roll=StringVar()
        self.var_attend_Name=StringVar()
        self.var_attend_Dep=StringVar()
        self.var_attend_Time=StringVar()
        self.var_attend_Date=StringVar()
        self.var_attend_Attendance=StringVar()
        



        title_lbl=Label(self.root,text="ATTENDANCE SYSTEM",font=("time new roman",20,"bold"),bg="red",fg="Blue")
        title_lbl.place(x=0,y=205,width=1530,height=25)

        img=Image.open(r"Image_detail/first.jpg")
        img=img.resize((800,200),Image.AFFINE)
        self.photoimg=ImageTk.PhotoImage(img)
         
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
        
        img1=Image.open(r"Image_detail/middle.jpg")
        img1=img1.resize((800,200),Image.AFFINE)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        main_frame=Frame(bd=2,bg="white")
        main_frame.place(x=10,y=235,width=1500,height=600)

         #left label frame .............
        LEFT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        LEFT_frame.place(x=10,y=10,width=707,height=580)

        img_left=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail\R.jpg")
        img_left=img_left.resize((690,130),Image.AFFINE)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(LEFT_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=690,height=130)

        left_inside_frame=Frame(LEFT_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135,width=690,height=390)

        #labelland entry=============

        #attendance Id 
        attendanceID_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",13,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_Id,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        roll_label=Label(left_inside_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_Roll,font=("times new roman",13,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #name 

        Name_label=Label(left_inside_frame,text="Name :",font=("times new roman",13,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_Name,font=("times new roman",13,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #department

        Depart_label=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        Depart_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_Dep,font=("times new roman",13,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #time 

        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_Time,font=("times new roman",13,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #date

        Date_label=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_Date,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #attendance 

        attendancelabel=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",13,"bold"),bg="white")
        attendancelabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_attend_Attendance,font="comicsansns 11 bold",state="randomly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,padx=10,pady=0,sticky=W)
        self.atten_status.current(0)

        # bbutton frame 
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white") 
        btn_frame.place(x=0,y=300,width=720,height=40)

        save_btn=Button(btn_frame,text="Import csv",width=16,command=self.importCsv,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,)

        Update_btn=Button(btn_frame,text="Export cs",width=16,command=self.ExportCSV,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=1,)

        Delete_btn=Button(btn_frame,text="Update",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2,)

        Reset_btn=Button(btn_frame,text="Reset",width=16,command=self.resetdata,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3,)

        #Right label frame ===================
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",13,"bold"))
        RIGHT_frame.place(x=720,y=10,width=760,height=580)

        table_frame=Frame(RIGHT_frame,bd=2,relief=RIDGE,bg="white") 
        table_frame.place(x=5,y=5,width=750,height=455)

        #Scrollbar  table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendancecReportTable=ttk.Treeview(table_frame,column=("Id","Roll","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendancecReportTable.xview)
        scroll_y.config(command=self.attendancecReportTable.yview)

        self.attendancecReportTable.heading("Id",Text="Attendance ID:")
        self.attendancecReportTable.heading("Roll",Text="Roll no:")
        self.attendancecReportTable.heading("Name",Text="Name:")
        self.attendancecReportTable.heading("Department",Text="Department:")
        self.attendancecReportTable.heading("Time",Text="Time")
        self.attendancecReportTable.heading("Date",Text="Date")
        self.attendancecReportTable.heading("Attendance",Text="Attendance")

        self.attendancecReportTable["show"]="headings"
        
        self.attendancecReportTable.column("Id",width=100)
        self.attendancecReportTable.column("Roll",width=100)
        self.attendancecReportTable.column("Name",width=100)
        self.attendancecReportTable.column("Department",width=100)
        self.attendancecReportTable.column("Time",width=100)
        self.attendancecReportTable.column("Date",width=100)
        self.attendancecReportTable.column("Attendance",width=100)
        
        self.attendancecReportTable.pack(fill=BOTH,expand=1)
        self.attendancecReportTable.bind("<ButtonRelease",self.get_cursor)

        #*************** fectch data   *************  

    def fetchdata(self,root):
        self.attendancecReportTable.delete(self.att.get_children())
        for i in rows:
            self.attendancecReportTable.insert("",END,values=i)

    # import csv

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*csv"),("All file","*.*")),parent=self.root)
        with open(fln) as myfiles:
            csvread=csv.reader(myfiles,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
            
          #Export csv..
    def ExportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No Data is found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*csv"),("All file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfiles:
                exp_write=csv.writer(myfiles,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data is exported"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



    def get_cursor(self,event=""):
        cursor_row=self.attendancecReportTable.focus()
        content=self.attendancecReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_Id.set(rows[0])
        self.var_attend_Roll.set(rows[1])
        self.var_attend_Name.set(rows[2]) 
        self.var_attend_Dep.set(rows[3])
        self.var_attend_Time.set(rows[4])
        self.var_attend_Date.set(rows[5])
        self.var_attend_Attendance.set(rows[6])
    
        
    def resetdata(self):
        self.var_attend_Id.set()
        self.var_attend_Roll.set()
        self.var_attend_Name.set() 
        self.var_attend_Dep.set()
        self.var_attend_Time.set()
        self.var_attend_Date.set()
        self.var_attend_Attendance.set()


if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()   