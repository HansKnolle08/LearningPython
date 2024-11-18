"""
FOR-SCHLEIFEN
"""
for i in range(10): # Eine For-Schleife wird zum Durchlaufen einer Sequenz (das ist entweder eine Liste, ein Tupel, ein Dictonary oder eine Zeichenfolge) verwendet.
    print(i) # Hier zählt die Schleife 10 mal wegen der Methode range() in der die Reichweite eingegeben wird

fruits = ["Apfel", "Banane", "Birne"]
for x in fruits: # Diese Schleife durchläuft die Liste fruits bis keine Elemente mehr vorhanden sind
    print(x)

for y in fruits[1]: # Diese Schleife durchläuft ein Wort
    print(y)

inventory = ["Schwert", "Schild", "Apfel", "Gold-Erz", "Stein", "Glass", "Spitzhacke"]
for z in inventory: # Diese Schleife durchläuft die Liste inventory
    if z == "Apfel": # Die Schleife sucht nach dem Element Apfel
        print(z)
        break # Wenn das Element gefunden wurde wird die Schleife beendet

color = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in color: # Diese Schleife durchläuft die Liste color
  for y in fruits: # Diese Schleife durchläuft die Liste fruits
    print(x, y) # Jedes mal wenn die Äussere Schleife einen Durchlauf gemacht hat zählt innere Schleife

"""
WHILE-SCHLEIFEN
"""
index = 0
while not index == 10: # While Schleifen führen Code solange aus wie eine Bedingung True ist
    print(index)
    index += 1 # Diese Schleife hat einen negierten Zähler. Das heisst solang index nicht gleich 10 ist wird gezählt

"""
Diese Schleife ist unendlich da sie zählt solange die Bedingung True ist
Hier ist True eine Konstante deshalb läuft sie bis das Programm unterbochen wird

while True:
    print("Hi")
"""