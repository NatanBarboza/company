from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name:str, age:int, role:str, salary:float):
        self.__name = name
        self.__age = age
        self.__role = role
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, new_role):
        self.__role = new_role

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary

    @abstractmethod
    def bonus(self):
        self.__salary += self.__salary * 0.1