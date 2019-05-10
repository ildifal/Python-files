# Ildiko Fallahpour
#

# This program creates and displayes three instances
# of the class called employee.

# Importing the employee.py file to use the employee class.

import employee

# Getting the the necessary data from the user and passing it as parameters
# to the initializer method.

def main():

    for count in range(1, 4):
        count += 1
        name = input('Enter employee name: ')
        idnum = input('Enter employee ID: ')
        dept = input('Enter department: ')
        title = input('Enter position: ')
        person = employee.Employee(name, idnum, dept, title)

# Displaying the entered data.
def __str__(self):
    print('Employee ' + str(count) + ':' )
    return  'Name: ' + self.__name + \
            'ID number: ' + self.__idnum + \
            'Department: ' + self.__dept + \
            'Title: ' + self.__title

main()    
