"""
FUNKTIONEN
"""
def say_hi(): # So deklariert man eine Funktion. def steht für define und danach kommt der name der Funktion. Ein Funktionsname sollte immer klein geschrieben sein
    print("Hi")
    """
    Der Code in diesem Block wird ausgeführt wenn die Funktion aufgerufen wird
    """

say_hi() # Funktionsaufruf

"""
PARAMETER
"""
def say_hello(name): # Diese Methode verwendet einen Parameter der in der Funktion verwendet wird
    print("Hello", name, "!") # So kann man in einer print() Funktion Variabeln mit Text mischen

say_hello("Hans") # Funktionsaufruf mit Parameter