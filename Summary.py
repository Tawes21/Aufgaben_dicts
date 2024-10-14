# DICTIONARIES (OBJEKTE)

product = {
    "id": "12345",
    "name": "Holzschrauben",
    "amount": 1000,
    "price": 19.99,
}

product["name"] = "Metallschrauben"  # ändert den Wert an der Stelle "name"
product["size"] = "18x30"  # wenn der Wert nicht existiert, wird er hinzugefügt

del product["price"]  # löscht das Key Value Paar direkt aus dem Dictionary
deleted_entry = product.pop(
    "amount"
)  # wirft das letzte Key Value Paar raus und liefert es zurück


product.get(
    "name"
)  # Gibt den Wert eines Schlüssels zurück, wenn der Schlüssel nicht existiert, wirft es None zurück anstatt einen Key Error
# Beispiel: test = product.get("name")

product.keys()  # Gibt eine Liste aller Schlüssel im Dictionary zurück.
# Beispiel: test = product.keys()

product.values()  # Gibt alle Werte eines Dictionaries zurück
# Beispiel: test = product.values()

product.update(
    {"amount": 500}
)  # fügt neue Paare hinzu oder aktualisiert vorhandene Key Value Paare

# product.clear() # Entfernt alle Elemente aus dem Dictionary

testkopie = product.copy()  # Erstellt eine Kopie des Dictionaries

# product.popitem() # Entfernt den zuletzt hinzugefügten Eintrag aus dem Dictionary
# test_pop = product.popitem

# print(test_pop)

print(product)
