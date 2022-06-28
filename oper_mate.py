print("To sa operatory matematyczne ktore portafie zrobic w Python:")
print("\nDodawanie:\n \t7+3=", 7+3)
print("\nOdejmowanie:\n \t7-3=",7-3)
print("\nMnozenie:\n \t7*3=", 7*3)
print("\nDzielenie:\n \t7/3=", 7/3)
print("\nDzielenie bez liczny dziesietnej:\n \t7//3=", 7//3)
print("\nModulo:\n \t7%3=",7%3) 






print("\n\nTo komputer przeliczyl automatycznie, jesli chcesz mam inna zabawe!")

odp = input("Jesli chce sie pobawic wcisnij przycisk \"Y\"")
if odp == 'Y' or 'y' or 'Yes' or 'Tak' or 't' or 'tak' or 'yes':
    print("To bawimy sie dalej!\n")
else:
    exit()


print("\n\n\nA moze Ty bedziesz wprowadzal dane a ja je oblicze?\n\n\tZaczynajmy! :)")

liczba1 = int(input("Dodawanie! podaj dwie liczby:\nPierwsza:"))
liczba2 = int(input("Druga:"))
print("Wynik: ", liczba1 + liczba2)
print("\n\nTo bylo dodwanie, Sprobujmy odjmowanie twoich liczb:")


liczba1 = int(input("Odejmowanie! podaj dwie liczby:\nPierwsza:"))
liczba2 = int(input("Druga:"))
print("Wynik: ", liczba1 - liczba2)
print("\n\nTo bylo odejmowanie, teraz mnozenie:")


liczba1 = int(input("Mnozenie! podaj dwie liczby:\nPierwsza:"))
liczba2 = int(input("Druga:"))
print("Wynik: ", liczba1 * liczba2)
print("\n\nTo bylo mnozenie, teraz dzielenie:")


liczba1 = int(input("Dzielenie! podaj dwie liczby:\nPierwsza:"))
liczba2 = int(input("Druga:"))
print("Wynik: ", liczba1 / liczba2)
print("\n\nTo bylo dzielenie, teraz modulo?")



odp = input("Jesli chcesz sie bawic dalej nacisnij \"Y\".")
if odp == "Y"or 'y' or 'Yes' or 'Tak' or 't' or 'tak' or 'yes':
    print("No to jazda! :)")
else:
    exit()


liczba1 = int(input("Tym razem nie modulo, ale przed tym dzielenie bez liczby dziesietnej:\nPierwsza: "))
liczba2 = int(input("Druga:"))
print("Wynik: ", liczba1 // liczba2)
print("\n\nTo byl wynik dzielenia bez liczb dziesietnych. Teraz czas na ostatnie czyli modulo")


liczba1 = int(input("Modulo!, podaj dwie liczby:\nPierwsza:"))
liczba2 = int(input("Druga"))
print("Wynik: ", liczba1 % liczba2)


print("A czy wiesz co to modulo?")


odp_modulo = input("Jesli chcesz wiedziec co to modulo wpisz \"Modulo\".")
    
if odp_modulo == "Modulo":
    print("Operacja wyznaczania reszty z dzielenia jednego typu liczbowego przez drugi.")
else:
    input("TY ignorancie! nacisnij ENTER, aby zakonczyc program")





#w Python3 nie ma raw_input!
#aby chcesz zeby wprowadzony 'text' byl traktowany jako liczby uzyj int /jak wyzej/




input("\n\nAby zakonczyc program, nacisnij ENTER.")
