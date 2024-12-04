def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Exit")

def saveNewEntry():
    id = input("ID: ")

    if  not id.isdigit():
        printIdErrorNotNumber(id)
        return -1
    
    id = int(id)

    if id in dict_by_id.keys():
        print("Error: ID already exists: " + str(dict_by_id[id]))
        return -1

    name = input("Name: ")

    age = (input("Age: ")) 

    if not age.isdigit():
        print("Error, age must be a number. " + age + " is not a number")
        return -1 
    age = int(age)
    
    dict_by_name[name] = (id, age)
    dict_by_id[id] = (name, age)     
    # list_by_name.append(name)
    list_by_id.append(id)
    print("ID [" + str(id) + "] saved successfully")
    return int(age)
    

def searchById():
    id = input("Please enter the ID you want to look for: ")
    if not id.isdigit():
        printIdErrorNotNumber(id)
        return
    id = int(id)

    if id in dict_by_id.keys():
        printById(id)
    else:
        print("Error: ID " + str(id) + " is not saved")


def printAgesAverage():
    if num_people == 0:
        print("0")
        return
    res = sum_of_ages / num_people
    print(str(res))



def printAllNames():
    if num_people == 0:
        return
    for idx, name in enumerate(dict_by_name.keys()):
        print(str(idx) + ". " + name)



def printAllIds():
    if num_people == 0:
        return
    for idx, id in enumerate(dict_by_id.keys()):
        print(str(idx) + ". " + str(id))


def printAllEntries():
    if num_people == 0:
        return
    for idx, id  in enumerate(dict_by_id.keys()):
        print(str(idx) +  ". " + str(id))
        print(tab_str + "Name: " + dict_by_id[id][0])
        print(tab_str + "Age: " + str(dict_by_id[id][1]))


def printEntryByIndex():
    idx = input("Index: ")

    if not idx.isdigit():
        printIdnexErrorNotNumber(idx)
        return
    idx = int(idx)
    if idx >= num_people or idx < 0:
        printIdnexErrorOutOfRange(idx)
    else:
        printById(list_by_id[idx])

def exitSystem():
    flag = ""
    while flag != "y" and flag != "n":
        flag = input("Are you sure you want to exit? (y/n) ")
    if flag == "y":
        print("Goodbye!")
        exit()

def printById(id):
    print("ID: " + str(id))
    print("Name: " + dict_by_id[id][0])
    print("Age: " + str(dict_by_id[id][1]))


def printIdErrorNotNumber(id):
    print("Errorr, ID must be a number. " + id + " is not a number")

def printIdnexErrorNotNumber(idx):
    print("Error, index must be a number. " + idx + " is not a number")

def printIdnexErrorOutOfRange(idx):
    if idx >= num_people:
        print("Error, Index out of range. The maximum index allowed is " + str(num_people - 1))
    elif idx < 0:
        print("Error, Index out of range. The minimum index allowed is 0")


tab_str = "   "
dict_by_name = {}
dict_by_id = {}
# list_by_name = [] if needed further
list_by_id = []
sum_of_ages = 0
num_people = 0
while True:
    printMenu()
    choise = input("Please enter your choise: ")
    if choise == "1":
        age = saveNewEntry()
        if age != -1:
            num_people += 1
            sum_of_ages += age

    elif choise == "2":
        searchById()
    elif choise == "3":
        printAgesAverage()
    elif choise == "4":
        printAllNames()
    elif choise == "5":
        printAllIds()
    elif choise == "6":
        printAllEntries()
    elif choise == "7":
        printEntryByIndex()
    elif choise == "8":
        exitSystem()
    else:
        print("Error: Option [" + choise + "] does not exists. Please try again")
        continue

    holder = input("Press enter to continue ")   
    