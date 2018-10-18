import requests
import xmltodict
from tkinter import *


root = Tk()

def destroyer(lijst,refresher):
        lijst[0].destroy()
        lijst[1].destroy()
        lijst[2].destroy()
        lijst[3].destroy()
        lijst[4].destroy()
        refresher.destroy()

        return begin()

def clicked(label,entry,button):
        q = 0
        stationIn = entry.get() #Verkrijgt het getypte station
        tekst = "Station: {}"
        label["text"] = tekst.format(stationIn) #Gooit de station in de tekst

        #Request de api
        response = requests.get("https://webservices.ns.nl/ns-api-avt?station=" + entry.get(), auth=(
        'luthmarnick@hotmail.com', 'xxX8_vL4EWukcoy3OQOrET9M9vDP3lHIdEj8Y1KOapRzitKuKnVw0A'))

        with open('vertrektijden.xml', 'w') as myXMLFile: #Open en schrijven in een xml file
            lijst = []
            myXMLFile.write(response.text)
            vertrekXML = xmltodict.parse(response.text)

            Button(master=root, text='Refresh', command=(button.destroy(), label.destroy(), entry.destroy()))
            #De vertrek weten
            for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein'][:5]:
                eindbestemming = vertrek['EindBestemming']

                vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
                vertrektijd = vertrektijd[11:16]  # 18:36

                #Laat de vertrektijden en eindbestemming zien
                stationText = Label(master=root,  height=2,text = 'Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming, background='#ffd72a', font='comicsansms')
                lijst.append(stationText)
                stationText.pack()

            refresh = Button(master=root, text='Refresh', command=lambda: destroyer(lijst, refresh), background='#02339a',
                                 foreground='white',
                                 font='comicsansms', )
            refresh.pack(pady=50)


def begin():
    label = Label(master=root, text='Kies een station', height = 10, background='#ffd72a', width=100, font='comicsansms')
    label.pack()

    entry = Entry(master=root)
    entry.pack(padx=10, pady=10)

    button = Button(master=root, text='Plannen', command=lambda: clicked(label,entry,button), background='#02339a', foreground='white',
                    font='comicsansms', )
    button.pack(pady=10)

    root.configure(background='#ffd72a')
    root.mainloop()

begin()
