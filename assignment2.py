import os

#clearing terminal
os.system('cls')

#varibles
no_of_leters = 0
random = ""
fist_digit_from_frount_without_desimal = 0

#taking input
no_of_leters = int(input("how many numbers are in this number "))
input1 = int(input("enter your number "))


#main body
while no_of_leters != 0:
    fist_digit_from_frount_with_desimal = input1 % pow(10,no_of_leters-1) 
    print(f"{fist_digit_from_frount_with_desimal}")
    if fist_digit_from_frount_with_desimal - round(fist_digit_from_frount_with_desimal) != 0:
        fist_digit_from_frount_without_desimal = round(fist_digit_from_frount_with_desimal-0.5)
    if fist_digit_from_frount_with_desimal - round(fist_digit_from_frount_with_desimal) == 0:
        fist_digit_from_frount_without_desimal = fist_digit_from_frount_with_desimal
    random = f"{fist_digit_from_frount_without_desimal}{random}"
    no_of_leters = no_of_leters - 1
print(f"{random}")