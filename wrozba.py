#Program ktory symuluje ciasteczko z wrozba.
#Program powinien wyslwietlic jedna z pieciu nie powtarzalnych przepowiedni, dokonujac losowego wyboru przy kazdym uruchomieniu

import random

wrozba = random.randrange(5) + 1


if wrozba == 1:
    print ("Bedziesz zdrowy i bogaty!!")
elif wrozba == 2:
    print ("Bedziesz szczesliwy")
elif wrozba == 3:
    print ("Bedziesz duzo podrozowa!")
elif wrozba == 4:
    print ("Bedziesz bardzo dobry w programowaniu!")
elif wrozba == 5:
    print ("Duzo wytrwalosci!")

input ("Nacisnij ENTER aby zakonczyc")



#1 = "Bedziesz zdrowy i bogaty!!"
#2 = "Bedziesz szczesliwy"
#3 = "Bedziesz duzo podrozowa!"
#4 = "Bedziesz bardzo dobry w programowaniu!"
#5 = "Duzo wytrwalosci!"


#print (wrozba)

