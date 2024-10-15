# Aufgabe 4
# Erstelle ein Dicitonary mit dem Namen und dem Alter von 3 Personen. Schreibe ein Programm, das durch die Schlüssel des
# Dictionaries iteriert und nur die Namen der Personen ausgibt

name_dict = {
    "Max": 15,
    "Peter": 19,
    "Martina": 21,
}


def keylist():
    keys = name_dict.keys()
    print(keys)


keylist()
