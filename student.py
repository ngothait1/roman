from person import Person # type: ignore

class Student(Person):
    def __init__(self, id, name, age, field, year, avg):
        super().__init__(id, name, age)
        self._field = field
        self._year = year
        self._avg = avg
    
    def getField(self):
        return self._field
    def setField(self, field):
        self._field = field

    def getYear(self):
        return self._year
    def setYear(self, year):
        self._year = year

    def getAvg(self):
        return self._avg
    def setAvg(self, avg):
        self._avg = avg

    def printStudent(self, idx):
        super().printPerson(idx)
        tab_str = ""
        if idx != -1:
            tab_str = "   "
  
        print(tab_str + "Field: " + self.getField())
        print(tab_str + "Year of study: " + str(self.getYear()))
        print(tab_str + "Average score: " + str(self.getAvg()))
    
    def printMySelf(self, idx):
        self.printStudent(idx)
