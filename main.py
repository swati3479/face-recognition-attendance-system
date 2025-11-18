from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from time import strftime
from datetime import datetime
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from config import ScreenConfig, SCREEN_CONFIG, TITLE_FONT_SIZE, BUTTON_FONT_SIZE, LABEL_FONT_SIZE
import os

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        
        screen_w = SCREEN_CONFIG['screen_width']
        screen_h = SCREEN_CONFIG['screen_height']
        self.root.geometry(f"{screen_w}x{screen_h}+0+0")
        self.root.title("Face Recognition Attendance System")
        self.root.configure(bg="white")
        
        header_height = ScreenConfig.scale_dimension(120)
        content_height = screen_h - header_height
        header_width = screen_w // 3
        
        try:
            img = Image.open(r"college_images/face-recognition.png")
            img = img.resize((header_width, header_height), Image.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)
            f_lbl = Label(self.root, image=self.photoimg)
            f_lbl.place(x=0, y=0, width=header_width, height=header_height)
            
            img1 = Image.open(r"college_images/smart-attendance.jpg")
            img1 = img1.resize((header_width, header_height), Image.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)
            f_lbl1 = Label(self.root, image=self.photoimg1)
            f_lbl1.place(x=header_width, y=0, width=header_width, height=header_height)
            
            img2 = Image.open(r"college_images/classroom.jpg")
            img2 = img2.resize((header_width, header_height), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
            f_lbl2 = Label(self.root, image=self.photoimg2)
            f_lbl2.place(x=header_width*2, y=0, width=header_width, height=header_height)
            
            img_bg = Image.open(r"college_images/b2.jpg")
            img_bg = img_bg.resize((screen_w, content_height), Image.LANCZOS)
            self.photoimg_bg = ImageTk.PhotoImage(img_bg)
            bg_img = Label(self.root, image=self.photoimg_bg)
            bg_img.place(x=0, y=header_height, width=screen_w, height=content_height)
        except Exception as e:
            messagebox.showerror("Error", f"Image loading failed: {e}")
            bg_img = Label(self.root, bg="white")
            bg_img.place(x=0, y=header_height, width=screen_w, height=content_height)
        
        title_height = ScreenConfig.scale_dimension(50)
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM",
                         font=("Arial", TITLE_FONT_SIZE, "bold"), bg="white", fg="#003366")
        title_lbl.place(x=0, y=0, width=screen_w, height=title_height)
        
        # Time display
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        
        lbl = Label(title_lbl, font=('times new roman', 14, 'bold'), background='white', foreground='blue')
        lbl.place(x=0, y=0, width=100, height=40)
        time()
        
        # Button layout
        button_size = ScreenConfig.scale_dimension(160)
        button_text_height = ScreenConfig.scale_dimension(40)
        button_total_height = button_size + button_text_height
        
        cols = 3
        rows = 2
        
        total_button_width = button_size * cols
        total_button_height = button_total_height * rows
        
        total_h_spacing = screen_w - total_button_width
        space_between_buttons_x = total_h_spacing // (cols + 1)
        
        available_content_height = content_height - title_height
        total_v_spacing = available_content_height - total_button_height
        space_between_buttons_y = total_v_spacing // (rows + 1)
        
        button_images_paths = [
            r"college_images/student-portal_1.jpg",
            r"college_images/face_detector1.jpg",
            r"college_images/AdobeStock_303989091.jpeg",
            r"college_images/Train.jpg",
            r"college_images/photos.jpg",
            r"college_images/exit.jpg"
        ]
        
        buttons_config = [
            ("STUDENT\nDETAILS", self.student_details),
            ("FACE\nRECOGNITION", self.face_data),
            ("ATTENDANCE", self.attendance_data),
            ("TRAIN\nDATA", self.train_data),
            ("PHOTOS", self.open_img),
            ("EXIT", self.exit_data)
        ]
        
        self.button_images = []
        
        for idx, (text, cmd) in enumerate(buttons_config):
            row = idx // cols
            col = idx % cols
            
            x = space_between_buttons_x + col * (button_size + space_between_buttons_x)
            y = title_height + space_between_buttons_y + row * (button_total_height + space_between_buttons_y)
            
            try:
                img_b = Image.open(button_images_paths[idx])
                img_b = img_b.resize((button_size, button_size), Image.LANCZOS)
                photoimg_b = ImageTk.PhotoImage(img_b)
                self.button_images.append(photoimg_b)
                
                b = Button(bg_img, image=photoimg_b, command=cmd, cursor="hand2",
                          bd=2, relief=RAISED, bg="lightgray")
                b.place(x=x, y=y, width=button_size, height=button_size)
                
                b_lbl = Button(bg_img, text=text, cursor="hand2", command=cmd,
                              font=("Arial", max(BUTTON_FONT_SIZE - 6, 10), "bold"),
                              bg="#003366", fg="white")
                b_lbl.place(x=x, y=y + button_size, width=button_size, height=button_text_height)
            except Exception as e:
                print(f"Button image load failed: {e}")
                b = Button(bg_img, text=text, cursor="hand2", command=cmd,
                          font=("Arial", LABEL_FONT_SIZE, "bold"),
                          bg="#003366", fg="white")
                b.place(x=x, y=y, width=button_size, height=button_total_height)
    
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def open_img(self):
        try:
            if os.path.exists("data"):
                os.startfile("data")
            else:
                messagebox.showerror("Error", "Data folder nahi hai!", parent=self.root)
        except:
            messagebox.showerror("Error", "Data folder nahi khul raha!", parent=self.root)
    
    def exit_data(self):
        result = tkinter.messagebox.askyesno("Exit", "Do you want to exit?", parent=self.root)
        if result:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
    
    
