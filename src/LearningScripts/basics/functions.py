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

"""
RÜCKGABEWERTE
"""
def add(a, b):
    return a + b # Return gibt einen Rückgabe Wert an.

sum = add(2, 4) # Rückgabewerte können in einer Variabel gespeichert werden
print(sum) # Diese können dann ausgegeben werden
print(add(3, 6)) # Man kann die Funktion auch direkt in der print() Methode aufrufen

def compare(a, b):
    if a == b:
        return True # Eine Funktion kann verschiedene Rückgabewerte geben
    else:
        return False
    
print(compare(3, 0))

"""
STANDARD PARAMETER
"""
def say_bye(name = 'Hans'): # Man kann einem Parameter einen Standard Wert zuweisen
    print("Bye Bye", name, "!")

 # Funktionen mit Standard Parametern geben diesen Standard Parameter aus wenn in dem Funktionsaufruf kein anderer Wert für das Parameter festgelegt wurde
say_bye() # -> Standardparameter für name wird verwendet
say_bye("Hansisi") # -> Standardparameter für name wird mit dem Parameter in dem Aufruf ersetzt