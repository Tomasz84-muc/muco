from datetime import date
today = date.today().isoformat()
print
zuzycie_prad = input ("Podaj jakie masz zyczycie pradu: ",)
zuzycie_gaz = input ("Podaj jakie masz zuzycie gazu: ",)
zuzycie_woda = input ("Podaj jakie masz zycucie wody: ",)

oblicz_prad = 0.6 * zuzycie_prad

oblicz_gaz = (8.67+8.42)+((zuzycie_gaz*11.271)*0.10895)+((zuzycie_gaz*11.271)*0.04143)

vat = oblicz_gaz * 0.23

oblicz_woda = (6.06 + 8.14) + ((zuzycie_woda * 5.48)+(zuzycie_woda * 7.54))

suma_prad = oblicz_prad
suma_gaz = oblicz_gaz + vat
suma_woda = oblicz_woda
suma_calosc = oblicz_prad + oblicz_woda + oblicz_gaz





print
print
print
print "---------------------------------"
print "Odczyt z dnia: ",today
print "---------------------------------"
print
print "Za PRAD w tym miesiacu zaplacisz: ",suma_prad,"PLN"
print "Za GAZ w tym miesiacu zaplacisz: ",suma_gaz,"PLN"
print "Za WODE w tym miesiacu zaplacisz: ",suma_woda,"PLN"
print
print "Suma= ",suma_calosc
print

