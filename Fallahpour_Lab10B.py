# Ildiko Fallahpour
#

# This program creates and displayes three instances
# of the class called employee.

# Importing the employee.py file to use the employee class.

import employee

def main():

# Getting a list of Employee objects.

    employees = make_list()
    
# Displaying the data in the list.
    
    display_list(employees)

def make_list():

# Creating an empty list.

    person_list = []

# Adding three Employee objects to the list.
    
# First employee:

    name1 = input('Enter employee name: ')
    idnum1 = input('Enter employee ID: ')
    dept1 = input('Enter department: ')
    title1 = input('Enter position: ')
    print()
    person1 = employee.Employee(name1, idnum1, dept1, title1)

# Second employee:

    name2 = input('Enter employee name: ')
    idnum2 = input('Enter employee ID: ')
    dept2 = input('Enter department: ')
    title2 = input('Enter position: ')
    print() 
    person2 = employee.Employee(name2, idnum2, dept2, title2)

# Third employee:

    name3 = input('Enter employee name: ')
    idnum3 = input('Enter employee ID: ')
    dept3 = input('Enter department: ')
    title3 = input('Enter position: ')
    print()
    person3 = employee.Employee(name3, idnum3, dept3, title3)
    
# Adding the object to the list.

    person_list.append(person1)
    person_list.append(person2)
    person_list.append(person3)
    return person_list

def display_list(person_list):
    count = 0
    count += 1
    for count in range(1, 4, 1):
        print()
        print('Employee ' + str(count) + ':' )
        for person in person_list:
            print(person)

main()
    
