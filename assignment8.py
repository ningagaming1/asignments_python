import os
os.system("cls")

total_units = int(input("Enter total units consumed: "))

if total_units <= 100 and total_units >= 0:
    bill_amount = total_units * 5
elif total_units > 100 and total_units <= 200:
    bill_amount = (100 * 5) + ((total_units - 100) * 7)
elif total_units > 200 :
    bill_amount = (100 * 5) + (100 * 7) + ((total_units - 200) * 10)
else:
    bill_amount = "invalid input"
if bill_amount > 2000:
    discout = bill_amount * 0.1
    bill_amount = bill_amount - discout

print(f"Your electricity bill is: {bill_amount}")
print(f"your discount is: {discout}")