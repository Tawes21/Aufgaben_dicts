# Aufgabe 3
# Erstelle ein Dictionary, das 5 Lebensmittel und ihre Preise enthält. Baue eine Funktion, die neue Produkte und
# deren Preise speichert. Erweitere deine Funktion, indem du nach einem
# Artikel suchst und gib ihn mit seinem Preis aus. Wenn der Artikel nicht gefunden wurde, soll der Artikel gespeichert werden und einen
# Standardpreis von 0 zurückgegeben

food_dict = {
    "Obst": 2.99,
    "Fleisch": 15.99,
    "Tk Pizza": 21.99,
    "Fisch": 25.99,
    "Kaese": 32.99,
}


def update():
    new_item = input("Welcher Artikel soll hinzugefügt werden?: ")
    if new_item in food_dict:
        print(f"{new_item} " f"{food_dict.get(new_item)}")
    else:
        food_dict.update({new_item})
        print("Der Artikel wurde angelegt, derzeitiger preis 0€")


update()
