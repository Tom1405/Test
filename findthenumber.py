from random import randint

def try_number():
    
    x = randint(0, 99)
    y = -1
    r = 0 #Runden
    print("Ich habe mir eine Zahl zwischen 0 und 100 überlegt.")
    print("Versuche die Zahl mit möglichs wenig Versuchen zu erraten.")
    
    while y != x:
        try:
            y_str = input("Rate eine Zahl: ")
            y = int(y_str)
            r = r + 1
            if int(y) < x:
                print(" Die Zahl ist zu klein! Rate ein Zahl die über deiner letzten Zahl liegt.")
            elif int(y) > x:
                print("Die Zahl ist zu groß! Rate eine Zahl die unter deiner letzten Zahl liegt.")
            else:
                print("Du hast richtig geraten")         
        except ValueError:
            print("Deine Eingabe muss eine Zahl sein!")
    print("Glückwunsch!")
    print(f"Du hast {r} Versuche benötigt.")


try_number()




