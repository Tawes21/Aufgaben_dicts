# Aufgabe 1
# Erstelle ein Dictionary, da die Noten eines Schülers in verschiedenen Fächern speichert.
# Schreibe ein Programm, das die Note für ein Fach abfragt und ausgibt. Verwende get() und
# fange mit if und else einen Fehler ab, falls das Fach nicht existiert.

noten_dict = {
    "Mathe": 1,
    "Deutsch": 5,
    "Sport": 1,
    "Chemie": 3,
    "Biologie": 3,
    "Kunst": 5,
}

x = "Mathe"
if noten_dict[x] > 0:
    note = noten_dict.get(x)

else:
    print(f"Du wurdest in {x} nit benotet!")

print(f"Du hast in Mateh eine: {note}")
