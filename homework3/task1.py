''' 1) Переписать код в соответствии с Single Responsibility Principle:
from datetime import date
class Employee:
def init(self, name, dob, base_salary):
self.name = name
self.dob = dob
self.base_salary = base_salary

def get_emp_info(self):
    return f"name - {self.name} , dob - {self.dob}"

def calculate_net_salary(self):
    tax = int(self.base_salary * 0.25)  # рассчитать налог другим способом
    return self.base_salary - tax

Подсказка: вынесите метод calculateNetSalary() в отдельный класс
'''

from datetime import date


class Employee:

    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"

    def get_base_salary(self):
        return self.base_salary


class CalculateNetSalary:

    def calculate_net_salary(self, base_salary):
        tax = int(base_salary * 0.25)
        return base_salary - tax
