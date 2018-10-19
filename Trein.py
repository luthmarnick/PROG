import requests
import xmltodict
from tkinter import *
from tkinter.messagebox import showinfo


root = Tk()
root.maxsize(700, 675)  #zet de maximale grote van de window
root.minsize(700, 675)  #zet de minimale grote van de window
img = Image('photo', file='logoNS.png')
root.call('wm', 'iconphoto', root._w,img)   #zet het plaatje als icoon neer

#De def die de clicked() verwijderd en terug zet naar begin()
def destroyer(lijst,refresher):
    #De code hieronder zorgt ervoor dat de vertrek teksten zullen worden verwijderd
    q = 0
    while True:
        lijst[q].destroy()
        q +=1 #q gaat tot 10 en dan stopt het en zullen de teksten verwijderd zijn
        if q == 10:
            break
    refresher.destroy()#Verwijderd de refresh button

    return begin()

#De def die de vertrektijden en bestemmingen laat zien
def clicked(label,entry,button):
    try:
        lijst = []

        #Request de api
        response = requests.get("https://webservices.ns.nl/ns-api-avt?station=" + entry.get(), auth=(
        'luthmarnick@hotmail.com', 'xxX8_vL4EWukcoy3OQOrET9M9vDP3lHIdEj8Y1KOapRzitKuKnVw0A'))

        with open('vertrektijden.xml', 'w') as myXMLFile: #Open en schrijven in een XML File
            myXMLFile.write(response.text)
            vertrekXML = xmltodict.parse(response.text)

            #Verwijderd de button,label en entry van begin()
            button.destroy()
            label.destroy()
            entry.destroy()

            #De vertrek tijden en bestemmingen vinden in de XML File
            for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein'][:10]: #Dit zal zich 10 keer repeaten
                eindbestemming = vertrek['EindBestemming']
                spoor = vertrek['VertrekSpoor']['#text'] #geeft het spoor waarop de trein rijd weer

                vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
                vertrektijd = vertrektijd[11:16]  # 11:16 geeft het tijd format aan
                #print(vertrektijd['VertrekTijd'])

                #Laat de vertrektijden en eindbestemming zien
                stationText = Label(master=root,  height=2,text = 'Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming +' op spoor ' + spoor,
                                    background='#ffd72a', font='comicsansms')
                #Doet de stationText in de lijst en we gebruiken de lijst om daarmee de teksten te verwijderen
                lijst.append(stationText)
                stationText.pack()

            #De button die ervoor zorgt dat het terug gaat naar het begin scherm, de '#02339a' is de blauwe NS kleur
            refresh = Button(master=root, text='Refresh', command=lambda: destroyer(lijst, refresh), background='#02339a',
                                 foreground='white',
                                 font='comicsansms', )
            refresh.pack(pady=50)

    #Bij een keyerror zal dit zich uitvoeren
    except KeyError:
        showinfo(title='Error', message='Verkeerde invoer!')#Een pop-up error scherm
        return begin() #Dit zorgt ervoor dat het terug gaat naar het beginscherm
    #Bij een andere error zal dit zich uitvoeren
    except:
        showinfo(title='Error', message='Er ging iets verkeerd')
        return begin()


#Def begin() is waar het programma start
def begin():
    #Dit zorgt voor de tekst
    label = Label(master=root, text='Kies een station', height = 10, background='#ffd72a', width=50, font='comicsansms')
    label.pack()

    #Hierin kan je de gewenste station schrijven
    entry = Entry(master=root)
    entry.pack(padx=10, pady=10)

    #De button zorgt ervoor dat het clicked def zal starten
    button = Button(master=root, text='Plannen', command=lambda: clicked(label,entry,button), background='#02339a',
                    foreground='white', font='comicsansms', )
    button.pack(pady=10)

    root.configure(background='#ffd72a')#De NS geel achtergrond
    root.title('NS Treinen') #Veranderd de titel
    root.mainloop()

begin()#Begint het programma
