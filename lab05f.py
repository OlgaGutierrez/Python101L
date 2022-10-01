########################################################################
##
## CS 101 Lab
## Program 05 
## Name: Juli Gutierrez
## Email: ojgpfv@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. import string
##      2. creat a get_check_digit function using library card as parameter
##      3. create a verify_check_digit function creating tuple
##      4. create get_school function with digits only ranging from 1-3 assigning each digit to correct school
##      5. create a get_grade function ranging from digits 1-4 assigning each digit to correct grade
##      6. create a while loop for main program
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


# import statements
import string

# character value function
def character_value(ch : str) -> int:
    '''return A as 0, B as 1, C as 2, etc.'''
    return string.ascii_uppercase.index("A")

# get check digit function using library card as parameter
def get_check_digit(library_card):
    sum = 0
    for i in range(len(library_card)):
        value = character_value(library_card[i])
        sum += value * (i+1)
    return sum % 10

# verify check digit function using tuple using 
def verify_check_digit(num:str) -> tuple:
    '''return true if check digit is valid and false if not'''
    if len(num) != 10:
        return False, 'The length of the number given must be 10'
    for index, value in enumerate(num[0:5]):
        if not value.isalpha():
            return False, 'The first 5 characters must be A-Z, the invalid character is at {} is {}'.format(index,value)
        for index, value in enumerate(num[7:]):
            if not value.isdigit():
                return False, 'The last 3 characters must be 0-9, the invalid character is at {} is {}'.format((index + 7), value)
            if get_school(num) == 'Invalid School':
                return False, 'the sixth character must be 1 2 or 3'
            if get_grade (num) == 'Invalid Grade':
                return False,'the seventh character must be 1 2 3 or 4'
            elif get_check_digit(num) != int(num[9]):
                return True, ''

# get schoool function to output was school student is in
# can only have numbers from 1-3
def get_school(num : str) -> str:
    '''return school withindex value'''
    schools = {'1' : 'School of Computing and Engineering SCE', '2' : 'School of Law','3' : 'College of Arts and Sciences'}
    if num[5] in schools:
        return schools[num[5]]
    else:
        return 'Invalid School'

# get grade function using if statements
# can only include digits using 1,2,3,4, or else invalid
def get_grade(num : str) -> str:
    '''returns for academci grade'''
    grade = {'1' : 'Freshman','2' : 'Sophomore','3' : 'Junior','4' : 'Senior'}
    if num[6] in grade:
        return grade[num[6]]
    else:
        return 'Invalid Grade'

# have user input card number making sure it is valid
def main():
    while(1):
        library_card = input("Enter Library Card. Hit Enter to Exit ==> ")
        (is_valid,msg) = verify_check_digit(library_card)

        if is_valid == True:
            print(msg)
            print("The cared belongs to a student in " + get_school(library_card))
            print("The card belongs to a " + get_grade(library_card))

        else:
            print("Library card is invalid.")
            print(msg)

# 
if __name__ == "__main__":
    main()

