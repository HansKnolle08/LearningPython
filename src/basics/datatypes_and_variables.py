number = 2 # Variabeln können verschiedene Datentypen speichern
print(number) # print() Methoden können Varbiabeln in die Kommandozeile ausgeben
number = 4 # Variabeln können überschrieben werden
print(number)

number2 = 4
print(number + number2) # Variabeln können verrechnet werden

# Datentypen können umgewandelt werden
integer = int(number) # int() oder Integer ist eine Ganzzahl also -4, -1, 0, 1, 5 usw
float = float(number) # float() oder Floating Point Number ist eine Dezimalzahl also -4.5, 0.5, 3.14
string = str(number) # str() oder String ist ein Text aus Buchstaben; Zahlen und Zeichen
print(integer, float, string)
print(type(integer), type(float), type(string)) # Mit der Methode type() kann man sich den Datentypen einer Variabel ausgeben lassen

