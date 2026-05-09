import os 
os.system("cls")

num1 =  int(input("Enter first number: "))
num2 =  int(input("Enter second number: "))
num3 =  int(input("Enter third number: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is the greatest number")
    else:
        print(f"{num3} is the greatest number")
if num2 > num1:
    if num2 > num3:
        print(f"{num2} is the greatest number")
    else:
        print(f"{num3} is the greatest number")
if num3 > num1:
    if num3 > num2:
        print(f"{num3} is the greatest number")
    else:
        print(f"{num2} is the greatest number") 
