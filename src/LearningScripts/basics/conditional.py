"""
IF STRUKTUR
"""
if 2 > 1: # -> if ist das Schlüsselwort für eine Bedingung.
    print("2 ist größer als 1")
    """
    Der Code der hier steht wird ausgeführt wenn die Bedingung war ist als True ist
    """

"""
IF-ELSE STRUKTUR
"""
user_input = input("Gib dein Passwort ein:\n") # -> mit der Methode input() kann man Eingaben aus der Kommandozeile tätigen. Diese Eingabe wird in der Variabel gespeichert
password = "passwort123"

if user_input == password: # Man kann Variabeln vergleichen
    print("Zugriff gewährt")
    """
    Dieser Block wird ausgeführt wenn die Bedingung True ergibt
    """
else: # else ist das Schlüsselwort für einen "oder" Bereich
    print("Zugriff verweigert")
    """
    Dieser Block wird ausgeführt wenn die Bedingung False ergibt
    """

"""
ELIF STRUKTUR
"""
i = 1
if i == 2:
    print(i)
elif i == 1: # elif is das Schlüsselwort um nach einem if Block eine weitere Bedingung einzufügen
    print(i)
else:
    print(i)