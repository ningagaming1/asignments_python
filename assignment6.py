import os 
os.system("cls")

input1 = int(input("Enter marks of first subject: "))
input2 = int(input("Enter marks of second subject: "))
input3 = int(input("Enter marks of third subject: "))
max_marks_of_subject_one = int(input("Enter maximum marks of first subject: "))
max_marks_of_subject_two = int(input("Enter maximum marks of second subject: "))
max_marks_of_subject_three = int(input("Enter maximum marks of third subject: "))
total = int(input1) + int(input2) + int(input3)
average_marks = total / 3
print(f"Total marks: {total}")
print(f"Average marks: {average_marks}")
percentage = (total / (max_marks_of_subject_one + max_marks_of_subject_two + max_marks_of_subject_three)) * 100
print(f"Percentage: {percentage}%")
if percentage >= 90:
    print("Grade: ")
if percentage >= 80 and percentage < 90:
    print("Grade: ")
if percentage >= 70 and percentage < 80:
    print("Grade: ")
if percentage >= 60 and percentage < 70:
    print("Grade: ")