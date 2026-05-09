import os 
os.system("cls")

num1 =  int(input("Enter first number: "))
num2 =  int(input("Enter second number: "))

operation = input("Enter the operation you want to perform 1 for even/odd, 2 for finding largest number, 3 for exit: ")
if operation == "1":
    if num1 % 2 == 0:
        print(f"{num1} is an even number")
    else:
        print(f"{num1} is an odd number")
    if num2 % 2 == 0:
        print(f"{num2} is an even number")
    else:
        print(f"{num2} is an odd number")
elif operation == "2":
    if num1 > num2:
        print(f"{num1} is the largest number")
    else:
        print(f"{num2} is the largest number")
elif operation == "3":
    print("Exiting the program")
else:
    print("Invalid operation")
