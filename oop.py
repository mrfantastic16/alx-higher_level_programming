#!/usr/bin/python3

class Employee:
    raise_amount = 1.04
    num_of_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'
        Employee.num_of_employee += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amount = amt

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 500)
emp_2 = Employee.from_string('Chimobi-Ekwunife-9000')


import datetime
my_date = datetime.date(2018, 7, 11)

# print(Employee.is_workday(my_date))


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


dev_1 = Developer("Martin", "Scharfer", 1200, "Python")
dev_2 = Developer("Segun", "Ojo", 1500, "Java")

# print(dev_1.fullname())


class Manager(Employee):
    def __init__(self, first, last, pay, employee=None):
        super().__init__(first, last, pay)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    def add_employee(self, employee):
        if employee not in self.employee:
            self.employee.append(employee)

    def remove_employee(self, employee):
        if employee in self.employee:
            self.employee.remove(employee)

    @staticmethod
    def print_employee(employee):
        return employee.fullname()


mgr_1 = Manager("Charles", "Barbage", 3000, dev_1)

# print(mgr_1.print_employee(dev_2))


class P:
    def __init__(self, x):
        self.set_x(x)

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    def get_x(self):
        return self.__x


# p1 = P(0)
# print(p1.get_x())


class P2:
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


p1 = P2(10001)
print(p1.x)
