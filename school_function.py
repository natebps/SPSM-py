id = input("Enter ID:")
name = input("Enter name:")

def info(name,id):
    all = (f'Name:{name} ID:{id}')
    return all
info(name,id)

s1 = int(input("Enter test score:"))
s2 = int(input("Enter personal score:"))
s3 = int(input("Enter eiei score:"))

def score(s1,s2,s3):
    sum = s1+s2+s3
    return sum
score(s1,s2,s3)

print(info(name,id))
print(score(s1,s2,s3))

