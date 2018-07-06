class Person(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


class Customer(Person):
    def __init__(self, first_name, last_name, email):
        super(Customer, self).__init__(first_name, last_name, email)
 
    def is_employee(self):
        return False

class Employee(Person):
    def __init__(self, first_name, last_name, email):
        super(Employee, self).__init__(first_name, last_name, email)
 
    def is_employee(self):
        return True
