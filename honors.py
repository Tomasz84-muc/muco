srednia = input("Jaka byla twoja srednia w ostatniej klasie? ")
godziny = input("Jaka byla twoja srednia uczesniczenia w zajeciach (w godzinach) ")

if srednia > 3.5 and godziny > 12:
	print("Gratulujemy zanalazles sie na liscie honorowej!")
else:
	print("Przykro nam, powodzemnia w przyszlosci.")

if srednia == 3.5 or godziny == 12:
	print("Jestes szczesciarzem! Jestes na liscie rezerwowej!")
