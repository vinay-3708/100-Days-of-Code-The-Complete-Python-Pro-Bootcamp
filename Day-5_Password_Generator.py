import random
#import string
#number = range(0,10)
number = ['0','1','2','3','4','5','6','7','8','9']
#alpha = list(string.ascii_letters)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
spl_ch = ['!','#','$','%','&','*','(',')','+']
print("Welcome to PyPassword Generator!")
alp = int(input("How many letters would you like in your password? "))
num = int(input("How many numbers would you like in your password? "))
sp = int(input("How many special characters would you like in your password? "))
password = random.choices(alpha, k=alp)
#print(password)
password.extend(random.choices(spl_ch, k=sp))
#print(password)
password.extend(random.choices(number, k=num))
random.shuffle(password)
pwd = ""
for x in password:
    pwd += x
print(pwd)