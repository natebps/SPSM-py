class book:
    nameBook = "PythonEiEi"
    ISBN = 212224236248
    def read(book,isbn):
       nameBook = book
       ISBN = isbn
       print(nameBook, ISBN)
b = book.read("eiei",123456)


class subject:
    def student(nS,idS):
        nameStu = nS 
        idStu = idS
        print("=====Student is:",nameStu,idStu)
    def register(name,id,credits):
        nameSubject = name
        IDSubject = id
        creditSubject = credits
        print("=====Register Subject is:",nameSubject,IDSubject,creditSubject)
    def unregister(unname,unid,uncredits):
        UnnameSubject = unname
        UnIDSubject = unid
        UncreditSubject = uncredits
        print("======Unregister Subject is:",UnnameSubject,UnIDSubject,UncreditSubject)

nameS = input("Enter Student name: ")
idSt = input("Enter Student ID: ")
student = subject.student(nameS,idSt)
       
n = input("Enter name register subject: ")
d = input("Enter id register subject: ")
c = input("Enter credit register subject: ")
re = subject.register(n,d,c)

n1 = input("Enter name register subject: ")
d1 = input("Enter id register subject: ")
c1 = input("Enter credit register subject: ")
un = subject.unregister(n1,d1,c1)