from person import Person # type: ignore

class Employee(Person):
    def __init__(self, id, name, age, field, salary):
        super().__init__(id, name, age)
        self._field = field
        self._salary = salary

    def getField(self):
        return self._field
    def setField(self, field):
        self._field = field

    def getSalary(self):
        return self._salary
    def setSalary(self, salary):
        self._salary = salary

    def printEmployee(self, idx=-1):
        super().printPerson(idx)
        tab_str = ""
        if idx != -1:
            tab_str = "   "
  
        print(tab_str + "Field: " + self.getField())
        print(tab_str + "Salary: " + str(self.getSalary()))

    def printMySelf(self, idx):
        self.printEmployee(idx)
