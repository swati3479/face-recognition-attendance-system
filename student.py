from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import glob
import numpy as np
from config import ScreenConfig, SCREEN_CONFIG, TITLE_FONT_SIZE, BUTTON_FONT_SIZE, LABEL_FONT_SIZE


class Student:
    def __init__(self, root):
        self.root = root
        
        # Get screen dimensions dynamically
        screen_w = SCREEN_CONFIG['screen_width']
        screen_h = SCREEN_CONFIG['screen_height']
        
        # Set geometry responsively
        self.root.geometry(f"{screen_w}x{screen_h}+0+0")
        self.root.title("face Recognition System")
        
        # Calculate responsive dimensions
        header_height = ScreenConfig.scale_dimension(130)
        content_height = screen_h - header_height
        
        # Divide screen into 3 equal header sections
        header_width = screen_w // 3
        
        # Variables
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_sem = StringVar()
        self.var_regd = StringVar()
        self.var_radio1 = StringVar(value="no")  # ✅ DEFAULT VALUE SET KAR DI
        
        # Load and resize header images
        try:
            img = Image.open("college_images/img1.jpeg")
            img = img.resize((header_width, header_height), Image.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)
            f_lbl = Label(self.root, image=self.photoimg)
            f_lbl.place(x=0, y=0, width=header_width, height=header_height)
            
            img1 = Image.open("college_images/img2.jpg")
            img1 = img1.resize((header_width, header_height), Image.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)
            f_lbl = Label(self.root, image=self.photoimg1)
            f_lbl.place(x=header_width, y=0, width=header_width, height=header_height)
            
            img2 = Image.open("college_images/img3.jpeg")
            img2 = img2.resize((header_width, header_height), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
            f_lbl = Label(self.root, image=self.photoimg2)
            f_lbl.place(x=header_width*2, y=0, width=header_width, height=header_height)
        except Exception as e:
            messagebox.showerror("Error", f"Header images loading failed: {e}")
        
        # Background image
        try:
            img3 = Image.open("college_images/b2.jpg")
            img3 = img3.resize((screen_w, content_height), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)
            bg_img = Label(self.root, image=self.photoimg3)
            bg_img.place(x=0, y=header_height, width=screen_w, height=content_height)
        except Exception as e:
            messagebox.showerror("Error", f"Background image loading failed: {e}")
            bg_img = Label(self.root, bg="white")
            bg_img.place(x=0, y=header_height, width=screen_w, height=content_height)
        
        # Title label
        title_height = ScreenConfig.scale_dimension(45)
        title_lbl = Label(bg_img, text="STUDENT DETAILS", font=("times new roman", TITLE_FONT_SIZE, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=screen_w, height=title_height)
        
        # Calculate responsive main frame dimensions
        main_frame_margin = ScreenConfig.scale_dimension(10)
        main_frame_width = screen_w - (main_frame_margin * 2)
        main_frame_height = content_height - title_height - main_frame_margin
        
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=main_frame_margin, y=title_height + main_frame_margin, width=main_frame_width, height=main_frame_height)
        
        # Calculate left and right frame dimensions
        left_frame_width = (main_frame_width - ScreenConfig.scale_dimension(15)) // 2
        right_frame_width = left_frame_width
        frame_height = main_frame_height - ScreenConfig.scale_dimension(20)
        
        # Left frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student details", font=("times new roman", LABEL_FONT_SIZE, "bold"))
        Left_frame.place(x=ScreenConfig.scale_dimension(10), y=ScreenConfig.scale_dimension(10), width=left_frame_width, height=frame_height)
        
        # Left frame header image
        try:
            img_left = Image.open("college_images/std.jpg")
            img_left_width = left_frame_width - ScreenConfig.scale_dimension(10)
            img_left_height = ScreenConfig.scale_dimension(150)
            img_left = img_left.resize((img_left_width, img_left_height), Image.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)
            f_lbl = Label(Left_frame, image=self.photoimg_left)
            f_lbl.place(x=ScreenConfig.scale_dimension(5), y=0, width=img_left_width, height=img_left_height)
        except Exception as e:
            messagebox.showerror("Error", f"Left frame image loading failed: {e}")
        
        # Responsive label and entry styling
        label_font_size = LABEL_FONT_SIZE
        entry_width = 20
        
        class_student_frame_height = ScreenConfig.scale_dimension(320)
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("times new roman", LABEL_FONT_SIZE, "bold"))
        class_student_frame.place(x=ScreenConfig.scale_dimension(5), y=ScreenConfig.scale_dimension(150), width=right_frame_width - ScreenConfig.scale_dimension(10), height=class_student_frame_height)

        
        # Student ID
        studentId_label = Label(class_student_frame, text="STUDENT ID:", font=("times new roman", label_font_size, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=ScreenConfig.scale_dimension(10), pady=ScreenConfig.scale_dimension(6), sticky=W)
        
        studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_id, width=entry_width, font=("times new roman", label_font_size, "bold"))
        studentId_entry.grid(row=0, column=1, padx=ScreenConfig.scale_dimension(10), pady=ScreenConfig.scale_dimension(6), sticky=W)
        
        # Student Name
        studentName_label = Label(class_student_frame, text="STUDENT NAME:", font=("times new roman", label_font_size, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=ScreenConfig.scale_dimension(10), pady=ScreenConfig.scale_dimension(6), sticky=W)
        
        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_name, width=entry_width, font=("times new roman", label_font_size, "bold"))
        studentName_entry.grid(row=0, column=3, padx=ScreenConfig.scale_dimension(10), pady=ScreenConfig.scale_dimension(6), sticky=W)
        
        # Department
        dep_label = Label(class_student_frame, text="DEPARTMENT:", font=("times new roman", label_font_size, "bold"), bg="white")
        dep_label.grid(row=1, column=0, padx=ScreenConfig.scale_dimension(10), pady=ScreenConfig.scale_dimension(6), sticky=W)
        
        dep_entry = ttk.Entry(class_student_frame, textvariable=self.var_dep, width=entry_width, font=("times new roman", label_font_size, "bold"))
        dep_entry.grid(row=1, column=1, padx=ScreenConfig.scale_dimension(10), pady=ScreenConfig.scale_dimension(6), sticky=W)
        
        # Semester
        semester_label = Label(class_student_frame, text="SEMESTER:", font=("times new roman", label_font_size, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=ScreenConfig.scale_dimension(10), pady=ScreenConfig.scale_dimension(6), sticky=W)
        
        semester_entry = ttk.Entry(class_student_frame, textvariable=self.var_sem, width=entry_width, font=("times new roman", label_font_size, "bold"))
        semester_entry.grid(row=1, column=3, padx=ScreenConfig.scale_dimension(10), pady=ScreenConfig.scale_dimension(6), sticky=W)
        
        # Radio buttons for photo sample
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take photo sample", value="yes")
        radiobtn1.grid(row=2, column=0)
        
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No photo sample", value="no")
        radiobtn2.grid(row=2, column=1)
        
        # Button frame - Attendance style buttons
        btn_frame_height = ScreenConfig.scale_dimension(30)
        btn_frame = Frame(class_student_frame, bd=1, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=ScreenConfig.scale_dimension(225), width=left_frame_width-1, height=btn_frame_height)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=12, font=("Arial", LABEL_FONT_SIZE, "bold"), bg="#28a745", fg="white", cursor="hand2")
        save_btn.grid(row=0, column=0, padx=2)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=12, font=("Arial", LABEL_FONT_SIZE, "bold"), bg="#ffc107", fg="black", cursor="hand2")
        update_btn.grid(row=0, column=1, padx=2)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=12, font=("Arial", LABEL_FONT_SIZE, "bold"), bg="#CC0000", fg="white", cursor="hand2")
        delete_btn.grid(row=0, column=2, padx=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=12, font=("Arial", LABEL_FONT_SIZE, "bold"), bg="#0066CC", fg="white", cursor="hand2")
        reset_btn.grid(row=0, column=3, padx=2)

        # Button frame 2 - Photo button only (update photo button removed)
        btn_frame1_height = ScreenConfig.scale_dimension(30)
        btn_frame1 = Frame(class_student_frame, bd=1, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=ScreenConfig.scale_dimension(260), width=left_frame_width, height=btn_frame1_height)

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Add Photo Sample", width=20, font=("Arial", LABEL_FONT_SIZE, "bold"), bg="#0066CC", fg="white", cursor="hand2")
        take_photo_btn.grid(row=0, column=0, padx=2)

        # Right frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student details", font=("times new roman", LABEL_FONT_SIZE, "bold"))
        Right_frame.place(x=left_frame_width + ScreenConfig.scale_dimension(20), y=ScreenConfig.scale_dimension(10), width=right_frame_width, height=frame_height)
        
        # Right frame header image
        try:
            img_right = Image.open("college_images/img4.jpg")
            img_right_width = right_frame_width - ScreenConfig.scale_dimension(10)
            img_right_height = ScreenConfig.scale_dimension(150)
            img_right = img_right.resize((img_right_width, img_right_height), Image.LANCZOS)
            self.photoimg_right = ImageTk.PhotoImage(img_right)
            f_lbl = Label(Right_frame, image=self.photoimg_right)
            f_lbl.place(x=ScreenConfig.scale_dimension(5), y=0, width=img_right_width, height=img_right_height)
        except Exception as e:
            messagebox.showerror("Error", f"Right frame image loading failed: {e}")
        
        # Search frame
        search_frame_height = ScreenConfig.scale_dimension(70)
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search system", font=("times new roman", LABEL_FONT_SIZE, "bold"))
        Search_frame.place(x=ScreenConfig.scale_dimension(5), y=ScreenConfig.scale_dimension(150), width=right_frame_width - ScreenConfig.scale_dimension(10), height=search_frame_height)
        
        search_label = Label(Search_frame, text="Search by", font=("times new roman", label_font_size, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=ScreenConfig.scale_dimension(10), sticky=W)
        
        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 11, "bold"), state="readonly", width=10)
        search_combo["values"] = ("select", "student id", "name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=ScreenConfig.scale_dimension(10), sticky=W)
        
        search_entry = ttk.Entry(Search_frame, width=10, font=("times new roman", 11, "bold"))
        search_entry.grid(row=0, column=2, padx=ScreenConfig.scale_dimension(10), pady=ScreenConfig.scale_dimension(5), sticky=W)
        
        search_btn = Button(Search_frame, text="Search", width=10, font=("times new roman", 11, "bold"), bg="blue", fg="white", cursor="hand2")
        search_btn.grid(row=0, column=3, padx=4)
        
        showAll_btn = Button(Search_frame, text="Show All", width=10, font=("times new roman", 11, "bold"), bg="blue", fg="white", cursor="hand2")
        showAll_btn.grid(row=0, column=4, padx=4)
        
        # Table frame
        table_frame_height = frame_height - search_frame_height - ScreenConfig.scale_dimension(170)
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=ScreenConfig.scale_dimension(5), y=ScreenConfig.scale_dimension(210), width=right_frame_width - ScreenConfig.scale_dimension(10), height=table_frame_height)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        # Treeview configuration ko fix karo - pehle wale code mein
        self.student_table = ttk.Treeview(table_frame, column=("id","name","dep","sem", "photosample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # ✅ FIXED: Properly configure column #0 (hidden index column)
        self.student_table.column("#0", width=0, stretch=NO)  # ✅ ADD YEH LINE

        self.student_table.heading("id", text="Student_Id")
        self.student_table.heading("name", text="Student_Name")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("photosample", text="Photo Sample")

        self.student_table["show"] = "headings"

        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("dep", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("photosample", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)  # ✅ BIND THEEK HAI
        self.fetch_data()

    
    # ✅ DATABASE CONNECTION HELPER FUNCTION - CENTRALIZED
    def get_db_connection(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Test@123",
                database="face_recognizer"
            )
            return conn
        except Exception as e:
            messagebox.showerror("Database Error", f"Connection failed: {str(e)}", parent=self.root)
            return None
    
    def add_data(self):
        if self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error!", "All fields are required", parent=self.root)
        else:
            try:
                conn = self.get_db_connection()  # ✅ USE HELPER FUNCTION
                if conn is None:
                    return
                
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s)", (
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_dep.get(),
                    self.var_sem.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success", "student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)
    
    def fetch_data(self):
        try:
            conn = self.get_db_connection()  # ✅ USE HELPER FUNCTION
            if conn is None:
                return
            
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            data = my_cursor.fetchall()
            
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
            
            conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Fetch data failed: {str(es)}", parent=self.root)
    
    def get_cursor(self, event=""):
        try:
            cursor_focus = self.student_table.focus()
        
            # ✅ Check if something is actually selected
            if not cursor_focus:
                messagebox.showwarning("Warning", "Please select a row from the table", parent=self.root)
                return
        
            content = self.student_table.item(cursor_focus)
            data = content["values"]
        
            # ✅ Check if data exists aur valid hai
            if len(data) == 0:
                messagebox.showwarning("Warning", "No data found in selected row", parent=self.root)
                return
        
            # ✅ Properly set all values
            print(f"DEBUG: Selected data = {data}")  # Debugging ke liye
        
            self.var_id.set(data[0])
            self.var_name.set(data[1])
            self.var_dep.set(data[2])
            self.var_sem.set(data[3])
            self.var_radio1.set(data[4])
        
            print(f"DEBUG: var_id = {self.var_id.get()}")  # Debugging ke liye
        
        except IndexError as e:
            messagebox.showerror("Error", f"Data indexing error: {str(e)}", parent=self.root)

    
    def update_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error!", "Please select a student first or enter Student ID", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("update", "Do you want to update this student details?", parent=self.root)
                if update > 0:
                    conn = self.get_db_connection()
                    if conn is None:
                        return
                
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set student_name=%s, department=%s, semester=%s, photosample=%s where student_id=%s", (
                        self.var_name.get(),
                        self.var_dep.get(),
                        self.var_sem.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                
                    affected_rows = my_cursor.rowcount  # ✅ Check if update happened
                    print(f"DEBUG: Affected rows = {affected_rows}")
                
                    if affected_rows == 0:
                        messagebox.showwarning("Warning", "No student found with this ID", parent=self.root)
                        conn.close()
                        return
                
                    conn.commit()
                    conn.close()
                    self.fetch_data()  # ✅ Refresh table
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                    self.reset_data()
                
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Please select a student first or enter Student ID", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?", parent=self.root)
                if delete:
                    conn = self.get_db_connection()
                    if conn is None:
                        return

                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)

                    affected_rows = my_cursor.rowcount
                    if affected_rows == 0:
                        messagebox.showwarning("Warning", "No student found with this ID", parent=self.root)
                        conn.close()
                        return

                    conn.commit()
                    conn.close()
                    self.fetch_data()

                    # --- DELETE PHOTOS LOGIC ---
                    student_id = self.var_id.get()
                    pattern = f"data/user.{student_id}.*.jpg"
                    image_files = glob.glob(pattern)
                    for f in image_files:
                        try:
                            os.remove(f)
                        except Exception as img_err:
                            print(f"ERROR deleting {f}: {img_err}")

                    messagebox.showinfo("Delete", "Successfully deleted student details and photos", parent=self.root)
                    self.reset_data()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_sem.set("")
        self.var_radio1.set("no")  # ✅ RESET TO DEFAULT VALUE
    
    # Generate data set Take Photo Samples
    def generate_dataset(self):
        # ✅ FIXED: Added .get() to all StringVar() objects
        if (self.var_id.get() == "" or self.var_name.get() == "" or 
            self.var_dep.get() == "" or self.var_sem.get() == "" or 
            self.var_radio1.get() == ""):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = self.get_db_connection()  # ✅ USE HELPER FUNCTION
                if conn is None:
                    return
                
                my_cursor = conn.cursor()
                
                # ✅ FIXED: Use student ID directly, don't count all records
                id = int(self.var_id.get())
                
                # Update student record
                my_cursor.execute("update student set student_name=%s, department=%s, semester=%s, photosample=%s where student_id=%s", (
                    self.var_name.get(),
                    self.var_dep.get(),
                    self.var_sem.get(),
                    self.var_radio1.get(),
                    self.var_id.get()
                ))
                
                conn.commit()
                self.fetch_data()  # ✅ REFRESH TABLE IMMEDIATELY
                self.reset_data()
                conn.close()
                
                # Haarcascade classifier
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    return None  # ✅ RETURN None explicitly if no face found
                
                cap = cv2.VideoCapture(0)
                img_id = 0
                
                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        break
                    
                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                    
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:  # 13 is Enter key
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()