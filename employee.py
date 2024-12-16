import importlib
from person import Person 
# from utils import checkParamIsNumber

def checkParamIsNumber(str, floatr_value=False):
    module = importlib.import_module("utils")
    return module.checkParamIsNumber(str, floatr_value)

class Employee(Person):
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self._field = input("Please enter the field of work: ")
        self._salary = checkParamIsNumber("salary")

    def getField(self):
        return self._field
    
    def setField(self, field):
        self._field = field

    def getSalary(self):
        return self._salary
    
    def setSalary(self, salary):
        self._salary = salary

    def printEmployee(self, idx=-1):     
        tab_str = super().printPerson(idx)
        print(tab_str + "Field: " + self.getField())
        print(tab_str + "Salary: " + str(self.getSalary()))

    def printMySelf(self, idx):
        self.printEmployee(idx)
