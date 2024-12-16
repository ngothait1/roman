from person import Person 
from utils import checkParamIsNumber

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

    def employeeAsDict(self):
        emp_dict = super().personAsDict()
        emp_dict["field"] = self.getField()
        emp_dict["salary"] = self.getSalary()
        return emp_dict

    def mySelfAsDict(self):
        return self.employeeAsDict()

