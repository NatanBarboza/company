from manager import Manager


manager = Manager("João", 45, "Manager of IT", 6000)

print(manager.name)
print(manager.age)
print(manager.role)
print(manager.salary)

manager.salary = 10000
print(manager.salary)

manager.bonus()
print(manager.salary)