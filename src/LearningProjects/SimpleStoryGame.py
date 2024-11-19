from time import sleep

print("Willkommen zu diesem kleinen Story Game!")
print("Tauche mit ein in die atemberaunde Geschichte dieses Spiels\n")

name: str = str(input("Nenne mir deinen Namen:\n"))

start_game_variations: list = ["s", "S", "start", "Start", "start game", "Start Game", "startgame"]
quit_game_variations: list = ["q", "Q", "quit", "Quit", "quit game", "Quit Game", "quitgame"]
choice: str = None
debug_multiplier: int = 0.1

def choice2(choice: str) -> None:
    if choice == "1":
        print("1")
    elif choice == "2":
        print("2")
    elif choice == "3":
        print("3")
    else:
        print("Bitte wähle eine geltende Möglichkeit")
        try:
            choice2(choice = str(input(f"Was soll {name} machen?:\n")))
        except ValueError:
            print("Bitte wähle eine geltende Eingabe")
            choice2(choice = str(input(f"Was soll {name} machen?:\n")))

def choice1(choice: str) -> None:
    if choice == "1":
        print(f'{name} stirmt aus seinem Haus raus in den Wald')
        sleep(3 * debug_multiplier)
        print(f'Er lässt alles stehen und liegen was ihm lieb ist')
        sleep(3 * debug_multiplier)
        print(f'Aber plötzlich ertönen Siren Heads Sirenen extrem laut.... undddd')
        sleep(3 * debug_multiplier)
        print(f'Du bist tot')
        print("Game Over")
        print("1. Neustart")
        print("2. Beenden")
        choice = str(input("Was möchtest du machen?:\n"))
        if choice == "1":
            main()
        elif choice == "2":
            print("Verlasse Spiel...")
            sleep(1 * debug_multiplier)
            quit()
        else:
            print("Unbekannte Eingabe")
            print("Verlasse Spiel...")
            sleep(1 * debug_multiplier)
            quit()
    elif choice == "2":
        print(f'{name} läuft mit geballten Fäusten auf Siren Head zu')
        sleep(3 * debug_multiplier)
        print(f'Er ist in seiner Prime und schlägt auf Siren Head ein bis nicht mehr geht.')
        sleep(3 * debug_multiplier)
        print(f'Dann hörte {name} auf und schaute vorsichtig nach oben.')
        sleep(3 * debug_multiplier)
        print(f'Siren Head hatte sich runter gebäugt und seine Sirenen wurden immer lauter...')
        sleep(3 * debug_multiplier)
        print(f'Du stirbst')
        print("Game Over")
        print("1. Neustart")
        print("2. Beenden")
        choice = str(input("Was möchtest du machen?:\n"))
        if choice == "1":
            main()
        elif choice == "2":
            print("Verlasse Spiel...")
            sleep(1 * debug_multiplier)
            quit()
        else:
            print("Unbekannte Eingabe")
            print("Verlasse Spiel...")
            sleep(1 * debug_multiplier)
            quit()
    elif choice == "3":
        print(f'{name} näher sich langsam Siren Head und möchte ein Gespräch beginnen')
        sleep(3 * debug_multiplier)
        print(f'Siren Head beugt sich runter zu {name} und Siren Head macht sich bereit ihn zu töten')
        sleep(3 * debug_multiplier)
        print(f'{name} sagte: "STOP, das du die Geräusche von meinem Hund für mich gemacht hast war wunderbar :)"')
        sleep(4 * debug_multiplier)
        print(f'Sirenhead ist für einen Moment still und beugt sich wieder zurück.')
        sleep(4 * debug_multiplier)
        print(f'Sirenhead gab laute von sich. {name} konnte sie nicht verstehen aber er benutze den Google Übersetzer und verstand es:')
        sleep(4 * debug_multiplier)
        print(f'Er sagt sowas wie: "Ja das habe ich extra für sich gemacht. Komm lass uns was unternehmen"')
        sleep(4 * debug_multiplier)
        print(f'Was soll {name} jetzt machen?')
        print("1. Zum Spielplatz gehen")
        print("2. Eis essen gehen")
        print("3. Nichts tun")
        try:
            choice2(choice = str(input(f"Was soll {name} machen?:\n")))
        except ValueError:
            print("Bitte wähle eine geltende Eingabe")
            choice2(choice = str(input(f"Was soll {name} machen?:\n")))
    else:
        try:
            choice1(choice = str(input(f"Was soll {name} machen?:\n")))
        except ValueError:
            print("Bitte wähle eine geltende eingabe!")
            choice1(choice = str(input(f"Was soll {name} machen?:\n")))

def game() -> None:
    print(f'Es war ein schöner Tag und {name} machte einen Spaziergang durch den Wald')
    sleep(4 * debug_multiplier)
    print(f'Plötzlich hörte {name} eine Sirene!')
    sleep(4 * debug_multiplier)
    print(f'Es war Siren Head! {name} lief um sein leben. Weg von Siren Head in sein altes Haus')
    sleep(5 * debug_multiplier)
    print(f'Auf einmal hörte er vor seiner Haustür seinen Hund bellen.')
    sleep(4 * debug_multiplier)
    print(f'"Das konnte aber garnicht sein", dachte {name} sich. Sein Hund war schon lange verschwunden.')
    sleep(5 * debug_multiplier)
    print(f'Er öffnete die Tür und sah.... Siren Head *dun dun dunnnnnnn*')
    sleep(4 * debug_multiplier)
    print(f'Siren Head machte die Geräusche mit ihrern Sirenen. {name} dachte sich wie nett das sei!')
    sleep(5 * debug_multiplier)
    print(f'Was soll {name} jetzt machen?\n')
    print("1. Weglaufen")
    print("2. Kämpfen")
    print("3. Mit Sirenhead reden")
    try:
        choice1(choice = str(input(f"Was soll {name} machen?:\n")))
    except ValueError:
        print("Bitte wähle eine geltende eingabe!")
        choice1(choice = str(input(f"Was soll {name} machen?:\n")))

def main() -> None:
    sleep(1 * debug_multiplier)
    print("### Start Game ###")
    print("### Quit Game ###\n")
    menu_choice: str = str(input("Wähle aus was du machen möchtest:\n"))
    if menu_choice in start_game_variations:
        game()
    elif menu_choice in quit_game_variations:
        print("Verlasse Spiel...")
        sleep(1 * debug_multiplier)
        quit()
    else:
        print("Bitte wähle eine Option")
        main()

main()
