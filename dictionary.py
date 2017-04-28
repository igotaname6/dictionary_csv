import csv
import sys

def read_from_csv():
    with open('dict.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        prog_dict = {}
        for row in reader:
            prog_dict[row[0]] = (row[1], row[2])
        return prog_dict

def add_definition():
    appelation = input("Add an appelation name: ")
    explenation = str(input("Add the explenation: "))
    source = input("Add the source of the explenation: ")
    with open('dict.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter = ",")
        writer.writerow([appelation.upper(), explenation, source])

def search_explenation(dictionary):
    appelation =  input("Enter an appelation to find its definition: \n").upper()
    if dictionary.get(appelation) == None:
        print("I can't find this definition. \n")
    else:
        print("definition: \n", dictionary[appelation][0], "\nsource:\n", dictionary[appelation][1] )

def show_key_list(dictionary):
    key_list = sorted(dictionary)
    for item in key_list:
        print(item)

while True:

    prog_dict = read_from_csv()
    menu = (open('menu.txt', 'r'))
    print(menu.read())
    option = input("Give the number: ")

    if option == "1":
        search_explenation(prog_dict)
        press_key = None
        press_key = input("Press any key to continue ")
        if press_key == True:
            continue

    elif option == "2":
        add_definition()
        print("You added the definition ")

    elif option == "3":
        show_key_list(prog_dict)
        press_key = None
        press_key = input("Press any key to continue ")
        if press_key == True:
            continue

    elif option == "0":
        break

    else:
        continue
