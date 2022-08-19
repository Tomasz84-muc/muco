print ("Tylko dla czlonkow ekskluzywnej sieci!")

security = 0
username = ""
while not username:
    username = input ("Uzytkownik: ")


password = ""
while not password:
    password = input ("Haslo: ")

if username == "Tomasz" and password == "Dupa":
    print("Jestes zalogowany!")

elif username == "Kamila" and password == "Cipa":
    print("Jestes zalogowany")

elif username == "gosc" or password == "gosc":
    print ("Jestes zalogowany")

else: 
    print ("Odmowa dostepu")
