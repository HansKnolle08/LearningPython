from time import sleep

print("Willkommen zu diesem kleinen Story Game!")
print("Tauche mit ein in die atemberaunde Geschichte dieses Spiels\n")

name: str = str(input("Nenne mir deinen Namen:\n"))

sleep(1)

start_game_variations: list = ["start", "Start", "start game", "Start Game", "startgame"]
quit_game_variations: list = ["quit", "Quit", "quit game", "Quit Game", "quitgame"]
choice: str = None

def section1(choice: str) -> None:
    if choice == "1":
        print(choice)
    elif choice == "2":
        print(choice)
    elif choice == "3":
        print(choice)
    else:
        try:
            section1(choice = str(input(f"Was soll {name} machen?:\n")))
        except ValueError:
            print("Bitte wähle eine geltende eingabe!")
            section1(choice = str(input(f"Was soll {name} machen?:\n")))

def game() -> None:
    print(f'Es war ein schöner Tag und {name} machte einen Spaziergang durch den Wald')
    sleep(4)
    print(f'Plötzlich hörte {name} eine Sirene!')
    sleep(4)
    print(f'Es war Siren Head! {name} lief um sein leben. Weg von Siren Head in sein altes Haus')
    sleep(5)
    print(f'Auf einmal hörte er vor seiner Haustür seinen Hund bellen.')
    sleep(4)
    print(f'"Das konnte aber garnicht sein", dachte {name} sich. Sein Hund war schon lange verschwunden.')
    sleep(5)
    print(f'Er öffnete die Tür und sah.... Siren Head *dun dun dunnnnnnn*')
    sleep(4)
    print(f'Siren Head machte die Geräusche mit ihrern Sirenen. {name} dachte sich wie nett das sei!')
    sleep(5)
    print(f'Was soll {name} jetzt machen?\n')
    print("1. Weglaufen")
    print("2. Kämpfen")
    print("3. Mit Sirenhead reden")
    try:
        section1(choice = str(input(f"Was soll {name} machen?:\n")))
    except ValueError:
        print("Bitte wähle eine geltende eingabe!")
        section1(choice = str(input(f"Was soll {name} machen?:\n")))

def main() -> None:
    print("### Start Game ###")
    print("### Quit Game ###\n")
    menu_choice: str = str(input("Wähle aus was du machen möchtest:\n"))
    if menu_choice in start_game_variations:
        game()
    elif menu_choice in quit_game_variations:
        print("Verlasse Spiel...")
        sleep(1)
        quit()
    else:
        print("Bitte wähle eine Option")
        main()

main()