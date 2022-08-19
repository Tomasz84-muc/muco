#Program zawiera funkcje if else elif

import random


haslo = input ("Jestem firma bezpieczeninstawa IT prowadz haslo: ")

if haslo == "sekret":
    print ("Zalogowano!")
    print ("Musisz byc kims bardzo waznym")

else:
    print ("Odmowa dostepu.")
    input ("Napisnij ENTER, aby zakonczyc")




print ("Wyczuwam twoj nastruj przez klawiature i kamerke i jest on taki:")


mood = random.randint(1, 3)

if mood == 3:
    print(":)")

elif mood == 2:
    print(":|")

elif mood == 1:
    print(":(")


print ("\nNa dzisiaj")

input ("Nacisnij Enter aby zakonczyc")
