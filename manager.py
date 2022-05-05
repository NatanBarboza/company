from employee import Employee

class Manager(Employee):
    def __init__(self, name: str, age: int, role: str, salary: float):
        super().__init__(name, age, role, salary)

    def bonus(self):
        return super().bonus()