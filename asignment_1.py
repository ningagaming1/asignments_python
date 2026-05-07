import os 

#clear terminal
os.system("cls")

#making function
 #some varables
#taking inputs
input1 = int(input("what do you want first to be "))
input2 = int(input("what do you want second input ot be "))
input3 = int(input("what do you want to do 1 for add 2 for subtract 3 for multiply and 4 for divide "))
#procesing data

if input3 == 1:
    output = input1 + input2
    print(f"{output}")
if input3 == 2:
   output = input1 - input2
   print(f"{output}")
if input3 == 3:
   output = input1 * input2
   print(f"{output}")
if input3 == 4:
   output = input1/input2
   remainder = input1 % input2 
   print(f"your answer is {output}")
   print(f"your remainder is {remainder}")

   