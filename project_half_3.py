import os
import json
import pandas as pd
from employee import Employee # type: ignore
from student import Student # type: ignore

def printMenu():
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Save all data")
    print("9. Exit")

def saveNewEntry(dict_by_id, list_of_person):

    id = checkParamIsNumber(input("ID: "), "ID")
    if id == -1:
        return 0

    if id in dict_by_id:
        print("Error: ID already exists: " + str(dict_by_id[id]))
        return 0

    name = input("Name: ")

    age = checkParamIsNumber(input("Age: "), "age")
    if age == -1:
        return 0
    
    flag = None
    while flag != "1" and flag !="2":
        flag  = input("If you are an employee - press 1, if you are a student - press 2: ")

    if flag == "1":
        field = input("Field of work: ")

        salary = checkParamIsNumber(input("Salary: "), "salary",)
        if salary == -1:
            return 0
        
        person = Employee(id, name, age, field, salary)
    else:
        field = input("Field of study: ")
        year = checkParamIsNumber(input("Year of study: "), "year of study")
        if year == -1:
            return 0
        avg = checkParamIsNumber(input("Average score: "), "avegare score", float_value=True)
        if avg == -1:
            return 0
        person = Student(id, name, age, field, year, avg)
    
    dict_by_id[id] = person
    list_of_person.append(person)     
    print("ID [" + str(id) + "] saved successfully")
    return int(age)
    

def searchById(dict_by_id):
    id = input("Please enter the ID you want to look for: ")
    
    id = checkParamIsNumber(id, "ID")
    if id == -1:
        return -1

    if id in dict_by_id:
        dict_by_id[id].printPerson()
    else:
        print("Error: ID " + str(id) + " is not saved")


def printAgesAverage(sum_of_ages, list_of_person):
    if len(list_of_person) == 0:
        print("0")
        return
    res = sum_of_ages / len(list_of_person)
    print(str(res))



def printAllNames(list_of_person):
    for idx, person in enumerate(list_of_person):
        print(str(idx) + ". " + person.getName())



def printAllIds(dict_by_id):
    for idx, person in enumerate(list_of_person):
        print(str(idx) + ". " + str(person.getId()))


def printAllEntries(list_of_person):
    for idx, person  in enumerate(list_of_person):
        person.printMySelf(idx)


def printEntryByIndex(list_of_person):
    idx = input("Index: ")

    if not idx.isdigit():
        printIndexErrorNotNumber(idx)
        return
    idx = int(idx)

    if idx >= len(list_of_person) or idx < 0:
        printIndexErrorOutOfRange(idx, len(list_of_person))
    else:
        list_of_person[idx].printPerson()


def saveAllData(list_of_person, path_to_conf):
    output_filename = input("What is your output file name? ")
    if not os.path.exists(path_to_conf):
        print("Error: Config file conf.json is missing in path " + os.getcwd())
        return

    with open(path_to_conf) as conf_json:
        conf = json.load(conf_json)
        id_table_tile = conf["id"]
        name_table_title = conf["name"]
        age_table_title = conf["age"]

    peolpe_list = []
    for person in list_of_person:
        curr_raw = {}
        curr_raw[id_table_tile] = person.getId()
        curr_raw[name_table_title] = person.getName()
        curr_raw[age_table_title] = person.getAge()
        peolpe_list.append(curr_raw)

    people_df = pd.DataFrame(peolpe_list)
    people_df.to_csv(output_filename, index = False)


def exitSystem():
    flag = ""
    while flag != "y" and flag != "n":
        flag = input("Are you sure you want to exit? (y/n) ")
    if flag == "y":
        print("Goodbye!")
        exit()

def checkParamIsNumber(param, param_name, float_value = False):
    if not float_value:
        if  not param.isdigit():
            printParamErrorNotNumber(param, param_name)
            return -1
        
        return int(param)    
    else:
        split_of_float = param.strip().split(".")
        if (not split_of_float[0].isdigit()) or (not split_of_float[1].isdigit()) or len(split_of_float) != 2:
            print(split_of_float)
            printParamErrorNotNumber(param, param_name)
        return float(param)

def printParamErrorNotNumber(param, param_name):
    print("Error, " + param_name + " must be a number. " + param + " is not a number")

def printIndexErrorNotNumber(idx):
    print("Error, index must be a number. " + idx + " is not a number")

def printIndexErrorOutOfRange(idx, num_people):
    if idx >= num_people:
        print("Error, Index out of range. The maximum index allowed is " + str(num_people - 1))
    elif idx < 0:
        print("Error, Index out of range. The minimum index allowed is 0")


tab_str = "   "
dict_by_id = {}
list_of_person = list()
sum_of_ages = 0
while True:
    printMenu()
    choise = input("Please enter your choise: ")
    if choise == "1":
        age = saveNewEntry(dict_by_id, list_of_person)
        sum_of_ages += age

    elif choise == "2":
        searchById(dict_by_id)
    elif choise == "3":
        printAgesAverage(sum_of_ages, list_of_person)
    elif choise == "4":
        printAllNames(list_of_person)
    elif choise == "5":
        printAllIds(list_of_person)
    elif choise == "6":
        printAllEntries(list_of_person)
    elif choise == "7":
        printEntryByIndex(list_of_person)
    elif choise == "8":
        saveAllData(list_of_person, "conf.json")
        continue
    elif choise == "9":
        exitSystem()
    else:
        print("Error: Option [" + choise + "] does not exists. Please try again")
        continue

    holder = input("Press enter to continue ")   
    