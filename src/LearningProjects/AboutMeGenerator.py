print("Hallo :D Willkommen zu diesem Generator\n")
name = str(input("Nenne mir zuerst deinen Namen:\n"))
straße = str(input("Sag uns wo du wohnst:\n"))
age = int(input("Jetzt dein Alter:\n"))
birthdate = str(input("Jetzt brauche ich deinen Geburtstag:\n"))
desc = str(input("Beschreib dich:\n"))

print(f'\nHallo!, mein Name ist {name} und ich wohne in der {straße}.\n Ich bin {age} alt und wurde am {birthdate} geboren.\n So bin ich:\n {desc}')