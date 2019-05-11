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
    count = 0
    count += 1
    for count in range(1, 4):
        print('Employee ' , str(count) + ':')
        name = input('Enter employee name: ')
        idnum = input('Enter employee ID: ')
        dept = input('Enter department: ')
        title = input('Enter position: ')
        print()

# Creating a new Employee object and ssigning it to the person variable.

        person = employee.Employee(name, idnum, dept, title)

# Adding the object to the list.

        person_list.append(person)
    return person_list
    
def display_list(person_list):
    for item in person_list:
        print(item)
    
main()    
