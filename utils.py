import pandas as pd
from enum import Enum
from employee import Employee 
from student import Student

class Menu(Enum):
    SAVE_NEW_ENTRY = "1"
    SEARCH_BY_ID = "2"
    PRINT_AGES_AVERAGE = "3"
    PRINT_ALL_NAMES = "4"
    PRINT_ALL_IDS = "5"
    PRINT_ALL_ENTRIES = "6"
    PRINT_ENTRY_BY_INDEX = "7"
    SAVE_ALL_DATA = "8"
    EXIT = "9"

def isvowel(char):
    return char.lower() in "aeiou"


def printMenu():
    idx = 1
    for option in Menu:
        print(str(idx) + ". " + option.name.replace("_", " ").capitalize())
        idx += 1

types_of_person = [Employee, Student]

def saveNewEntry(dict_by_id, list_of_person):
    try:
        id = checkParamIsNumber("ID")
        if id in dict_by_id:
            print("Error: ID already exists: ", end="")
            print(dict_by_id[id].getName() + " - " + str(dict_by_id[id].getAge()))
            return 0

        name = input("Please enter the name: ")

        age = checkParamIsNumber("age")
    except ValueError as e:
        return 0
    
    for idx, person in enumerate(types_of_person):
        str_to_print = str(person).replace("<class '", "").replace("'>", "").split(".")[0]
        if isvowel(str_to_print[0]):
            articule = "an"
        else:
            articule = "a"
        print("If you are " + articule + " " + str_to_print + " - press " + str(idx))

    type_of_person = None
    while type_of_person != "0" and type_of_person != "1":
        type_of_person = input()

    type_of_person = int(type_of_person)
    person = types_of_person[type_of_person](id, name, age)
    
    dict_by_id[id] = person
    list_of_person.append(person)     
    print("ID [" + str(id) + "] saved successfully")
    return int(age)
    

def searchById(dict_by_id):
    try:
        id = checkParamIsNumber("ID")
    except ValueError as e:
        return
    
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



def printAllIds(list_of_person):
    [print(str(idx) + ". " + str(person.getId())) for idx, person in enumerate(list_of_person)]


def printAllEntries(list_of_person):
    [person.printMySelf(idx)  for idx, person in enumerate(list_of_person)]



def printEntryByIndex(list_of_person):
    try:
        idx = checkParamIsNumber("Index")
    except ValueError:
        return

    if idx >= len(list_of_person) or idx < 0:
        printIndexErrorOutOfRange(idx, len(list_of_person))
    else:
        list_of_person[idx].printPerson()


def saveAllData(list_of_person):
    output_filename = input("What is your output file name? ")

    peolpe_list = []
    for person in list_of_person:
        curr_raw = {}
        curr_raw["id"] = person.getId()
        curr_raw["name"] = person.getName()
        curr_raw["age"] = person.getAge()
        curr_raw["field"] = person.getField()
        if isinstance(person, Employee):
            curr_raw["income"] = person.getSalary()
        else:
            curr_raw["year of study"] = person.getYear()
            curr_raw["average score"] = person.getAvg()
        
        peolpe_list.append(curr_raw)

    people_df = pd.DataFrame(peolpe_list)
    people_df.to_csv(output_filename, index = False)


def exitSystem():
    flag = None
    while flag != "y" and flag != "n":
        flag = input("Are you sure you want to exit? (y/n) ")
    if flag == "y":
        print("Goodbye!")
        exit()

def checkParamIsNumber(param_name, float_value = False):

    param = input("Please enter the " + param_name + ": ")
    try:
        if float_value:
            return float(param)
        else:
            return int(param)
    except ValueError as e:
        printParamErrorNotNumber(param, param_name)
        raise e
    
def printParamErrorNotNumber(param, param_name):
    print("Error, " + param_name + " must be a number. " + param + " is not a number")

def printIndexErrorNotNumber(idx):
    print("Error, index must be a number. " + idx + " is not a number")

def printIndexErrorOutOfRange(idx, num_people):
    if idx >= num_people:
        print("Error, Index out of range. The maximum index allowed is " + str(num_people - 1))
    elif idx < 0:
        print("Error, Index out of range. The minimum index allowed is 0")
