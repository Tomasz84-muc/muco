print "Podaj mi dane o ktre poprosze: "
imie = raw_input ("Jak masz na imie? ",)
nazwisko = raw_input ("Jak masz na nazwisko? ",)
plec = raw_input ("Jaka masz plec? ",)
suma_danych = imie +" "+nazwisko+" "+plec
nazwaPliku = imie+"_"+plec+".txt"


#procedura zapisu do pliku:
file = open(nazwaPliku, "wb")
file.write(suma_danych)
print "Wlasnie przed chwila zapisalem to: ",suma_danych, " i zostaly zapisane w pliku o nazwie ",nazwaPliku
file.close ()
