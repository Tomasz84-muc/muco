imie = raw_input ("Jak masz na imie? ")
email = raw_input ("Jaki jest twoj adres e-mail? ")
zespol = raw_input ("Jaki jest twoj ulubiony zespol? ")
outputString = imie + "|" + email + "|" + zespol
nazwaPliku = imie + "_" + zespol + ".txt"

#plik bedzie stworzony tak:
#wb - to tak zwany tryb pliku ze jest otwierany z prawami do zapisu.
file = open(nazwaPliku, "wb")
file.write(outputString)
print outputString , "zapisano w pliku ", nazwaPliku
file.close()
