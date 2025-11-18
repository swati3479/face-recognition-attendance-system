from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np
from config import ScreenConfig, SCREEN_CONFIG, HEADING_FONT_SIZE, BUTTON_FONT_SIZE

class Train:
    def __init__(self, root):
        self.root = root
        
        # Get responsive dimensions
        screen_w = SCREEN_CONFIG['screen_width']
        screen_h = SCREEN_CONFIG['screen_height']
        
        self.root.geometry(f"{screen_w}x{screen_h}+0+0")
        self.root.title("Train Dataset")
        self.root.configure(bg="white")
        
        # Title
        title_height = ScreenConfig.scale_dimension(45)
        title_lbl = Label(self.root, text="TRAIN DATASET",
                         font=("Arial", HEADING_FONT_SIZE, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=screen_w, height=title_height)
        
        # Top image
        try:
            img_top = Image.open(r"college_images/facialrecognition.png")
            img_top = img_top.resize((screen_w, ScreenConfig.scale_dimension(280)), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
            f_lbl = Label(self.root, image=self.photoimg_top)
            f_lbl.place(x=0, y=title_height, width=screen_w, height=ScreenConfig.scale_dimension(280))
        except:
            pass
        
        # Button
        button_y = title_height + ScreenConfig.scale_dimension(280) + ScreenConfig.scale_dimension(15)
        button_width = ScreenConfig.scale_dimension(500)
        button_height = ScreenConfig.scale_dimension(45)
        button_x = (screen_w - button_width) // 2
        
        b1_1 = Button(self.root, command=self.train_classifier, text="TRAIN DATASET",
                     cursor="hand2", font=("Arial", BUTTON_FONT_SIZE, "bold"),
                     bg="#006600", fg="white")
        b1_1.place(x=button_x, y=button_y, width=button_width, height=button_height)
        
        # Bottom image
        try:
            bottom_y = button_y + button_height + ScreenConfig.scale_dimension(15)
            bottom_height = screen_h - bottom_y
            
            img_bottom = Image.open(r"college_images/photos.jpg")
            img_bottom = img_bottom.resize((screen_w, bottom_height), Image.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
            f_lbl = Label(self.root, image=self.photoimg_bottom)
            f_lbl.place(x=0, y=bottom_y, width=screen_w, height=bottom_height)
        except:
            pass
    
    def train_classifier(self):
        data_dir = "data"
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            
        faces = []
        ids = []
            
        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        print(ids)
            
        # Train classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
            
        cv2.destroyAllWindows()
            
        messagebox.showinfo("Result","Training datasets completed!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()