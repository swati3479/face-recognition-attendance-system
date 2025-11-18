from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv
from tkinter import filedialog
import os
from config import ScreenConfig, SCREEN_CONFIG, HEADING_FONT_SIZE, LABEL_FONT_SIZE, ENTRY_FONT_SIZE, SMALL_FONT_SIZE

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        
        # Get responsive dimensions
        screen_w = SCREEN_CONFIG['screen_width']
        screen_h = SCREEN_CONFIG['screen_height']
        
        self.root.geometry(f"{screen_w}x{screen_h}+0+0")
        self.root.title("Attendance Management System")
        self.root.configure(bg="white")
        
        # Variables
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        
        # Responsive dimensions
        header_height = ScreenConfig.scale_dimension(80)
        header_width = screen_w // 2
        content_height = screen_h - header_height
        title_height = ScreenConfig.scale_dimension(35)
        
        try:
            # Header images
            img = Image.open(r"college_images/smart-attendance.jpg")
            img = img.resize((header_width, header_height), Image.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)
            f_lbl = Label(self.root, image=self.photoimg)
            f_lbl.place(x=0, y=0, width=header_width, height=header_height)
            
            img1 = Image.open(r"college_images/classroom.jpg")
            img1 = img1.resize((header_width, header_height), Image.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)
            f_lbl = Label(self.root, image=self.photoimg1)
            f_lbl.place(x=header_width, y=0, width=header_width, height=header_height)
            
            # Background
            img_bg = Image.open(r"college_images/b3.jpg")
            img_bg = img_bg.resize((screen_w, content_height), Image.LANCZOS)
            self.photoimg_bg = ImageTk.PhotoImage(img_bg)
            bg_img = Label(self.root, image=self.photoimg_bg)
            bg_img.place(x=0, y=header_height, width=screen_w, height=content_height)
            
            # Title
            title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM",
                            font=("Arial", HEADING_FONT_SIZE, "bold"), bg="white", fg="#006600")
            title_lbl.place(x=0, y=0, width=screen_w, height=title_height)
            
            # Main frame
            main_frame_height = content_height - title_height
            main_frame = Frame(bg_img, bd=1, bg="white")
            main_frame.place(x=ScreenConfig.scale_dimension(8),
                           y=ScreenConfig.scale_dimension(38),
                           width=screen_w-ScreenConfig.scale_dimension(16),
                           height=main_frame_height-ScreenConfig.scale_dimension(20))
            
            # Left frame
            left_width = int(screen_w * 0.49)
            Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Student Attendance Details", font=("Arial", LABEL_FONT_SIZE, "bold"))
            Left_frame.place(x=ScreenConfig.scale_dimension(5),
                           y=ScreenConfig.scale_dimension(5),
                           width=left_width-ScreenConfig.scale_dimension(10),
                           height=main_frame_height-ScreenConfig.scale_dimension(50))
            
            # Left inside frame
            left_inside_frame = Frame(Left_frame, bd=1, relief=RIDGE, bg="white")
            left_inside_frame.place(x=ScreenConfig.scale_dimension(5),
                                  y=ScreenConfig.scale_dimension(5),
                                  width=left_width-ScreenConfig.scale_dimension(20),
                                  height=ScreenConfig.scale_dimension(360))
            
            # Attendance ID
            attendanceID_label = Label(left_inside_frame, text="Student ID:",
                                     font=("Arial", SMALL_FONT_SIZE, "bold"), bg="white")
            attendanceID_label.grid(row=0, column=0, padx=6, pady=5, sticky=W)
            attendanceID_entry = ttk.Entry(left_inside_frame, width=13,
                                         textvariable=self.var_atten_id,
                                         font=("Arial", SMALL_FONT_SIZE))
            attendanceID_entry.grid(row=0, column=1, padx=6, pady=5, sticky=W)
            
            # Name
            name_label = Label(left_inside_frame, text="Student Name:",
                             font=("Arial", SMALL_FONT_SIZE, "bold"), bg="white")
            name_label.grid(row=0, column=2, padx=6, pady=5, sticky=W)
            name_entry = ttk.Entry(left_inside_frame, width=13,
                                 textvariable=self.var_atten_name,
                                 font=("Arial", SMALL_FONT_SIZE))
            name_entry.grid(row=0, column=3, padx=6, pady=5, sticky=W)
            
            # Department
            dep_label = Label(left_inside_frame, text="Department:",
                             font=("Arial", SMALL_FONT_SIZE, "bold"), bg="white")
            dep_label.grid(row=1, column=0, padx=6, pady=5, sticky=W)
            dep_entry = ttk.Entry(left_inside_frame, width=13,
                                 textvariable=self.var_atten_dep,
                                 font=("Arial", SMALL_FONT_SIZE))
            dep_entry.grid(row=1, column=1, padx=6, pady=5, sticky=W)
            

            # Time
            time_label = Label(left_inside_frame, text="Time:",
                             font=("Arial", SMALL_FONT_SIZE, "bold"), bg="white")
            time_label.grid(row=1, column=2, padx=6, pady=5, sticky=W)
            time_entry = ttk.Entry(left_inside_frame, width=13,
                                 textvariable=self.var_atten_time,
                                 font=("Arial", SMALL_FONT_SIZE))
            time_entry.grid(row=1, column=3, padx=6, pady=5, sticky=W)
            
            # Date
            date_label = Label(left_inside_frame, text="Date:",
                             font=("Arial", SMALL_FONT_SIZE, "bold"), bg="white")
            date_label.grid(row=2, column=0, padx=6, pady=5, sticky=W)
            date_entry = ttk.Entry(left_inside_frame, width=13,
                                 textvariable=self.var_atten_date,
                                 font=("Arial", SMALL_FONT_SIZE))
            date_entry.grid(row=2, column=1, padx=6, pady=5, sticky=W)
            
            # Attendance Status
            attendance_label = Label(left_inside_frame, text="Attendance Status:",
                                   font=("Arial", SMALL_FONT_SIZE, "bold"), bg="white")
            attendance_label.grid(row=2, column=2, padx=6, pady=5, sticky=W)
            self.atten_status = ttk.Combobox(left_inside_frame, width=11,
                                            textvariable=self.var_atten_attendance,
                                            font=("Arial", SMALL_FONT_SIZE), state="readonly")
            self.atten_status["values"] = ("Status", "Present", "Absent")
            self.atten_status.current(0)
            self.atten_status.grid(row=2, column=3, padx=6, pady=5, sticky=W)
            
            # Button frame
            btn_frame = Frame(Left_frame, bd=1, relief=RIDGE, bg="white")
            btn_frame.place(x=ScreenConfig.scale_dimension(5),
                          y=ScreenConfig.scale_dimension(370),
                          width=left_width-ScreenConfig.scale_dimension(20),
                          height=ScreenConfig.scale_dimension(30))
            
            import_btn = Button(btn_frame, text="Import CSV", command=self.importCsv,
                              width=12, font=("Arial", SMALL_FONT_SIZE, "bold"),
                              bg="#0066CC", fg="white", cursor="hand2")
            import_btn.grid(row=0, column=0, padx=2)
            
            export_btn = Button(btn_frame, text="Export CSV", command=self.exportCsv,
                              width=12, font=("Arial", SMALL_FONT_SIZE, "bold"),
                              bg="#0066CC", fg="white", cursor="hand2")
            export_btn.grid(row=0, column=1, padx=2)
            
            reset_btn = Button(btn_frame, text="Reset", command=self.reset_data,
                             width=12, font=("Arial", SMALL_FONT_SIZE, "bold"),
                             bg="#0066CC", fg="white", cursor="hand2")
            reset_btn.grid(row=0, column=2, padx=2)
            
            delete_btn = Button(btn_frame, text="Delete", command=self.delete_record,
                              width=12, font=("Arial", SMALL_FONT_SIZE, "bold"),
                              bg="#CC0000", fg="white", cursor="hand2")
            delete_btn.grid(row=0, column=3, padx=2)
            
            save_btn = Button(btn_frame, text="Add", command=self.add_data,
                  width=12, font=("Arial", SMALL_FONT_SIZE, "bold"),
                  bg="#28a745", fg="white", cursor="hand2")
            save_btn.grid(row=0, column=4, padx=2)

            update_btn = Button(btn_frame, text="Update", command=self.update_data,
                    width=12, font=("Arial", SMALL_FONT_SIZE, "bold"),
                    bg="#ffc107", fg="black", cursor="hand2")
            update_btn.grid(row=0, column=5, padx=2)

            
            # Right frame
            right_width = int(screen_w * 0.49)
            Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                   text="Attendance Records", font=("Arial", LABEL_FONT_SIZE, "bold"))
            Right_frame.place(x=left_width,
                            y=ScreenConfig.scale_dimension(5),
                            width=right_width-ScreenConfig.scale_dimension(10),
                            height=main_frame_height-ScreenConfig.scale_dimension(50))
            
            # Table frame
            table_frame = Frame(Right_frame, bd=1, relief=RIDGE, bg="white")
            table_frame.place(x=ScreenConfig.scale_dimension(5),
                            y=ScreenConfig.scale_dimension(5),
                            width=right_width-ScreenConfig.scale_dimension(20),
                            height=main_frame_height-ScreenConfig.scale_dimension(60))
            
            # Scroll bars
            scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
            
            self.AttendanceReportTable = ttk.Treeview(table_frame,
                                                     column=("id","name", "dep",
                                                           "time", "date", "attendance"),
                                                     xscrollcommand=scroll_x.set,
                                                     yscrollcommand=scroll_y.set)
            
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            
            scroll_x.config(command=self.AttendanceReportTable.xview)
            scroll_y.config(command=self.AttendanceReportTable.yview)
            
            self.AttendanceReportTable.heading("id", text="ID")
            self.AttendanceReportTable.heading("name", text="Name")
            self.AttendanceReportTable.heading("dep", text="Department")
            self.AttendanceReportTable.heading("time", text="Time")
            self.AttendanceReportTable.heading("date", text="Date")
            self.AttendanceReportTable.heading("attendance", text="Status")
            
            self.AttendanceReportTable["show"] = "headings"
            
            self.AttendanceReportTable.column("id", width=100)
            self.AttendanceReportTable.column("name", width=150)
            self.AttendanceReportTable.column("dep", width=120)
            self.AttendanceReportTable.column("time", width=80)
            self.AttendanceReportTable.column("date", width=100)
            self.AttendanceReportTable.column("attendance", width=80)
            
            self.AttendanceReportTable.pack(fill=BOTH, expand=1)
            self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
            
        except Exception as e:
            messagebox.showerror("Error", f"Initialization error: {e}")
    
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)
    
    def importCsv(self):
        global mydata
        mydata.clear()
        
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="Open CSV",
                                        filetypes=(("CSV File", "*.csv"),
                                                  ("All Files", "*.*")),
                                        parent=self.root)
        try:
            with open(fln) as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    mydata.append(i)
            
            self.fetchData(mydata)
            messagebox.showinfo("Success", "CSV import successful!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)
    
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "Koi data nahi hai!", parent=self.root)
                return False
            
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                             title="Save CSV",
                                             filetypes=(("CSV File", "*.csv"),
                                                       ("All Files", "*.*")),
                                             parent=self.root)
            
            with open(fln, mode='w', newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
            
            messagebox.showinfo("Success", f"Export complete!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)
    
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        
        if rows:
            self.var_atten_id.set(rows[0])
            self.var_atten_name.set(rows[1])
            self.var_atten_dep.set(rows[2])
            self.var_atten_time.set(rows[3])
            self.var_atten_date.set(rows[4])
            self.var_atten_attendance.set(rows[5])
    
    def delete_record(self):
        if self.var_atten_id.get() == "":
            messagebox.showerror("Error", "Record select karo!", parent=self.root)
        else:
            global mydata
            for i in mydata:
                if i[0] == self.var_atten_id.get():
                    mydata.remove(i)
            
            self.fetchData(mydata)
            messagebox.showinfo("Success", "Record delete ho gaya!", parent=self.root)
            self.reset_data()
    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")
        
    def add_data(self):
        if self.var_atten_id.get() == "" or self.var_atten_name.get() == "" or self.var_atten_dep.get() == "" or self.var_atten_attendance.get() == "Status":
            messagebox.showerror("Error", "Sab fields sahi bharain!", parent=self.root)
            return
    
        #  Prepare new record tuple/list
        new_record = (
            self.var_atten_id.get(),
            self.var_atten_name.get(),
            self.var_atten_dep.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get()
        )
    
        # Append to data list
        mydata.append(new_record)
    
        # Refresh table
        self.fetchData(mydata)
    
        messagebox.showinfo("Success", "Record added successfully!", parent=self.root)
        self.reset_data()
        
    def update_data(self):
        if self.var_atten_id.get() == "":
            messagebox.showerror("Error", "Pehle record select karo!", parent=self.root)
            return
    
        for index, record in enumerate(mydata):
            if record[0] == self.var_atten_id.get():
                # Update record with new values
                mydata[index] = (
                    self.var_atten_id.get(),
                    self.var_atten_name.get(),
                    self.var_atten_dep.get(),
                    self.var_atten_time.get(),
                    self.var_atten_date.get(),
                    self.var_atten_attendance.get()
                )
                break
    
        self.fetchData(mydata)
        messagebox.showinfo("Success", "Record updated successfully!", parent=self.root)
        self.reset_data()



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()