#program symulujacy rzut moneta
#rzuca 100 razy i zlicza ile wypadla raszka a ile orzel
#dopoki-->while


import random


reszka = 0
orzel  = 0
ilosc_prob = 0
pierdolnik = int(input("Prosze podac ile rzucic koscia:"))
while ilosc_prob != pierdolnik:
  
    kostka = random.randrange(2) + 1
    if kostka == 1:
        reszka += 1
    else:
        kostka == 2
        orzel += 1
    ilosc_prob += 1

print ("Program rzucil koscia..")
print ("Ilosc prob: ", ilosc_prob)
print ("Reszka: ",reszka)
print ("Orzel: ",orzel)
