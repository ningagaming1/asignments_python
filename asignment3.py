import os
#clear chat
os.system('cls')

#input 
temp1=float(input("what is the tempreture you want to convert "))
index = int(input("if the given temprature is in ferahanite press 1 if in celcius press 2 and if in klvin press 3:- "))

#main
if index == 1:
    f=temp1
    celcius = (f-32)*5/9
    kelven = celcius + 273.15
    print(f"your temp is {celcius}degre celcius and {kelven}kelvin")
elif index == 2:
    celcius = temp1
    ferehinite = celcius*9/5+32
    kelven = celcius + 273.15
    print(f"your temp is {ferehinite}degre ferehinite and {kelven}kelvin")
elif index == 3:
    kelven = temp1
    celcius= kelven - 273.15
    ferehinite = celcius*9/5+32
    print(f"your temp is {celcius}degre celcius and {ferehinite}degree ferehinite")
else :
    print("invalid output please rerun the program")
