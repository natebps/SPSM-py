#NATEETAN NO.09 M.5/IT
#number1=========================================
a = int(input("Input number:"))
b = int(input("Input number:"))
c = int(input("Input number:"))

z = a+b+c
result = z/3
print("RESULT:", result)

#number2=========================================
x = list(map(int,input("\nEnter the numbers : ").strip().split()))
a,b,c,d,e = x
if a < b < c < d < e:
    print("CORRECT")
else:
    print("INCORRECT")

#number3=========================================
hr = int(input("Input hour of parking:"))
min = int(input("Input minute of parking:"))

hrs = hr*60
timetotal = hrs+min

n =()
if timetotal <= 15:
    print("Total is FREE")
elif 15<= timetotal <240:
    print("Total is",hr*20)
elif 240 < timetotal:
    print("Total is 2,000")