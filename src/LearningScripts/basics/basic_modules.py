import time # Mit dem Schlüsselwort import können Module in das Skript eingefügt werden

# Bsiepiel für time Modul
print("Hallo")
time.sleep(2) # Der Code wartet 2 Sekunden
print("Welt!")

import math as m # Man kann einem Modul mit as einen anderen Namen geben um den Code übersichtlicher zu halten
print(m.pi) # pi ist eine Konstante in dem Modul math

from math import sqrt # Man kann auch nur bestimmte Elemente aus einem Modul importieren
sqrt(1) # Direkt importierte Methoden oder andere Elemente können direkt eingefügt ohne davor den namen des Moduls zu schreiben

"""
BASIC MODULE
"""
import math
import time