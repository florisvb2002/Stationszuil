

# Hier importeer ik csv(om naar de file te schrijven)
# datetime(voor de datum en tijd)
# psycopg2(het connecten van de database in pgAdmin)


import datetime
import psycopg2
import csv


# Hier open ik de csv file in r en maak een variabele aan van de oudste zin

file_open = open('ZUIL.csv','r')
oudste_zin = file_open.readline()

# EN maak ik een andere variabele aan die ik daarna schrijf naar een ander csv bestand
goede_zin = oudste_zin.replace('\n','')

file_open.close()

# Print oudste zin voor moderator
print(oudste_zin)

# Hier verwijder ik de oudste zin
infile = open('ZUIL.csv', 'r')
data = infile.read().splitlines(True)
infile.close()

file = open('ZUIL.csv', 'w')
file.writelines(data[1:])
infile.close()


# Hier split ik hem dus op komma die ik had geschreven in de csv file
# En geef daarbij de bijhorende variabelen
zin = oudste_zin.split(',')
naam = zin[0]
bericht = zin[1]
datum = zin[2]
station = zin[3]


# Moderator kan naam invullen
naam_moderator = input('Naam van moderator: ')

# Moderator kan email invullen
email_moderator = input('E-mail van moderator: ')

# Hier kan de moderator invullen of het goedgekeurd is
keuring = input("Typ g voor goedgekeurd en a voor afgekeurd: ")

# Hier een variabele voor de tijd van de keuring
vandaag = datetime.datetime.now()
datum_en_tijd = vandaag.strftime("%d-%m-%Y %H:%M:%S")

# If keuring is gelijk aan g dan is de status Goedgekeurd
if keuring == "g":
    status = "Goedgekeurd"
# Else Afgekeurd
else:
    status = "Afgekeurd"

# Hier schrijf ik de keuring naar het csv bestand
data = f'{goede_zin},{naam_moderator},{email_moderator},{status},{datum_en_tijd}\n'
open_goedkeuring = open('goedkeuring.csv','a')
open_goedkeuring.write(data)
open_goedkeuring.close()




# Hier connect ik naar de database in pgAdmin

conn = psycopg2.connect(
    database = "postgres",
    host = 'localhost',
    port = '5432',
    password = 'Bommel2011',
    user = 'postgres'
)

conn.autocommit = True
cursor = conn.cursor()



# Hier geef ik variabelen die ik daaronder door middel van execute naar de database schrijf
moderator_database = 'INSERT INTO moderator(Naam, Email) VALUES(%s, %s)'
bericht_database ='INSERT INTO bericht(bericht, Naam, Tijd, Station_naam) VALUES(%s, %s, %s, %s)'
keuring_database ='INSERT INTO keuring(Tijd, Status, bericht_keuring, moderator_naam) VALUES (%s, %s, %s, %s)'


cursor.execute(moderator_database, (naam_moderator, email_moderator))
cursor.execute(bericht_database, (bericht, naam, datum, station))
cursor.execute(keuring_database, (datum_en_tijd, status, bericht, naam_moderator))





