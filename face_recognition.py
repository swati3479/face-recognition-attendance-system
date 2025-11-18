from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
from config import ScreenConfig, SCREEN_CONFIG, HEADING_FONT_SIZE, BUTTON_FONT_SIZE, LABEL_FONT_SIZE, SMALL_FONT_SIZE


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        
        # Get responsive dimensions
        screen_w = SCREEN_CONFIG['screen_width']
        screen_h = SCREEN_CONFIG['screen_height']
        
        self.root.geometry(f"{screen_w}x{screen_h}+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="white")
        
        # Title
        title_height = ScreenConfig.scale_dimension(50)
        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE",
                         font=("Arial", HEADING_FONT_SIZE, "bold"), bg="white", fg="#003366")
        title_lbl.place(x=0, y=0, width=screen_w, height=title_height)
        
        # Image frame - divide screen into 2 equal parts
        remaining_height = screen_h - title_height
        image_frame_height = int(remaining_height * 0.65)  # 65% for images
        button_frame_height = remaining_height - image_frame_height  # 35% for button
        
        img_frame = Frame(self.root, bg="white")
        img_frame.place(x=0, y=title_height, width=screen_w, height=image_frame_height)
        
        # Left image
        left_img_width = screen_w // 2
        try:
            img_top = Image.open(r"college_images/face_detector1.jpg")
            img_top = img_top.resize((left_img_width, image_frame_height), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
            f_lbl = Label(img_frame, image=self.photoimg_top)
            f_lbl.place(x=0, y=0, width=left_img_width, height=image_frame_height)
        except Exception as e:
            print(f"Left image error: {e}")
            Label(img_frame, bg="lightgray").place(x=0, y=0, width=left_img_width, height=image_frame_height)
        
        # Right image
        right_img_width = screen_w - left_img_width
        try:
            img_bottom = Image.open(r"college_images/fcs.jpg")
            img_bottom = img_bottom.resize((right_img_width, image_frame_height), Image.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
            f_lbl2 = Label(img_frame, image=self.photoimg_bottom)
            f_lbl2.place(x=left_img_width, y=0, width=right_img_width, height=image_frame_height)
        except Exception as e:
            print(f"Right image error: {e}")
            Label(img_frame, bg="lightgray").place(x=left_img_width, y=0, width=right_img_width, height=image_frame_height)
        
        # Button frame
        btn_frame_y = title_height + image_frame_height
        btn_frame = Frame(self.root, bg="#f0f0f0")
        btn_frame.place(x=0, y=btn_frame_y, width=screen_w, height=button_frame_height)
        
        # Calculate button dimensions for proper centering
        button_width = ScreenConfig.scale_dimension(550)
        button_height = ScreenConfig.scale_dimension(80)
        button_x = (screen_w - button_width) // 2
        button_y = (button_frame_height - button_height) // 2
        
        # Start button
        b1_1 = Button(btn_frame,
                     text="START FACE RECOGNITION\n(Press ENTER to Exit)",
                     command=self.face_recog,
                     cursor="hand2",
                     font=("Arial", BUTTON_FONT_SIZE-2, "bold"),
                     bg="#006600", fg="white",
                     activebackground="#005500",
                     activeforeground="white",
                     bd=3,
                     relief=RAISED)
        b1_1.place(x=button_x, y=button_y, width=button_width, height=button_height)
        
        # Info label below button
        info_label = Label(btn_frame,
                          text="Face Recognition System - Real-time Attendance Marking",
                          font=("Arial", SMALL_FONT_SIZE, "italic"),
                          bg="#f0f0f0", fg="#666666")
        info_label.place(x=0, y=button_y + button_height + ScreenConfig.scale_dimension(5),
                        width=screen_w, height=ScreenConfig.scale_dimension(20))
    
    def mark_attendance(self, student_id, student_name, dep):
        try:
            file_exists = os.path.isfile("attendance.csv")
            now = datetime.now()
            today_date = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
        
            # Agar file pehli baar banti hai toh headers likho
            if not file_exists:
                with open("attendance.csv", "w", newline="") as f:
                    f.write("ID,Name,Department,Time,Date,Status\n")
        
            with open("attendance.csv", "r+") as f:
                lines = f.readlines()
                # Check if attendance already marked for student today
                already_marked = False
                for line in lines[1:]:  # Skip header line
                    if line.strip():
                        cols = line.strip().split(",")
                        if cols[0] == str(student_id) and cols[4] == today_date:
                            already_marked = True
                            break
            
                if not already_marked:
                    # Append new attendance entry
                    with open("attendance.csv", "a", newline="") as f:
                        f.write(f"{student_id},{student_name},{dep},{dtString},{today_date},Present\n")
                    print(f"Attendance marked for {student_name}")
                else:
                    print(f"Attendance already marked for {student_name} today.")
    
        except Exception as e:
            print(f"Attendance marking error: {e}")
    
    def face_recog(self):
        """Main face recognition function"""
        
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
    
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
                # Predict using classifier
                try:
                    id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                    confidence = int((100 * (1 - predict / 300)))
            
                    # Database se info fetch karo
                    try:
                        conn = mysql.connector.connect(
                            host="localhost",
                            username="root",
                            password="Test@123",
                            database="face_recognizer"
                        )
                        my_cursor = conn.cursor()
                
                        # Student info fetch karo
                        my_cursor.execute("SELECT student_id, student_name, department FROM student WHERE student_id = %s", (id,))
                        result = my_cursor.fetchone()
                
                        if result:
                            student_id = str(result[0])
                            student_name = str(result[1])
                            department = str(result[2])
                    
                            if confidence > 77:  # High confidence
                                # Green rectangle for recognized face
                                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                        
                                # Display info
                                cv2.putText(img, f"ID: {student_id}", (x, y-55), 
                                   cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                cv2.putText(img, f"Name: {student_name}", (x, y-30), 
                                   cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                cv2.putText(img, f"Dept: {department}", (x, y-5), 
                                   cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                cv2.putText(img, f"Conf: {confidence}%", (x, y+20), 
                                   cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
                        
                                # ✅ SAHI PARAMETERS
                                self.mark_attendance(student_id, student_name, department)
                            else:  # Low confidence
                                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                                cv2.putText(img, "UNKNOWN FACE", (x, y-5), 
                                   cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 3)
                                cv2.putText(img, f"Conf: {confidence}%", (x, y+20), 
                                   cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
                        else:
                            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                            cv2.putText(img, "ID NOT FOUND", (x, y-5), 
                                        cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 3)
                
                        conn.close()
                    except mysql.connector.Error as db_err:
                        print(f"Database error: {db_err}")
                        cv2.putText(img, "DB ERROR", (x, y-5), 
                                    cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                except Exception as e:
                    print(f"Recognition error: {e}")
    
            return img

        
        # Load cascade classifier aur trained model
        try:
            faceCascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            )
            
            clf = cv2.face.LBPHFaceRecognizer_create()
            
            # Check if classifier.xml exists
            if not os.path.exists("classifier.xml"):
                messagebox.showerror("Error", "classifier.xml not found! Please train the model first.")
                return
            
            clf.read("classifier.xml")
            
            # Video capture start karo
            video_cap = cv2.VideoCapture(0)
            
            if not video_cap.isOpened():
                messagebox.showerror("Error", "Camera not available!")
                return
            
            print("Face Recognition Started... Press ENTER to exit")
            
            while True:
                ret, img = video_cap.read()
                
                if not ret:
                    print("Failed to read frame")
                    break
                
                img = draw_boundary(img, faceCascade, 1.1, 10, clf)
                
                cv2.imshow("Face Recognition - Press ENTER to Exit", img)
                
                # ENTER key (13) dabao to exit
                if cv2.waitKey(1) == 13:
                    break
            
            video_cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Success", "Face Recognition Completed")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error in face recognition: {str(e)}")
            print(f"Face recognition error: {e}")


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()