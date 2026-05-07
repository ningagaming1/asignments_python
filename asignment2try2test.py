import os 
os.system("cls")

#varibles
no_of_leters = 0
final_number = ""

#taking input
input1 = int(input("enter your number "))

while input1 != 0 :
    left_most_leter = input1 % 10
    input1 = int(input1/10)
    final_number = f"{final_number}{left_most_leter}"
    no_of_leters = no_of_leters-1
print(f"{final_number}")