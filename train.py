from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
#import mysq.connector
import os
import numpy as np
import cv2

class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Train Data Set", font=("time new roman", 35, "bold"), bg="Blue", fg="yellow")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"Image_detail/third.jpg")
        img_top = img_top.resize((1530, 230), Image.AFFINE)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=5, y=55, width=1530, height=230)

        b1_1 = Button(self.root, text="TRAIN DATA", command=self.Train_Classifier, cursor="hand2", font=("time new roman", 35, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=5, y=290, width=1530, height=38)
         
        img_bottom = Image.open(r"Image_detail/background.jpg")
        img_bottom = img_bottom.resize((1530, 450), Image.AFFINE)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=5, y=330, width=1530, height=450)

    def Train_Classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        Ids = []

        for image in path:
            img = Image.open(image).convert('L') # gray scale image 
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp) 
            Ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        Ids = np.array(Ids)

        # train the classifier and save 
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, Ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets completed !!")

if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()