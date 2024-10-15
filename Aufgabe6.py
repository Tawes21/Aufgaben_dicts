# Aufgabe 6
# Du findest ein Dictionary mit Ländern als Schlüssel und deren Bevölkerungszahlen als Wert.
# Schreibe ein Programm, das die Länder nach Namen sortiert und in alphabetischer Reihenfolge
# die Namen ausgibt

countries = {
    "Deutschland": 85000000,
    "Frankreich": 68000000,
    "Spanien": 47000000,
    "Polen": 36000000,
}


def sort():
    sorted_country = {key: sorted(str(value)) for key, value in countries.items()}
    return sorted_country.keys()


print(sort())
