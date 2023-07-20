from datetime import datetime


class BirthdayError(Exception):
    ...


class Birthday:
    def __init__(self, value):
        self.__value = None
        self.value = value
    
    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, value):
        try:
            self.__value = datetime.strptime(value, "%d-%m-%Y")
        except ValueError:
            raise BirthdayError()
    
    def __str__(self):
        return self.__value.strftime("%Y-%d-%m-%Y")


class Employee:
    def __init__(self, name, phone=None, email=None, birthday=None):
        self.name = name
        self.birthday = birthday
    
    def get_day_to_birthday(self):
        if self.birthday:
            return self.birthday.value.weekday()
        return -1


emp = Employee("Bill")
emp1 = Employee("Jill", birthday=Birthday("10-12-1995"))

print(emp.get_day_to_birthday())