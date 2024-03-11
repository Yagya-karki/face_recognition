from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recongition system")

        # variable ....
        self.var_Dep=StringVar()
        self.var_Course=StringVar()
        self.var_Year=StringVar()
        self.var_Semester=StringVar()
        self.var_Std_Id=StringVar()
        self.var_Std_Name=StringVar()
        self.var_Div=StringVar()
        self.var_Roll=StringVar()
        self.var_Gender=StringVar()
        self.var_DOB=StringVar()
        self.var_Email=StringVar()
        self.var_Phone=StringVar()
        self.var_Address=StringVar()
        self.var_Teacher=StringVar()

 
        
        img=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail\first.jpg")
        img=img.resize((500,130),Image.AFFINE)
        self.photoimg=ImageTk.PhotoImage(img)
         
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        
        img1=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail\middle.jpg")
        img1=img1.resize((550,130),Image.AFFINE)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=500,height=130)
        
        
        img2=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail/2580.jpg")
        img2=img2.resize((550,130),Image.AFFINE)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1020,y=0,width=500,height=130)
        
        
        img3=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail\bg.jpg")
        img3=img3.resize((1530,710),Image.AFFINE)
        self.photoimg3=ImageTk.PhotoImage(img3)
         
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="STUDENTS MANAGEMENT SYSTEM",font=("time new roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)
        
        #left label frame .............
        LEFT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        LEFT_frame.place(x=10,y=10,width=707,height=580)
        
        img_left=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail\R.jpg")
        img_left=img_left.resize((690,130),Image.AFFINE)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(LEFT_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=690,height=130)
        
        #label frame ............
        Current_course_frame=LabelFrame(LEFT_frame,bd=2,bg="white",relief=RIDGE,text="Current Details",font=("times new roman",13,"bold"))
        Current_course_frame.place(x=5,y=135,width=690,height=125)
        
        
        #department.............
        dep_label=Label(Current_course_frame,text="Deparment",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Dep,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechincal","CSIT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #course....
        course_label=Label(Current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE",)
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #year.....
        
        Year_label=Label(Current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        Year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Year,font=("times new roman",13,"bold"),state="readonly",width=20)
        Year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #semster .......
        Semster_label=Label(Current_course_frame,text="Semster",font=("times new roman",13,"bold"),bg="white")
        Semster_label.grid(row=1,column=2,padx=10,sticky=W)
        
        Semster_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        Semster_combo["values"]=("Select Semster","Semster-1","Semster-2","Semster-3","Semster-4","Semster-5")
        Semster_combo.current(0)
        Semster_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        # class information....
        Class_Student_frame=LabelFrame(LEFT_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=3,y=260,width=690,height=293)


        #Student ID ........
        StudentID_label=Label(Class_Student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Std_Id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student name ........

        StudentName_label=Label(Class_Student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Std_Name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class didivision .....

        Class_div_label=Label(Class_Student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        Class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        #Class_div_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Div,width=20,font=("times new roman",13,"bold"))
        #Class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_Div,font=("times new roman",13,"bold"),state="readonly",width=18)
        div_combo["values"]=("A","B","C",)
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll no .........

        Roll_No_label=Label(Class_Student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        Roll_No_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        Roll_No_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Roll,width=20,font=("times new roman",13,"bold"))
        Roll_No_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender

        Gender_label=Label(Class_Student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        

        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_Gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other",)
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Day of Births....
        
        dob_label=Label(Class_Student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email...

        email_label=Label(Class_Student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone No....

        
        Phone_label=Label(Class_Student_frame,text="Phone:",font=("times new roman",13,"bold"),bg="white")
        Phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        Phone_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Phone,width=20,font=("times new roman",13,"bold"))
        Phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address....

        
        address_label=Label(Class_Student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher .....
        
        
        Teacher_label=Label(Class_Student_frame,text="Teacher Nmae:",font=("times new roman",13,"bold"),bg="white")
        Teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        Teacher_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Teacher,width=20,font=("times new roman",13,"bold"))
        Teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="take Photo sample",value="yes")
        radiobtn1.grid(row=6,column=0,padx=10,pady=5,sticky=W)
        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text=" No take Photo sample",value="No")
        radiobtn2.grid(row=6,column=1,padx=10,pady=5,sticky=W)

       # bbutton frame 
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white") 
        btn_frame.place(x=0,y=205,width=720,height=39)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,)

        Update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=1,)

        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2,)

        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3,)

        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white") 
        btn_frame.place(x=0,y=240,width=720,height=35)

        Take_photo_btn=Button(btn_frame,command=self.Generate_dataset,text="Take Photo Sample",width=34,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Take_photo_btn.grid(row=0,column=0,)

        Update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=34,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_photo_btn.grid(row=0,column=1,)
    

        #Right label frame
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",13,"bold"))
        RIGHT_frame.place(x=720,y=10,width=760,height=580)

        img_right=Image.open(r"C:\Users\~acer~\Desktop\Face recognition System\Image_detail\student.jpg")
        img_right=img_right.resize((750,130),Image.AFFINE)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(RIGHT_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=750,height=130)
       

       # searching ........system

        Search_frame=LabelFrame(RIGHT_frame,bd=2,bg="white",relief=RIDGE,text="Search",font=("times new roman",12,"bold"))
        Search_frame.place(x=3,y=135,width=745,height=70)
 
        Search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="blue")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        Search_combo["values"]=("Select","Roll No","Phone",)
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        Search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        Search_btn=Button(Search_frame,text="Search",width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=4)

        Show_btn=Button(Search_frame,text="Show All",width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Show_btn.grid(row=0,column=4,padx=4)

         # table fram

        Table_frame=Frame(RIGHT_frame,bd=2,bg="white",relief=RIDGE,)
        Table_frame.place(x=3,y=210,width=745,height=345)

        SCROLL_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        SCROLL_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,column=("Dep","Course","Year","Sem","Id","Name","Div","Roll","Gender","Address","DOB","Phone","email","teacher","Photo",),xscrollcommand=SCROLL_x.set,yscrollcommand=SCROLL_y.set)
        SCROLL_x.pack(side=BOTTOM,fill=X)
        SCROLL_y.pack(side=RIGHT,fill=Y)
        SCROLL_x.config(command=self.student_table.xview)
        SCROLL_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Id",text="StudentId")
        self.student_table.heading("Roll",text="Roll No")
        self.student_table.heading("Gender",text="Gender")

        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSampleState")
        self.student_table["show"]="headings"


        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # function decaration..........
        
    def add_data(self):
        if self.var_Dep.get()=="select Department" or self.var_Std_Name.get()=="" or self.var_Std_Id.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="text@12345",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_Dep.get(),
                                                                                                                self.var_Course.get(),
                                                                                                                self.var_Year.get(),
                                                                                                                self.var_Semester.get(),
                                                                                                                self.var_Std_Id.get(),
                                                                                                                self.var_Std_Name.get(),
                                                                                                                self.var_Div.get(),
                                                                                                                self.var_Roll.get(),
                                                                                                                self.var_Gender.get(),
                                                                                                                self.var_DOB.get(),
                                                                                                                self.var_Email.get(),
                                                                                                                self.var_Phone.get(),
                                                                                                                self.var_Address.get(),
                                                                                                                self.var_Teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            

                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student details has been added successfully",parent=self.root)
            except Exception as es:
               messagebox.showinfo("Error",f"Due to :{str(es)}",parent=self.root)
#................................... fetch data..................#
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="text@12345",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.Delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=1)
            conn.commit
        conn.close()   


        #************** get cursor ===================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]        

        self.var_Dep.set(data(0)),
        self.var_Course.set(data(1)),
        self.var_Year.set(data(2)),
        self.var_Semester.set(data(3)),
        self.var_Std_Id.set(data(4)),
        self.var_Std_Name.set(data(5)),
        self.var_Div.set(data(6)),
        self.var_Roll.set(data(7)),
        self.var_Gender.set(data(8)),
        self.var_DOB.set(data(9)),
        self.var_Email.set(data(10)),
        self.var_Phone.set(data(11)),
        self.var_Address.set(data(12)),
        self.var_Teacher.set(data(13)),
        self.var_radio1.set(data(14))


        #''''''''''' update function ...........
    def update_data():
        if self.var_Dep.get()=="select Department" or self.var_Std_Name.get()=="" or self.var_Std_Id.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root) 
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="text@12345",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student details set Dep=%s,Course=%s,year=%s,semester=%s,Division=%s,Roll=%s,DOB=%s,phone=%s,Address=%s,teacher=%s,Department=%s,Email=%s,gemder=%s,photosample=%s where student_id=%s",(
                        
                                                                                                                                                                                                                                                                    self.var_Dep.get(),
                                                                                                                                                                                                                                                                    self.var_Course.get(),
                                                                                                                                                                                                                                                                    self.var_Year.get(),
                                                                                                                                                                                                                                                                    self.var_Semester(),
                                                                                                                                                                                                                                                                    self.var_Std_Name.get(),
                                                                                                                                                                                                                                                                    self.var_Div.get(),
                                                                                                                                                                                                                                                                    self.var_Roll.get(),
                                                                                                                                                                                                                                                                    self.var_Gender.get(),
                                                                                                                                                                                                                                                                    self.var_DOB.get(),
                                                                                                                                                                                                                                                                    self.var_Email.get(),
                                                                                                                                                                                                                                                                    self.var_Phone.get(),
                                                                                                                                                                                                                                                                    self.var_Address.get(),
                                                                                                                                                                                                                                                                    self.var_Teacher.get(),
                                                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                                                    self.var_Std_Id.get()
                                                                                                              
                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                 ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully update complete",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to{str(es)}",parent=self.root)

      #******************* delete function *********************
    def delete_data(self):
        if self.var_Std_Id.get()=="":
            messagebox.showerror('Error',"Student id must be required ",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","Do you want to delete this student ",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="text@12345",database="face_recognizer")
                    my_cursor=conn.cursor() 
                    sql="delete from student where student_id=%s"
                    val=(self.var_Std_Id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student",parent=self.root)    
            except Exception as es:
                messagebox.showerror("Error",f"Due to{str(es)}",parent=self.root)    
#Reset>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.............
    def reset_data(self):
        self.var_Dep.set("select Department")
        self.var_Course.set("select Course")
        self.var_Year.set("select Year")
        self.var_Semester.set("select semeter")
        self.var_Std_Id.set("")       
        self.var_Std_Name.set("")
        self.var_Div.set("select Division")
        self.var_Roll.set("")
        self.var_Gender.set("Male")
        self.var_DOB.set("")
        self.var_Email.set("")
        self.var_Phone.set("")
        self.var_Address.set("")
        self.var_Teacher.set("")
        self.var_radio1.set("")

        # Generate data set or take a sample ==============
    def Generate_dataset(self):
        if self.var_Dep.get()=="select Department" or self.var_Std_Name.get()=="" or self.var_Std_Id.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root) 

        else:
            try:

                conn=mysql.connector.connect(host="localhost",username="root",password="text@12345",database="face_recognizer-")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    my_cursor.execute("update student details set Dep=%s,Course=%s,year=%s,semester=%s,Division=%s,std_id=%s,std_Name=%s,Roll no=%s,DOB=%s,phone=%s,Address=%s,teacher=%s,Department=%s,Email=%s,gemder=%s,photosample=% where student_id=5s",(
                        
                                                                                                                                                                                                                                                                    self.var_Dep.get(),
                                                                                                                                                                                                                                                                    self.var_Course.get(),
                                                                                                                                                                                                                                                                    self.var_Year.get(),
                                                                                                                                                                                                                                                                    self.var_Semester(),
                                                                                                                                                                                                                                                                    self.var_Std_Name.get(),
                                                                                                                                                                                                                                                                    self.var_Div.get(),
                                                                                                                                                                                                                                                                    self.var_Roll.get(),
                                                                                                                                                                                                                                                                    self.var_Gender.get(),
                                                                                                                                                                                                                                                                    self.var_DOB.get(),
                                                                                                                                                                                                                                                                    self.var_Email.get(),
                                                                                                                                                                                                                                                                    self.var_Phone.get(),
                                                                                                                                                                                                                                                                    self.var_Address.get(),
                                                                                                                                                                                                                                                                    self.var_Teacher.get(),
                                                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                                                    self.var_Std_Id.get()==id+1
                                                                                                              
                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                 ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #............load predefined data on face frontal from open cv===========

                Face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def facce_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BAYER_BG2GRAY)
                    faces=Face_classifier.detectMultiScale(gray,1.3,5)

                    #1.3 scaling factor 
                    # 5 minimum Neighbour

                    for (x,y,w,h) in faces:
                        facce_cropped=img[y:y+h,x:x+w]
                        return facce_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myFrame=cap.read()
                    if facce_cropped(myFrame) is not None:
                        img_id+=1
                        face=cv2.resize(facce_cropped(myFrame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BAYER_BG2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completly !!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to{str(es)}",parent=self.root) 



              
if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
    