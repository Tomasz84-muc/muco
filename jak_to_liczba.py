#To bedzie gra gdzie masz odnalesc liczbe od 1 do 100 
#wpisz jakies wyjsnienia zebys wiedzial za kilka miesiecy co miales na mysli z tym programem
#cokolwiek im wiecej tym lepiej kod przepisuje z ksiazki "Python dla Kazdego" Michale Dawson
#17.07.22 Piekna pogoda niedzile ja pisze kod. Michal u Kulow a Nicola bawi sie tarasie bez barierek 

print("Hej witaj w Grze \"Jaka To Liczba\"\nSprobuj odgadnac liczbe od 1 do 100\n\tDobrej Zabawy!!!")   #Napisz przywitanie

import random                                                               #importuje modul random

numer = random.randint(1, 100)                                              #losuje liczbe od 1 do 100 ktora jest zmienna o nazwie numer

proba = int(input("\nPodaj swoja liczbe: "))                                  #grac jest poproszony o podanie liczby ktora staje sie zmienna o nazwie proba

liczba_prob = 1                                                             # zmienna liczba_prob jest rowna 1



while proba != numer:                                                      #dopoki zmiennna proba nie jest rowna 1

    if liczba_prob == 5:                                                    #jezeli zmienna liczba_prob bedzie rowna 5 
        print ("\nWykorzystales",liczba_prob, "prob na odgadniecia wylosowanej liczby.\nByla to liczba",numer, "Dziekujemy za zabawe i zapraszamy ponownie\n\n") #to wyswitl ten text
        input ("Nacisnij Enter, aby zakonczyc.")                            #enter bedzie nowa zmienna
        break                                                               #wyjdz z petli

    if proba > numer:                                                       #jezeli  zmienna proba jest mniejsza niz zmienna numer
        print("\tLiczba jest mniejsza")                                       #wtedy wyswietl Liczba jest mniejsza
        proba = int(input("\nPodaj liczbe mniejsza: "))                       #gracz proszony jest o kolejan liczbe ktora staje sie nowa zmienna proba
        liczba_prob += 1                                                    #do zmiennej liczba_prob jest dodwana 1 
            
    else:                                                                   #inaczej
          print ("\tLiczba jest wieksza")                                     #wyswietl text
          proba = int(input("\nZaproponuj liczbe wieksza: "))                 #uzytkownik wprowadzi nowa zmienna proba
          liczba_prob += 1                                                  #dodaj 1 do zmiennej liczba_prob



if proba == numer:                                                          #jezeli zmienna proba jest rowna zmiennej numer
    print ("\nUdalo Ci sie odgadnac liczbe! Gratulacje!!! Szukana liczba to: ",numer, "\nZajelo ci to ", liczba_prob, "proby")   #to wyswietl text
    input ("\n\nNacisnij ENTER, aby zakonczyc.")
