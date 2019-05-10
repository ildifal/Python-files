# Ildiko Fallahpour

# This program contains a class called Employee,
# that holds data about an employee such as, name, ID number, department and
# job title.

# Initializing the class Employee.
class Employee:

    def __init__(self, name, idnum, dept, title):
        self.__name = name
        self.__idnum = idnum
        self.__dept = dept
        self.__title = title

# The set_name method accepts an argument for the employee's name.

    def set_name(self, name):
        self.__name = name

# The set_idnum method accepts an argument for the employee's ID number.

    def set_idnum(self, idnum):
        self.__idnum = idnum

# The set_dept method accepts an argument for the employee's department.

    def set_dept(self, dept):
        self.__dept = dept

# The set_title method accepts an argument for the employee's job title.

    def set_title(self, title):
        self.__title = title

# The get_name method returns the employee's name.

    def get_name(self):
        return self.__name

# The get_idnum method returns the employee's ID number.

    def get_idnum(self):
        return self.__idnum

# The get_dept method returns the employee's department.

    def get_dept(self):
        return self.__dept

# The get_title method returns the employee's job title.

    def get_title(self):
        return self.__title


    
