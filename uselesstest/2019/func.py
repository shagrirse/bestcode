import math
import time
def add(x1,x2):
    print(int(x1)+int(x2))
def sub(x1,x2):
    print(int(x1)-int(x2))
def div(x1,x2):
    print(int(x1)/int(x2))
def mul(x1,x2):
    print(int(x1)*int(x2))
def quad(a,b,c):
    d=b**2-4*a*c
    if d == 0:
        ans = -b / (2*a)
        print(ans)
    elif d>0:
        ans = -b + math.sqrt(b**2 - 4*a*c) / (2*a)
        ans2= -b + math.sqrt(b**2 - 4*a*c) / (2*a)
        print(ans, ans2)
    else:
        print("imaginary")
print("Welcome to calculator! Please wait while system initializes...")
time.sleep(1)
prompt = str(input("What operation? (+/-* or quad) : "))
if prompt == "+":
    a = str(input("First number: "))
    b = str(input("Second number: "))
    add(a,b)
elif prompt == "-":
    a = str(input("First number: "))
    b = str(input("Second number: "))
    sub(a,b)
elif prompt == "/":
    a = str(input("First number: "))
    b = str(input("Second number: "))
    div(a,b)
elif prompt == "*":
    a = str(input("First number: "))
    b = str(input("Second number: "))
    mul(a,b)
else:
    x = int(input("First number: "))
    y = int(input("Second number: "))
    z = int(input("Third number: "))
    quad(x, y, z)