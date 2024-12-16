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
        tab_str = ""
        if idx != -1:
            tab_str = "   "
            print(str(idx) +  ". ID:" + str(self.getId()))  
        else:
            print("ID: " + str(self.getId()))
    
        print(tab_str + "Name: " + self.getName())
        print(tab_str + "Age: " + str(self.getAge()))
    
    def printMySelf(self, idx):
        self.printPerson(self, idx)

