def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Exit")

def saveNewEntry(dict_by_id, list_of_id):
    id = input("ID: ")

    id = checkIdIsNumber(id)
    if id == -1:
        return -1

    if id in dict_by_id:
        print("Error: ID already exists: " + str(dict_by_id[id]))
        return -1

    name = input("Name: ")

    age = (input("Age: ")) 

    if not age.isdigit():
        print("Error, age must be a number. " + age + " is not a number")
        return -1 
    age = int(age)
    
    dict_by_id[id] = (name, age)     
    list_of_id.append(id)
    print("ID [" + str(id) + "] saved successfully")
    return int(age)
    

def searchById(dict_by_id):
    id = input("Please enter the ID you want to look for: ")
    
    id = checkIdIsNumber(id)
    if id == -1:
        return -1

    if id in dict_by_id:
        printById(id)
    else:
        print("Error: ID " + str(id) + " is not saved")


def printAgesAverage(sum_of_ages, list_of_id):
    if len(list_of_id) == 0:
        print("0")
        return
    res = sum_of_ages / len(list_of_id)
    print(str(res))



def printAllNames(dict_by_id):
    if len(dict_by_id) == 0:
        return
    for idx, value in enumerate(dict_by_id.values()):
        print(str(idx) + ". " + value[0])



def printAllIds(dict_by_id):
    if len(dict_by_id) == 0:
        return
    for idx, id in enumerate(dict_by_id.keys()):
        print(str(idx) + ". " + str(id))


def printAllEntries(dict_by_id):
    if len(dict_by_id) == 0:
        return
    for idx, id  in enumerate(dict_by_id.keys()):
        printById(id, idx)


def printEntryByIndex(list_of_id):
    idx = input("Index: ")

    if not idx.isdigit():
        printIndexErrorNotNumber(idx)
        return
    idx = int(idx)
    if idx >= len(list_of_id) or idx < 0:
        printIndexErrorOutOfRange(idx, len(list_of_id))
    else:
        printById(list_of_id[idx])

def exitSystem():
    flag = ""
    while flag != "y" and flag != "n":
        flag = input("Are you sure you want to exit? (y/n) ")
    if flag == "y":
        print("Goodbye!")
        exit()

def checkIdIsNumber(id):
    if  not id.isdigit():
        printIdErrorNotNumber(id)
        return -1
    
    return int(id)

def printById(id, idx=-1):
    if idx != -1:
        print(str(idx) +  ". " + str(id))
        print(tab_str + "Name: " + dict_by_id[id][0])
        print(tab_str + "Age: " + str(dict_by_id[id][1]))
    else:
        print("ID: " + str(id))
        print("Name: " + dict_by_id[id][0])
        print("Age: " + str(dict_by_id[id][1]))


def printIdErrorNotNumber(id):
    print("Errorr, ID must be a number. " + id + " is not a number")

def printIndexErrorNotNumber(idx):
    print("Error, index must be a number. " + idx + " is not a number")

def printIndexErrorOutOfRange(idx, num_people):
    if idx >= num_people:
        print("Error, Index out of range. The maximum index allowed is " + str(num_people - 1))
    elif idx < 0:
        print("Error, Index out of range. The minimum index allowed is 0")


tab_str = "   "
dict_by_id = {}
list_of_id = []
sum_of_ages = 0
while True:
    printMenu()
    choise = input("Please enter your choise: ")
    if choise == "1":
        age = saveNewEntry(dict_by_id, list_of_id)
        if age != -1:
            sum_of_ages += age

    elif choise == "2":
        searchById(dict_by_id)
    elif choise == "3":
        printAgesAverage(sum_of_ages, list_of_id)
    elif choise == "4":
        printAllNames(dict_by_id)
    elif choise == "5":
        printAllIds(dict_by_id)
    elif choise == "6":
        printAllEntries(dict_by_id)
    elif choise == "7":
        printEntryByIndex(list_of_id)
    elif choise == "8":
        exitSystem()
    else:
        print("Error: Option [" + choise + "] does not exists. Please try again")
        continue

    holder = input("Press enter to continue ")   
    