"""
BASICS
"""
# "Type Annotations" sind ein extra in Python mit dem den Code verständlicher machen kann
text: str = "Hallo" # -> Diese Annotation sagt das die Variabel text dein Datentyp String hat
print(text)

number: str = 2 # -> Sowas ist zwar falsch da die 2 ein Integer ist die Variabel aber als String annotiert wurde
print(type(number)) # -> Der Typ der Variabel entspricht jedoch immer dem tatsächlichen Datentyp des Wertes der Variabel
print(number) # Das heißt ich kann einen Integer als String annotieren aber der Datentyp der Variabel ist trotzdem der des Wertes

# Man kann diese Annotations auch auf Funktionen anwenden.
def hello(name: str) -> str: # Man kann annotieren welchen Typ ein Parameter bekommen soll und welcher Typ der Rückgabewert ist
    return f'Hallo {name}'

print(hello("Hans"))

# Man in einer Funktion auch Variationen von Typen einfügen. a und b sollen entweder ein Integer oder eine Float sein
def add(a: int | float, b: int | float) -> int | float: # Der Rückgabe ist auch entweder ein Integer oder eine Float
    return a + b

print(add(3, 5))