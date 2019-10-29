from random import randint

def try_number():
    
    x = randint(0, 99)
    y = -1
    print("Ich habe mir eine Zahl zwischen 0 und 100 überlegt.")
    print("Versuche die Zahl mit möglichs wenig Versuchen zu erraten.")
    
    while y != x:
        try:
            y_str = input("Rate eine Zahl zwischen 0 und 100: ")
            y = int(y_str)
            if int(y) < x:
                print(" Die Zahl ist zu klein! Rate ein Zahl die über deiner letzten Zahl liegt.")
            elif x == y:
                print("Du hast richtig geraten")
            elif int(y) > x:
                print("Die Zahl ist zu groß! Rate eine Zahl die unter deiner letzten Zahl liegt.")
        except ValueError:
            print("Deine Eingabe muss eine Zahl sein!")
    print("Du hast die richtige Zahl erraten! Glückwunsch!")        


try_number()





