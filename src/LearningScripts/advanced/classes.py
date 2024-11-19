"""
KLASSEN
"""
"""
Python ist eine objektorientierte Programmiersprache.
Fast alles in Python ist ein Objekt mit seinen Eigenschaften und Methoden.
Eine Klasse ist wie ein Objektkonstruktor oder eine „Blaupause“ zum Erstellen von Objekten.
"""
from hmac import new
from sys import builtin_module_names


class MyClass: # Klassen definiert man mit dem Schlüsselwort "class". Der Name einer Klasse sollte immer mit großem Anfangsbuchstaben geschrieben werden
    x: int = 5

MeineKlasse1 = MyClass() # So erstellt man ein Objekt einer Klasse
print(MeineKlasse1.x) # Dann kann ich damit auf dieses Objekt zugreifen und Datem und Methoden daraus verwenden

"""
Die obigen Beispiele sind Klassen und Objekte in ihrer einfachsten Form und sind in realen Anwendungen nicht wirklich nützlich.
Um die Bedeutung von Klassen zu verstehen, müssen wir die integrierte Funktion __init__() verstehen.
Alle Klassen haben eine Funktion namens __init__(), die immer ausgeführt wird, wenn die Klasse initiiert wird.
Die Funktion __init__() wird verwendet, um Objekteigenschaften Werte zuzuweisen oder andere Vorgänge auszuführen, die beim Erstellen des Objekts erforderlich sind
"""
class Person:  # Definiert eine Klasse namens "Person", die eine Vorlage für Personen-Objekte darstellt
    def __init__(self, name: str, age: int) -> None:  
        # Der Konstruktor der Klasse. Er wird automatisch aufgerufen, wenn ein neues Objekt der Klasse erstellt wird.
        # Parameter:
        # - name: der Name der Person (Typ: String)
        # - age: das Alter der Person (Typ: Integer)
        # Die Rückgabe ist None, da der Konstruktor kein Wert zurückgibt.
        self.name = name  # Die Instanzvariable "name" wird mit dem übergebenen Parameter initialisiert.
        self.age = age    # Die Instanzvariable "age" wird mit dem übergebenen Parameter initialisiert.

# Man kann beliebig viele Instanzen eines Objekts erstellen mit verschiedenen Parametern
person1 = Person(name = 'Hans', age = 16)
person2 = Person(name = 'Christoph', age = 8)
person3 = Person(name = 'Christian', age = 48)

print(person1.age)
print(person2.name)
print(person3) # -> Das representiert die Klasse ohne eine __str__() Methode

class Person1:
    def __init__(self, age: int, name: str) -> None:
        self.age = age
        self.name = name

    def __str__(self) -> str:
        return f'{self.name}, {self.age}'
    
person4 = Person1(name = 'Hansisi', age = 16)
print(person4) # -> Das representiert die Klasse mit einer __str__() Methode

# Die __str__() Methode wird immer dann aufgerufen wenn man ein Objekt direkt ausgeben möchte

class Car:
    def __init__(self, color: str, ps: int, speed: int) -> None:
        self.color = color
        self.ps = ps
        self.speed = speed

    def __str__(self) -> str:
        return f'Object "Car" with Attributes: {self.color, self.ps, self.speed}'
    
    def change_color(self, new_color: str): # Das ist eine Klassen Methode mit der man verschiedene Dinge mit der Instanz anstellen kann
        self.color = new_color

myCar = Car(color = "Green", ps = 900, speed = 320)
print(myCar.color)
myCar.change_color(new_color = "Red")
print(myCar.color)