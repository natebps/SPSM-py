#นทีธาร บัวประเสริฐ ม.6/CE เลขที่ 8

class student:
    def __init__(name1,id1, major1):
        name = name1
        id = id1
        major = major1
        print(name,id,major)
    def find_sum(score1,score2,score3):
        sum_all = score1+score2+score3
        print("Total:",sum_all)
        return sum_all
    def calculate(sumall):
        if sumall >= 80:
             print("Grade A")
        elif 70 <= sumall < 80:
            print("Grade B")
        elif 60 <= sumall < 70:
            print("Grade C")
        elif 50 <= sumall < 60:
            print("Grade D")
        else:
            print("Grade F")
class Major(student):
    nameS = input("Enter Student name: ")
    idSt = input("Enter Student ID: ")
    majorS = input("Enter Major: ")
    Student = student.__init__(nameS,idSt,majorS)
    
    Score1 = int(input("Enter Score1: "))
    Score2 = int(input("Enter Score2: "))
    Score3 = int(input("Enter Score3: "))
    all = int(student.find_sum(Score1,Score2,Score3))

    SUM = student.calculate(all)


