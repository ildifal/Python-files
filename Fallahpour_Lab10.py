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

    

def make_list():

# Creating an empty list.

    person_list = []

# Adding three Employee objects to the list.

    for count in range(1, 4):
        nam = input('Enter employee name: ')
        idn = input('Enter employee ID: ')
        dep = input('Enter department: ')
        tit = input('Enter position: ')
        print()

# Creating a new Employee object and ssigning it to the person variable.

        person = employee.Employee(nam, idn, dep, tit)

# Adding the object to the list.

        person_list.append(person)
        return person_list
    

    
main()    
