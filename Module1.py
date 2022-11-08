'''


Dit is het bestand van de ZUIL opdracht

'''

# Hier importeer ik csv(om naar de file te schrijven)
# datetime(voor de datum en tijd)
# en random(voor een random keuze van 3 stations)
import csv
import datetime
import random

# Lijstje van stations
stations = ['Utrecht','Zwolle','Amsterdam']

# Kies een random station
gekozen_station = random.choice(stations)






# Een while loop die vraagt om naam en een bericht
# Deze loop blijft doorgaan omdat dan een klant altijd iets kan invoeren
while True:
    # Datum van vandaag, en in de goede volgorde
    vandaag = datetime.datetime.now()
    datum_en_tijd = vandaag.strftime("%d-%m-%Y %H:%M:%S")
    naam = input('Wat is uw naam, Als u liever anoniem wilt blijven vul niks in: ')
    if naam == '':
        naam = 'Anoniem'

# Het bericht mag geen komma en mag niet langer dan 140 karakters zijn

    bericht = input('Geef uw mening over het NS-Station: ')
    while len(bericht) > 140 or ',' in bericht:
        print('Sorry, maar u mag maximaal 140 karakters invoeren en geen komma\'s')
        bericht = input('Geef uw mening over het NS-Station: ')

# Hier maak ik een variabele aan met kommas zodat ik die makkelijk kan splitten
    opslaan = f'{naam},{bericht},{datum_en_tijd},{gekozen_station}\n'

# Hier open ik de file en schrijf ik naar het csv bestand en daarna sluit ik hem weer
    openfile = open('ZUIL.csv','a')
    openfile.write(opslaan)
    openfile.close()





