import csv

add = {}
definitions = {}


with open('dictionary.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    definitions = dict(reader)


def show():
    appellation = input("Type appellation you want know: ").upper()
    if definitions.get(appellation):
        print(appellation.upper())
        print("\n"+"".join(str((definitions.get(appellation)))).strip('()').
              replace("'", "").replace("[", "").replace("]", ""))
    else:
        print("\nThere's not such a appellation\n"
              "Add this appellation, tuple and source if u can")


# adding new element (appellation, tuple, source)
def adding():
    definition_appellation = input("Please enter appellation: ").upper()
    # http://python-textbok.readthedocs.io/en/1.0/Loop_Control_Statements.html#using-loops-to-simplify-code
    for prop in ["explanation", "source"]:
        add[prop] = input("Please enter %s: " % prop)
    definitions[definition_appellation] = ([str(add["explanation"])], [str(add["source"])])
    # saving definition into the .csv file
    # https://pythonspot.com/en/save-a-dictionary-to-a-file/
    w = csv.writer(open("dictionary.csv", "w"))
    for key, val in definitions.items():
        w.writerow([key, val])


# sort list in alphabetical order
def show_alphabetically():
    print("\nAll appellations alphabetically:\n")
    for key in sorted(definitions.keys()):
        print(key)


# main loop for menu
while True:

    menu = input("""\nDictionary for a little programmer:
1) search explanation by appellation
2) add new definition
3) show all appellations alphabetically
0) exit\n
Enter the number: """)

    if menu == "1":
        show()

    elif menu == "2":
        adding()

    elif menu == "3":
        show_alphabetically()

    else:
        if menu != "0":
            print("\nUncorrect vaule")
        elif menu == "0":
            print("\nSee you!\n")
            exit()
