
from abc import ABC, abstractmethod

# class Employee:
#     pass

# e= Employee()
# print(type(e))

# class Employee:
#     def __init__(self, emp_id, name, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.salary = salary

# e= Employee(1, 'Alisa', 20000)
# print(e.name, e.salary)
class EmployeeBase(ABC):
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def compensation(self):
        pass



class Employee:
    company='1232132'

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self._salary= 0
    def info(self):
        return f'{self.name}->{self.salary}'

    def __str__(self):
        return f'{self.name}: {self.salary}'
    
    def __eq__(self):
        if not isinstance(other, Employee):
            return NotImplemented
    @classmethod
    def from_string(cls, raw):
        emp_id, name, salary= raw.split(',')
        return cls(int(emp_id), name, int(salary))

    @staticmethod
    def valid_name(name):
        return len(name.strip()) >=2
    def get_salary(self):
        return self.salary
    def set_salary(self, value):
        if value < 0:
            self.salary = 0
        else:
            self.salary = value

    def compensation(self):
        return self.salary

    # @property
    # def salary(self):
    #     return self._salary

    # @salary.setter
    # def salary(self, value):
    #     self._salary= value

    # @salary.deleter
    # def salary(self):
    #     self._salary = 0

    def yearly_income(self):
        return self.salary * 12

class LoggableMixin:
    def log(self, massage):
        print(f'[LOG]{self.name}: {massage}')

class Manager(Employee, LoggableMixin):
    def __init__(self, emp_id, name, salary, bonus):
        super().__init__(emp_id, name, salary)
        self.bonus = bonus

    def yearly_income(self):
        return super().yearly_income() + self.bonus

m = Manager(3, 'Алексей', 2000, 5000)
print(m.log('123123'))
print(Manager.__mro__)
print(m.yearly_income())

# e= Employee(1, 'Alisa', 20000)
# print(e.name, e.salary, Employee.company)
# print(e.info())

# e = Employee.from_string('2, Андрей, 3000')

# e.set_salary(4000)
# e.salary= 4000
# print(e.get_salary(), e.salary)
# print(e.emp_id, e.name, e.salary, Employee.valid_name(e.name()))
# del e.salary
# print(e.salary)

