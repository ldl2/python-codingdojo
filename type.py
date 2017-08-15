new_dct = {
    "sI": 45,
    "mI": 100,
    "bI": 455,
    "eI": 0,
    "spI": -23,
    "sS": "Rubber baby buggy bumpers",
    "mS": "Experience is simply the name we give our mistakes",
    "bS": "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
    "eS": "",
    "aL": [1, 7, 4, 21],
    "mL": [3, 5, 7, 34, 3, 2, 113, 65, 8, 89],
    "lL": [4, 34, 22, 68, 9, 13, 3, 5, 7, 9, 2, 12, 45, 923],
    "eL": [],
    "spL": ['name', 'address', 'phone number', 'social security number'],
}


def integers(x):
    if(x >= 100):
        print("That's a big number!")
    else:
        print("That's a small number!")


def strings(x):
    if(x.count("") < 50):
        print("Short sentence.")
    else:
        print("Long sentence.")


def lists(x):
    if(len(x) < 10):
        print("Short List!")
    else:
        print("Big List!")

y = raw_input("Please select sI, mI, bI, eI, spI, sS, mS, bS, eS, aL, mL, lL, eL, spL: ")
x = new_dct.get(y)


def run(x):
    if(type(x) == int):
        integers(x)
    elif(type(x) == str):
        strings(x)
    else:
        lists(x)

run(x)


