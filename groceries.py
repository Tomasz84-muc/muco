groceries = ["Jablka", "Ziemniaki", "Chleb", "Mleko", "Maslo", "Pomarancze", "Salata", "Cukier", "Platki"]
gpas = [3.25, 2.26, 1.99, 3.55, 4.0, 3.21, 2.56, 3.06, 2.78]
print groceries [0]
print groceries [4]
print gpas [3]

groceries.append("Kurczak")
print groceries

gpas.append("5000")
print gpas

groceries.sort()
print "Posortowane zakupy: ", groceries

gpas.sort()
print "Posortowane: ", gpas
