lab_weight = 0.7
exam_weight = 0.2
attendance_weight = 0.1
letter_grade = ['A', 'B', 'C', 'D', 'F']
print('****Welcome to the LAB grade calculator! ****')
#name of student
first_name  = input("Who are we calculating grades for ==>")
#lab grade
lab_grade = int(input("Enter the Labs grade? ==>"))
if lab_grade > 100:
    print("The lab value should have been 100 or less. It has been changed to 100.")
    lab_grade = 100
elif lab_grade < 0:
    print("The lab value shoud have been zero or greater. It has been changed to 0.")
    lab_grade = 0
#exam grade
exam_grade = int(input("Enter the EXAMS grade? ==>"))
if exam_grade > 100:
    print("The exam value should have been 100 or less. It has been changed to 100.")
    exam_grade = 100
elif exam_grade < 0:
    print("The exam value shoud have been zero or greater. It has been changed to 0.")
    exam_grade = 0
#attendance grade
attendance_grade = int(input("Enter the Attendance grade? ==>"))
if attendance_grade > 100:
    print("The attendance value should have been 100 or less. It has been changed to 100.")
    attendance_grade = 100
elif attendance_grade < 0:
    print("The sttendance value shoud have been zero or greater. It has been changed to 0.")
    attendance_grade = 0
#weighted grade = weighted grade * lab grad and sum all products
weighted_grade = (lab_weight * lab_grade) + (exam_weight * exam_grade) + (attendance_weight * attendance_grade)
print('The weighted grade for {first_name} is {weighted_grade}')
if weighted_grade > 90 and weighted_grade  >= 100: #letter grade
    print(f'{first_name} has a letter grade of A')
elif weighted_grade <= 80 and weighted_grade >= 89:
    print(f'{first_name} has a letter grade of B')
elif weighted_grade <= 70 and weighted_grade >= 79:
    print(f'{first_name} has a letter grade of C')
elif weighted_grade <= 60 and weighted_grade >= 69:
    print(f'{first_name} has a letter grade of D')
else:
    print(f'{first_name} has a letter grade of F of {weighted_grade} ')
print('**** Thanks for using the Lab grade calculator ****')
                                                                
