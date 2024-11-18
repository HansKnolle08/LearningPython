import time as t

print("WIllkommen zu diesem kleinen Story Game!")
print("Tauche mit ein in die atemberaunde Geschichte dieses Spiels\n")

t.sleep(1)

start_game_variations = ["start", "Start", "start game", "Start Game", "startgame"]
quit_game_variations = ["quit", "Quit", "quit game", "Quit Game", "quitgame"]

def game(name):
    print(name)

def main():
    print("###Start Game###")
    print("###Quit Game###\n")
    menu_choice = str(input("Wähle aus was du machen möchtest:\n"))
    if menu_choice in start_game_variations:
        game(name = str(input("Sag mir deinen Namen:\n")))
    elif menu_choice in quit_game_variations:
        print("Verlasse Spiel...")
        t.sleep(1)
        quit()
    else:
        print("Bitte wähle eine Option")
        main()

main()