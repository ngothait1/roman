class Person:
    def __init__(self, id, name, age):
        self._id = id
        self._name = name
        self._age = age


    def getId(self):
        return self._id
    
    def setId(self, id):
        self._id = id
    
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
    
    def getAge(self):
        return self._age
    
    def setAge(self, age):
        self._age = age

    def printPerson(self, idx = -1):
        tab_str = self.tab_str_index(idx)
        print(tab_str + "Name: " + self.getName())
        print(tab_str + "Age: " + str(self.getAge()))
        return tab_str

    def printMySelf(self, idx):
        self.printPerson(self, idx)

    def tab_str_index(self, idx):
        tab_str = ""
        if idx != -1:
            tab_str = "   "
            print(str(idx) +  ". ID:" + str(self.getId()))  
        else:
            print("ID: " + str(self.getId()))
        return tab_str
    
    def personAsDict(self):
        return {"id": self.getId(), "name": self.getName(), "age": self.getAge()}
    
    def mySelfAsDict(self):
        return self.personAsDict()

