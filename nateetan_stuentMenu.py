from tkinter import *
from tkinter import END, messagebox, ttk
#import tkinter as tk 
import mysql.connector as mysql

def con_db(): #ฟั่งชั่นการเชื่อมต่อ database
    global cs, con
    con = mysql.connect(host="localhost", user="root", password="123455", database="register")
    cs = con.cursor()
def clearEntryOfStudent(): #การเคลียร์ค่าใน Entry widget
        entID.delete(0, END)
        entFname.delete(0, END)
        entLname.delete(0, END)
        entEmail.delete(0, END)
        entPhone.delete(0, END)
        entIDSub.delete(0, END)
        entSub.delete(0, END)

def SelectTreeStudent(event): 
        clearEntryOfStudent() # เรียกใช้ฟังก์ชันเพื่อล้างข้อมูลออกจาก Entry widget
        # กำหนดให้แสดงข้อมูลที่ Entry widget เมื่อคลิกที่แถวของ Treeview widget
        item = viewTcr.selection()
        for i in item:
            entID.insert("", viewTcr.item(i, "values")[0])
            entFname.insert("", viewTcr.item(i, "values")[1])
            entLname.insert("", viewTcr.item(i, "values")[2])
            entEmail.insert("", viewTcr.item(i, "values")[3])
            entPhone.insert("", viewTcr.item(i, "values")[4]) 
            entIDSub.insert("", viewTcr.item(i, "values")[5])
            entSub.insert("", viewTcr.item(i, "values")[6])

def insertDataToTreeView():
        # ลบข้อมูลออกจาก Treeview widgit
        for c in viewTcr.get_children():
            viewTcr.delete(c)

        con_db()  # เรียกใช้งานฟังก์ชันเชื่อมต่อฐานข้อมูล
        cs.execute("select * from tb_student") # ใช้คำสั่ง select ดึงข้อมูลจากตาราง teacher
        data = cs.fetchall() # แสดงผลข้อมูลทั้งหมดในตาราง teacher
        # อ่านข้อมูลและเพิ่มข้อมูลไปยัง Treeview widget ทีละแถว
        for d in data:
            viewTcr.insert("", "end", values=d)
        con.close()
        cs.close()

def insert_data(): # ตรวจสอบ Entry widget มีค่าว่างหรือไม่
    if entID.get()=="" or entFname.get()=="" or entLname.get()== "" or entEmail.get()== "" or entPhone.get() =="" or entIDSub.get() == "" or entSub.get() == "":
            # แจ้งเตือนข้อความ
        messagebox.showwarning("Warning", "กรุณากรอกข้อมูลให้ครบด้วยครับ !!")
    else:
        con_db() # เรียกใช้ฟังก์ชันเชื่อมต่อฐานข้อมูล
        # คำสั่งเพิ่มข้อมูลลงตาราง teacher
        cs.execute("INSERT INTO tb_student(student_id, fName, lName, email, tel, subject_ID, subject)"\
                       "VALUES(%s, %s, %s, %s, %s, %s, %s)"\
                       ,(str(entID.get()), str(entFname.get()),  
                         str(entLname.get()), str(entEmail.get()), str(entPhone.get()), str(entIDSub.get()), str(entSub.get())))
        con.commit()            # คำสั่งปรับปรุงข้อมูลในฐานข้อมูล
        con.close()
        cs.close()
        clearEntryOfStudent()   # เรียกใช้ฟังก์ชันเพื่อล้างข้อมูลออกจาก Entry widget
        insertDataToTreeView()  # เรียกใช้ฟังก์ชันเพื่อปรับปรุงข้อมูลใน Treeview widget
        # แสดง messageBox
        messagebox.showwarning("Information", "บันทึกข้อมูลเรียบร้อยแล้ว ครับ") 

def delete_data():
        if not viewTcr.selection():
            messagebox.showinfo("Information", "คุณยังไม่เลือกข้อมูลที่ต้องการลบ")
        else:
            item = viewTcr.selection()
            for i in item:
                con_db()      # เรียกใช้งานเชื่อมต่อฐานข้อมูล
                # คำสั่งลบข้อมูลออกจากตาราง teachers
                cs.execute("DELETE FROM tb_student WHERE student_id = %s " % 
                           viewTcr.item(i, "values")[0])
                # ถ้าตอบ Yes เป็นการยืนยันการลบข้อมูล
                msgBox = messagebox.askquestion("Warning", "ต้องการลบข้อมูลนี้ใช่หรือไม่", 
                                                icon="warning")
                if msgBox == "yes":
                    con.commit()  # ยืนยันการลบข้อมูล
            con.close()
            cs.close()
            clearEntryOfStudent()  # ลบข้อมูลใน Entry widget
            insertDataToTreeView() # ปรับปรุงข้อมูลใน Treeview widget

def udate_data():
    # กำหนดให้ Entry widget ของ entID แสดงผลข้อมูลได้อย่างเดียว
    # entStyle.configure("entID.TEntry", state="readonly")   
    # แจ้งเตือนถ้ายังไม่มีการเลือกข้อมูลที่ต้องการแก้ไข
    if not viewTcr.selection():
        messagebox.showinfo("Warning", "คุณยังไม่เลือกข้อมูลที่ต้องการแก้ไข")
    else:
        con_db()   # เรียกใช้ฟังก์ชันเชื่อมต่อกับฐานข้อมูล
        cs.execute("UPDATE tb_student set fName=%s, lName=%s,email=%s, tel=%s, subject_ID=%s, subject=%s WHERE student_id =%s"\
            ,(str(entFname.get()), str(entLname.get()), 
              str(entEmail.get()), str(entPhone.get()), str(entIDSub.get()), str(entSub.get()), str(entID.get())))
        # แจ้งเตือนก่อนปรับปรุงข้อมูลด้วย messagebox ถ้าตอบ yes ข้อมูลจะถูกปรับปรุง
        msgBox = messagebox.askquestion("Information", "ต้องการแก้ไขข้อมูลนี้ใช่หรือไม่", 
                                            icon="warning")
        if msgBox == "yes":
            con.commit()
            con.close()
            cs.close()
    clearEntryOfStudent()  # เรียกใช้ฟังก์ชันลบข้อมูลออกจาก Entry widget
    insertDataToTreeView() # เรียกใช้ฟังก์ชันเพื่อปรับปรุงข้อมูล Treeview widget

mainFrm = Tk()
mainFrm.title("ระบบข้อมูลนักเรียน")
ttk.Frame(mainFrm, height=600,width=800).pack()
mainFrm.resizable(width=0, height=0) #กำหนดให้ไม่ให้ย่อขยาย Frame ได้

# Create Label wiget
lblFrm1 =ttk.LabelFrame(mainFrm, text="เพิ่ม/แก้ไขข้อมูล").place(height=200,width=450,x=10, y=10)
lblId = ttk.Label(mainFrm, text="รหัสนักเรียน",).place(height= 20, width= 80, x= 20, y= 40)
lblFname = ttk.Label(mainFrm, text="ชื่อ",).place(height= 20, width= 60, x= 20, y= 70)
lblLname = ttk.Label(mainFrm, text="นามสกุล",).place(height=20, width= 60, x= 20, y= 100)
lblEmail = ttk.Label(mainFrm, text="อีเมล์",).place(height= 20, width= 60, x= 20, y= 130)
lblPhone = ttk.Label(mainFrm, text="โทรศัพท์ ",).place(height= 20, width= 60, x= 20, y= 160)
lblIDSub = ttk.Label(mainFrm, text="รหัสวิชา ",).place(height= 20, width= 60, x= 20, y= 190)
lblSub = ttk.Label(mainFrm, text="ชื่อวิชา ",).place(height= 20, width= 60, x= 20, y= 220)

#entStyle = ttk.Style()
entID   = ttk.Entry(mainFrm)
entFname = ttk.Entry(mainFrm)
entLname = ttk.Entry(mainFrm)
entEmail = ttk.Entry(mainFrm)
entPhone = ttk.Entry(mainFrm)
entIDSub = ttk.Entry(mainFrm)
entSub = ttk.Entry(mainFrm)

entID.place(height=30,width=200,x=120,y=40)
entFname.place(height=30,width=200,x=120,y=70 )
entLname.place(height=30,width=200,x=120,y=100)
entEmail.place(height=30,width=200,x=120,y=130)
entPhone .place(height=30,width=200,x=120,y=160)
entIDSub.place(height=30,width=200,x=120,y=190)
entSub.place(height=30,width=200,x=120,y=220)


#Create Button Widget
btnSave = ttk.Button(mainFrm, text= "บันทึก",command=insert_data).place(height=40,width=120, x=480,y=20)
btnEdit = ttk.Button(mainFrm, text= "แก้ไข",command=udate_data).place(height=40,width=120, x=480,y=58)
btnDelete = ttk.Button(mainFrm, text= "ลบ", command=delete_data).place(height=40,width=120, x=480,y=96)
btnCancle = ttk.Button(mainFrm, text= "ยกเลิก",command=clearEntryOfStudent).place(height=40,width=120, x=480,y=133)
btnClose = ttk.Button(mainFrm, text= "ปิดโปรแกรม").place(height=40,width=120, x=480,y=170)

#Create View Table widget
viewTcr = ttk.Treeview(mainFrm,columns=("ID","Fname", "Lname","Email","Tell","SubjectID", "Subject"),show="headings")
viewTcr.place(height= 300,width=740, x=15,y=250)

sc = ttk.Scrollbar(mainFrm, orient= "vertical",command= viewTcr.yview)
sc.place(height=300,x=740,y=250)
viewTcr.config(yscrollcommand=sc.set)

viewTcr.column("#1",width="80")
viewTcr.column("#2",width="80")
viewTcr.column("#3",width="80")
viewTcr.column("#4",width="80")
viewTcr.column("#5",width="80")
viewTcr.column("#6",width="80")
viewTcr.column("#7",width="80")

viewTcr.heading("#1",text="รหัสนักเรียน")
viewTcr.heading("#2",text="ชื่อ")
viewTcr.heading("#3",text="สกุล")
viewTcr.heading("#4",text="อีเมล์")
viewTcr.heading("#5",text="เบอร์โทรศัพท์")
viewTcr.heading("#6",text="รหัสวิชา")
viewTcr.heading("#7",text="ชื่อวิชา")

viewTcr.bind('<ButtonRelease>',SelectTreeStudent) # 

mainFrm.mainloop()