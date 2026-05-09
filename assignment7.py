import os 
os.system("cls")

salary = int(input("Enter your salary: "))

if salary > 50000:
    bonus = salary * 0.2    
elif salary > 30000 and salary <= 50000
    bonus = salary * 0.1
elif salary > 20000 and salary <= 30000:
    bonus = salary * 0.05           
else:
    bonus = 0

new_salary = salary + bonus
print(f"Your new salary after bonus is: {new_salary}")