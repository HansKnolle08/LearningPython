"""
BASICS
"""
number = 2 # Variabeln können verschiedene Datentypen speichern
print(number) # print() Methoden können Varbiabeln in die Kommandozeile ausgeben
number = 4 # Variabeln können überschrieben werden
print(number)
number2 = 4
print(number + number2) # Variabeln können verrechnet werden

"""
UMWANDLUNG
"""
# Datentypen können umgewandelt werden
integer = int(number) # int() oder Integer ist eine Ganzzahl also -4, -1, 0, 1, 5 usw
float = float(number) # float() oder Floating Point Number ist eine Dezimalzahl also -4.5, 0.5, 3.14
string = str(number) # str() oder String ist ein Text aus Buchstaben; Zahlen und Zeichen
print(integer, float, string)
print(type(integer), type(float), type(string)) # Mit der Methode type() kann man sich den Datentypen einer Variabel ausgeben lassen

"""
BOOLISCHE WERTE
"""
boolean = True # True oder False sind boolische Werte. Sie werden in Kontrollstrukturen verwendet
print(boolean)
print(type(boolean))

boolean = bool(0) # Eine Zahl kann einen boolischen Wert darstellen. Dabei gilt -> alles was nicht 0 ist ist True
boolean2 = bool(1)
boolean3 = bool(9)
boolean4 = bool(-2839)
print(boolean, boolean2, boolean3, boolean4)

"""
LISTEN
"""
fruits = ["Apfel", "Birne", "Banane"] # -> Das ist eine Liste. Eine Liste ist veränderbar und steht immer in eckigen Klammern []
print(fruits) # Die ganze Liste ausgeben
print(type(fruits))
print(fruits[0]) # Das Element 0 der Liste fruits ausgeben. 0 ist immer das erste Element. Also ist das 2. Element 1. Diese Zahl nennt man Index
i = 1 # Der Variabelnname i wird am meisten für einen Index verwendet
print(fruits[i]) # Der Index kann auch eine Variabel sein
fruits.append("Orange") # Auf einer Liste kann man die Methode append() anwenden die ein Element hinzufügt und hinten anhängt
print(fruits)
fruits.remove("Orange") # Auf eine Liste kann man die Methode remove() anwenden um ein Element zu entfernen
print(fruits)
fruits[i] = "Melone" # Man kann ein Element mithilfe des Indexes anpassen
print(fruits)

"""
TUPLES
"""
coordinates = (10, 60, 123) # -> Das ist eine Tuple. Sie Sind ähnlich wie Listen aber ihre Daten sind unveränderlich
print(coordinates)
print(type(coordinates))
print(coordinates[0]) # Auch bei Tuples kann man mit einem Index bestimmte Objekte ausgeben lassen
# coordinates[1] = 50 würde einen Error auslösen

"""
SETS
"""
set1 = {"Apfel", "Birne", "Melone"} # -> Das ist ein Set. Sie sind ebenfalls ähnlich wie Listen allerdings können sie ein Element nich doppelt haben
print(set1) # Sets sind durcheinander und haben keine bestimmte Reihenfolge der Elemente
print(type(set1))
set1.add("Orange") # Mit der Methode add() kann man ein Element hinzufügen. Existiert das Element schon wird dieser Befehl ignoriert
print(set1)
set1.remove("Melone") # Mit der Methode remove() entfernt man ein Element
print(set1)
# print(set1[2]) wird einen Fehler ausgeben da man mit einem Index keine bestimmten Werte aus einem Set herausbekommt