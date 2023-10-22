from tkinter import*
from tkinter import ttk
from turtle import left, width

mainFrm = Tk()
mainFrm.title("ระบบลงทะเบียน")
ttk.Frame(mainFrm, height = 300, width = 300).pack()
mainFrm.resizable(height=0,width=0,)

imgTeacher = PhotoImage(file="icon\student.png")

def teacher():
    teacherID = input("Enter Teacher ID:")
    teacherName = input("Enter Teacher Name:")
    print(teacherID)
    print(teacherName)

def subject():
    subjectName = input("Enter Subject Name:")
    subjectID = input("Enter Subject ID:")
    print(subjectName)
    print(subjectID)

def student():
    studentID = input("Enter Student ID:")
    studentName = input("Enter Student Name:")
    print(studentID)
    print(studentName)
    
ttk.Button(mainFrm, text = "teacher",image=imgTeacher ,compound="left", command=teacher).place(height=50,width=120, x= 100,y=20)
ttk.Button(mainFrm, text = "subject", command=subject).place(height=50,width=120, x= 100,y=70)
ttk.Button(mainFrm, text = "student", command=student).place(height=50,width=120, x= 100,y=120)
ttk.Button(mainFrm, text = "register").place(height=50,width=120, x= 100,y=170)
ttk.Button(mainFrm, text = "exit",command=mainFrm.destroy).place(height=50,width=120, x= 100,y=220)


mainFrm.mainloop()