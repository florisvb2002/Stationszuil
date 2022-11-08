import requests
from tkinter import *
import psycopg2
from PIL import Image, ImageSequence
import random
import textwrap


conn = psycopg2.connect(
    database = "postgres",
    host = 'localhost',
    port = '5432',
    password = 'Bommel2011',
    user = 'postgres'
)

conn.autocommit = True
cursor = conn.cursor()


# Hier vraag ik om de berichten die goedgekeurd zijn
cursor.execute('''SELECT * FROM keuring WHERE status = 'Goedgekeurd' ORDER BY Tijd desc LIMIT 5 ''')

# Hier geef ik ze een variabele
alle = cursor.fetchall()

# Als er minder dan 5 berichten zijn goedgekeurd sluit het programma
if len(alle) in range(0,4):
    exit('Nog niet genoeg data')

# Hier geef ik elk bericht een variabele
zin1 = alle[0][3]
zin2 = alle[1][3]
zin3 = alle[2][3]
zin4 = alle[3][3]
zin5 = alle[4][3]


# berichten een uiterlijke grens laten aangeven
zin1 = zin1.replace("\n", " ")
# functie wrapped gebruiken voor het aantal tekens
zin1wrap = textwrap.fill(zin1, 70)

zin2 = zin2.replace("\n", " ")
zin2wrap = textwrap.fill(zin2, 70)

zin3 = zin3.replace("\n", " ")
zin3wrap = textwrap.fill(zin3, 70)

zin4 = zin4.replace("\n", " ")
zin4wrap = textwrap.fill(zin4, 70)

zin5 = zin5.replace("\n", " ")
zin5wrap = textwrap.fill(zin5, 70)

# berichten op een rij pla
# Lijstje van stations
stations = ['Utrecht','Zwolle','Amsterdam']

# Kies een random station
gekozen_station = random.choice(stations)


if gekozen_station == 'Utrecht':
# Hier vraag ik welke faciliteiten er zijn in Utrecht
    cursor.execute('''SELECT elevator, ov_bike, toilet, park_and_ride FROM faciliteit WHERE station_city = 'Utrecht' ''')
    faciliteitenUtrecht = cursor.fetchall()

# Hier maak ik een lege lijst aan voor welke faciliteiten er in utrecht zijn
    lstfaciliteitenGekozenstation = []

# Hier kijk ik of de faciliteiten er zijn en als ze er zijn dan voeg ik ze toe aan de lijst
    if faciliteitenUtrecht[0][0] == True:
        lift = 'Lift'
        lstfaciliteitenGekozenstation.append(lift)

    if faciliteitenUtrecht[0][1] == True:
        ov_fiets = 'Ov_Fiets'
        lstfaciliteitenGekozenstation.append(ov_fiets)

    if faciliteitenUtrecht[0][2] == True:
        toilet = 'Toilet'
        lstfaciliteitenGekozenstation.append(toilet)

    if faciliteitenUtrecht[0][3] == True:
        park_en_ride = 'P+R'
        lstfaciliteitenGekozenstation.append(park_en_ride)


if gekozen_station == 'Amsterdam':
# Hier doe ik hetzelfde maar dan voor Amsterdam
    cursor.execute('''SELECT elevator, ov_bike, toilet, park_and_ride FROM faciliteit WHERE station_city = 'Amsterdam' ''')
    faciliteitenAmsterdam = cursor.fetchall()
    lstfaciliteitenGekozenstation = []

    if faciliteitenAmsterdam[0][0] == True:
        lift = 'Lift'
        lstfaciliteitenGekozenstation.append(lift)

    if faciliteitenAmsterdam[0][1] == True:
        ov_fiets = 'Ov_Fiets'
        lstfaciliteitenGekozenstation.append(ov_fiets)

    if faciliteitenAmsterdam[0][2] == True:
        toilet = 'Toilet'
        lstfaciliteitenGekozenstation.append(toilet)

    if faciliteitenAmsterdam[0][3] == True:
        park_en_ride = 'P+R'
        lstfaciliteitenGekozenstation.append(park_en_ride)


if gekozen_station == 'Zwolle':
# Hier doe ik hetzelfde voor Zwolle
    cursor.execute('''SELECT elevator, ov_bike, toilet, park_and_ride FROM faciliteit WHERE station_city = 'Zwolle' ''')
    faciliteitenZwolle = cursor.fetchall()
    lstfaciliteitenGekozenstation = []

    if faciliteitenZwolle[0][0] == True:
        lift = 'Lift'
        lstfaciliteitenGekozenstation.append(lift)

    if faciliteitenZwolle[0][1] == True:
        ov_fiets = 'Ov_Fiets'
        lstfaciliteitenGekozenstation.append(ov_fiets)

    if faciliteitenZwolle[0][2] == True:
        toilet = 'Toilet'
        lstfaciliteitenGekozenstation.append(toilet)

    if faciliteitenZwolle[0][3] == True:
        park_en_ride = 'P+R'
        lstfaciliteitenGekozenstation.append(park_en_ride)



# Link van API
api_link = f"https://api.openweathermap.org/data/2.5/weather?q={gekozen_station}&appid=b1ab4d54a6e1cee3e0e19ef164cf829e"

# Hier roep ik de API op van het station
response = requests.get(api_link)
# Hier zet ik hem in een jsonfile
response_data = response.json()

# Hier haal ik de gegevens uit de json file en zet 1 om in graden en rond af op 1 decimaal
graden_station = round(float(response_data['main']['temp'])-272,1)
weer_station = response_data['weather'][0]['main']


# Hier open ik tkinter
root = Tk()
root.title(f'Scherm{gekozen_station}')
root.state("zoomed")

root.config(background='blue')


# Dit heb ik uit een video https://www.youtube.com/watch?v=YtnMgiLbJCU
gifImage = 'train-passing-by.gif'
openImage = Image.open(gifImage)

frames = openImage.n_frames

imageObject = [PhotoImage(file=gifImage, format=f'gif -index {i}') for i in range(frames)]

count = 0

showAnimation = None

def animation(count):
    global showAnimation
    newImage = imageObject[count]

    gif_Label.configure(image=newImage)
    count +=1
    if count == frames:
        count = 0
    showAnimation = root.after(50, lambda: animation(count))

gif_Label = Label(root, image="")
gif_Label.place(relx=0.5, rely=0.1, anchor=CENTER)

animation(count)

weerberichten = f'{gekozen_station}: {graden_station} ℃\nWeerbericht: {weer_station}'

faciliteitberichten = f'{gekozen_station}:\n{lstfaciliteitenGekozenstation[0]} en {lstfaciliteitenGekozenstation[1]}'

station = Label(root, text=f'{gekozen_station} Centraal', font=75, background='yellow')

berichtlabel = Label(root, text='Berichten:', font=('Arial', 25), justify=LEFT, background='yellow')

faciliteitlabel = Label(root, text='Faciliteiten:', font=('Arial', 25), justify=RIGHT, background='yellow')

weerlabel = Label(root, text='Weer:', font=('Arial', 25), background='yellow')

weerStation = Label(root, text=weerberichten, justify=LEFT,font=('Arial', 10), background='yellow')

faciliteitenlabel= Label(root, text=faciliteitberichten, justify=LEFT, font=('Arial', 10), background='yellow')

eerste_5_zinnen = Label(root, text=f'{zin1wrap}\n\n{zin2wrap}\n\n{zin3wrap}\n\n{zin4wrap}\n\n{zin5wrap}', justify=LEFT, font=('Arial', 10), background='yellow')


station.place(relx=0.5, rely=0.1, anchor=CENTER)
berichtlabel.place(x=10, y=300)
eerste_5_zinnen.place(x=10, y=350)
faciliteitlabel.place(x=550, y=300)
faciliteitenlabel.place(x=550, y=350)
weerlabel.place(x=1100, y=300)

weerStation.place(x=1100, y=350)



root.mainloop()

