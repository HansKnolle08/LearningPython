"""
BASICS
"""

i = 5 # -> Diese Variabel ist ein Integer
print(type(i))

text = "Hallo Welt" # -> Diese Variabel ist ein String
print(type(text))

# print(i + text) -> Dieser Aufruf würde einen TypeError auslösen
# Das liegt daran das die beiden Variabeln nicht den selben Typ haben
# Man kann keinen String mit einem Integer verrechnen

"""
HANDLING
"""
# die try-except Struktur ist die Struktur für das Error Handling
# Es bedeutet:
# "Versuche diesen Code auszuführen, wenn ein Error oder Exception kommt führe diesen Code aus"
try:
    print(i + text) # Das würde einen TypeError auslösen
except TypeError: # Hier bezieht man sich direkt auf diesen Error
    print("Das geht nicht") # Dieser Code wird ausgeführt wenn eine TypeError auftritt

try:
    print(2 + "Hi") # Es geht auch nicht wenn man keine Variabeln verwendet
except Exception as e: # Wenn man das so verwendet wird jeder Error abgefangen und in der Variabel e gespeichert
    print(e) # Diesen als e gespeicherten Error können wir ausgeben lassen