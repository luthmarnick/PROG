import requests
import xmltodict
from tkinter import *


# Make a get request to get the latest position of the international space station from the opennotify api.

root = Tk()

def clicked():
        stationIn = entry.get() #Verkrijgt het getypte station
        tekst = "Station: {}"
        label["text"] = tekst.format(stationIn) #Gooit de station in de tekst

        response = requests.get("https://webservices.ns.nl/ns-api-avt?station=" + entry.get(), auth=(
        'luthmarnick@hotmail.com', 'xxX8_vL4EWukcoy3OQOrET9M9vDP3lHIdEj8Y1KOapRzitKuKnVw0A')) #Request de api

        with open('vertrektijden.xml', 'w') as myXMLFile: #Open en schrijven in een xml file
            myXMLFile.write(response.text)

            vertrekXML = xmltodict.parse(response.text)

            #De vertrek weten
            for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
                eindbestemming = vertrek['EindBestemming']

                vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
                vertrektijd = vertrektijd[11:16]  # 18:36

                #Laat de vertrektijden en eindbestemming zien
                label1 = Label(master=root, text='Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming, height=2, background='yellow')

                label1.pack()
                root.mainloop()


label = Label(master=root, text='Type', height = 2, background='yellow')
label.pack()

button = Button(master=root, text='Druk hier', command=clicked)
button.pack(pady=10)

entry = Entry(master=root)
entry.pack(padx=10, pady=10)

root.mainloop()

