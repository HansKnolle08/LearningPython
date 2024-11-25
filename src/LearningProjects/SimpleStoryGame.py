from time import sleep

print("Willkommen zu diesem kleinen Story Game!")
print("Tauche mit ein in die atemberaunde Geschichte dieses Spiels\n")

name: str = str(input("Nenne mir deinen Namen:\n"))

start_game_variations: list = ["s", "S", "start", "Start", "start game", "Start Game", "startgame"]
quit_game_variations: list = ["q", "Q", "quit", "Quit", "quit game", "Quit Game", "quitgame"]
choice: str = None
debug_multiplier: int = 0.001

def normal_ending(name: str) -> None:
    print(f'{name} zog nach Deutschland und zog sich vollständig zurück.')
    sleep(3 * debug_multiplier)
    print(f'Er hatte genug Kapital und Geld um sich ein neues Leben aufzubauen...')
    sleep(2 * debug_multiplier)
    print(f'Ende. Du hast das Normale Ende erreicht')
    main()

def good_ending(name: str) -> None:
    print(f'{name} und Siren Head starben sofort')
    sleep(3 * debug_multiplier)
    print(f'Nun war es vorbei. {name} hatte die Welt von Siren Head befreit')
    sleep(3 * debug_multiplier)
    print(f'Ende. Du hast das Gute Ende erreicht')
    main()

def choice2(choice: str) -> None:
    if choice == "1":
        print("Playground") # <- Hier weitermachen
    elif choice == "2":
        print("Eis")
    elif choice == "3":
        print(f'{name} merkt das Siren Head wieder sauer wurde.')
        sleep(3 * debug_multiplier)
        print(f'Als Sirenhead versuchte anzugreifen wich {name} aus und floh.')
        sleep(3 * debug_multiplier)
        print(f'Er lief zu dem Platz wo er sein Auto abgestellt hatte und fuhr weg')
        sleep(3 * debug_multiplier)
        print(f'Doch plötzlich taucht Siren Head vor dir auf. Er stand auf der Straße.')
        print(f'Was soll {name} jetzt machen?')
        print("1. Ausweichen")
        print("2. Rammen")
        choice = str(input("Was möchtest du machen?:\n"))
        if choice == "1":
            print("1. Links")
            print("2. Rechts")
            choice = str(input(f'{name} macht eine scharfe Kurve nach:\n'))
            if choice == "1":
                print(f'{name} starb weil er nach links abbog und in den Graben fiel')
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
                print(f'{name} macht eine scharfe Kurve nach Rechts auf die Gegenfahrbahn.')
                sleep(3 * debug_multiplier)
                print(f'Als er hinter Siren Head war gab er Vollgas und fuhr ganz weit weg.')
                sleep(3 * debug_multiplier)
                normal_ending(name)
            else:
                print(f'{name} konnte sich nicht entscheiden und starb weil Sirenhead schneller war')
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
            print(F'{name} steuert auf mit Ramkurs auf ihn zu')
            sleep(3 * debug_multiplier)
            print("Er macht die Augen zu und akzeptiert sein Schicksal")
            sleep(3 * debug_multiplier)
            print("Als das Auto und Sirenhead mit 232 KM pro Stunde kolidieren explodiert das Auto in einem großem Feuerball")
            good_ending(name)
        else:
            print(f'{name} konnte sich nicht entscheiden und starb weil Sirenhead schneller war')
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
        print(f'{name} nähert sich langsam Siren Head und möchte ein Gespräch beginnen')
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
    print(f'\nEs war ein schöner Tag und {name} machte einen Spaziergang durch einen Wald irgendwo in England\n')
    sleep(4 * debug_multiplier)
    print(f'Plötzlich hörte {name} eine Sirene!\n')
    sleep(4 * debug_multiplier)
    print(f'Es war Siren Head! {name} lief um sein leben. Weg von Siren Head in sein altes Haus\n')
    sleep(5 * debug_multiplier)
    print(f'Auf einmal hörte er vor seiner Haustür seinen Hund bellen.\n')
    sleep(4 * debug_multiplier)
    print(f'"Das konnte aber garnicht sein", dachte {name} sich. Sein Hund war schon lange verschwunden.\n')
    sleep(5 * debug_multiplier)
    print(f'Er öffnete die Tür und sah.... Siren Head *dun dun dunnnnnnn*\n')
    sleep(4 * debug_multiplier)
    print(f'Siren Head machte die Geräusche mit ihrern Sirenen. {name} dachte sich wie nett das sei!\n')
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
    print("\n### Start Game ###")
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
