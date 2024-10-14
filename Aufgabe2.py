# Aufgabe 2
# Erstelle ein Dictionary mit den Namen von 5 Mitarbeitern und ihren Positionen in einem Betrieb.
# Schreibe ein Programm, das einen Benutzer nach dem Namen fragt und entweder die Position des
# Mitarbeiters ausgibt oder "Mitarbeiter konnte nicht gefunden werden" anzeigt, wenn der Name
# nicht im Dicitonary vorhanden ist (benutze get() )


mitarbeiter_dict = {
    "Max": "Chef",
    "Franz": "nicht Chef",
    "Dieter": "Verwalter",
    "John": "Hausmeister",
    "Judas": "Verräter",
}

searched = input("Was möchtest du wissen: Franz, Max, Dieter, John oder Judas? \n")
if searched in mitarbeiter_dict:
    position = mitarbeiter_dict.get(searched)
    print(f"Der Mitarbeiter {searched} hat die Position: {position}")
else:
    print("Der Mitarbeiter Arbeitet hier nicht.")
