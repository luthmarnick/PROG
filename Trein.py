import requests
import xmltodict
from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.maxsize(700, 675)  #zet de maximale grote van de window
root.minsize(700, 675)  #zet de minimale grote van de window
img = Image('photo', file='logoNS.png')
root.call('wm', 'iconphoto', root._w,img) #zet het plaatje als icoon neer

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
def clicked(label,entry,button,stoppen):
    try:
        lijst = []

        #Request de api
        response = requests.get("https://webservices.ns.nl/ns-api-avt?station=" + entry.get(), auth=(
        'luthmarnick@hotmail.com', 'xxX8_vL4EWukcoy3OQOrET9M9vDP3lHIdEj8Y1KOapRzitKuKnVw0A'))

        with open('vertrektijden.xml', 'w') as myXMLFile: #Open en schrijven in een XML File
            myXMLFile.write(response.text)
            vertrekXML = xmltodict.parse(response.text)

            #Verwijderd de buttons,label en entry van begin()
            button.destroy()
            label.destroy()
            entry.destroy()
            stoppen.destroy()

            #De vertrek tijden en bestemmingen vinden in de XML File
            for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein'][:10]: #Dit zal zich 10 keer repeaten
                eindbestemming = vertrek['EindBestemming']
                spoor = vertrek['VertrekSpoor']['#text'] #geeft het spoor waarop de trein rijd
                soort = vertrek['TreinSoort'] #De treinsoort

                vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
                vertrektijd = vertrektijd[11:16]  # 11:16 geeft het tijd format aan

                #Laat de vertrektijden en eindbestemming zien
                stationText = Label(master=root,  height=2,text = 'Om '+vertrektijd+' vertrekt een ' + soort + ' naar '+ eindbestemming +' op spoor ' + spoor,
                                    background='#ffd72a', font='Comic')
                #Doet de stationText in de lijst en we gebruiken de lijst om daarmee de teksten te verwijderen
                lijst.append(stationText)
                stationText.pack()

            #De button die ervoor zorgt dat het terug gaat naar het begin scherm, de '#02339a' is de blauwe NS kleur
            refresh = Button(master=root, text='Refresh', command=lambda: destroyer(lijst, refresh), background='#02339a',
                                 foreground='white',
                                 font='Comic', )
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
    label = Label(master=root, text='Kies een station', height = 10, background='#ffd72a', width=50, font='Comic')
    label.pack()

    #Hierin kan je de gewenste station schrijven
    entry = Entry(master=root)
    entry.pack(padx=10, pady=10, ipadx=100)

    #De button zorgt ervoor dat het clicked def zal starten
    button = Button(master=root, text='Plannen', command=lambda: clicked(label,entry,button,stoppen), background='#02339a',
                    foreground='white', font='Comic', )
    button.place(x=225,y=250)

    stoppen = Button(master=root, text='Stoppen', command=root.destroy, background='#02339a', #Stopt het programma
                    foreground='white', font='Comic', )

    stoppen.place(x=400,y=250)

    root.configure(background='#ffd72a')#De NS geel achtergrond
    root.title('NS Treinen') #Veranderd de titel
    root.mainloop()

begin()#Begint het programma

if __name__ == "__main__":
    import doctest
    doctest.testmod()
