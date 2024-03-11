from tkinter import*
from tkinter import ttk
from sys import path
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2
from time import strftime
from datetime import datetime





class Face_Recogntion:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogintion System")

        title_lbl=Label(self.root,text="Face_Recognition",font=("time new roman",35,"bold"),bg="White",fg="Blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #   first image 
        img_top=Image.open(r"Image_detail/third.jpg")
        img_top=img_top.resize((700,700),Image.AFFINE)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=5,y=55,width=700,height=700)

        #second image 

        img_bottom=Image.open(r"Image_detail/background.jpg")
        img_bottom=img_bottom.resize((790,700),Image.AFFINE)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=710,y=55,width=790,height=700)

        #button

        b1_1=Button(f_lbl,text="FACE RECOGNITION",command=self.Face_Recogs,font=("time new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=350,y=550,width=300,height=38)


        #================= Attendance ==============
    def mark_attendance(self,i,r,n,d):
        with open("rakesh.csv","r+",newline="\n")as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.splitd((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                 now=datetime.now()
                 d1=now.strftime("%d/%m/%Y")
                 dtString=now.strftime("%H:%M:%S")
                 f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")







        #================== face Recognition==========
    def Face_Recogs(self):
        def draw_boundary(img,classifier,scalefactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbours)

            coord=[]
            conn=mysql.connector.connect(host="localhost",username="root",password="text@12345",database="face_recognizer")
            my_cursor=conn.cursor()

            for (x,y,w,h) in features:
                cv2.rectangle(img(x,y)(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

              

                my_cursor.execute("Select student_name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("Select Roll no from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("Select Dep from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("Select Student_Id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                

                if confidence>77:
                    
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"student_Nmae:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img(x,y)(x+w,y+h),(0,0,255),3)

                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord=[x,y,w,h]
            return coord

        def recongnize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,55,255),"face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizier_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret, img=video_cap.read()
            img=recongnize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__== "__main__":
    root=Tk()
    obj=Face_Recogntion(root)
    root.mainloop()    