import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


#Def functie is niet nodig, maar was handig om 'Uit te zetten' met hashtag
def mail():
    mail = input('Je mail: ')
    ww = input('WW: ')#PAS OP! Het intypen van je WW wordt niet anders weergeven, dus als iemand meekijkt kan die het zien!

    msg = MIMEMultipart()

    msg['From'] = mail
    msg['To'] = mail
    msg['Subject'] = "SUBJECT OF THE EMAIL"

    body = str(input('Schrijf je bericht: ')) + "\nVerzonden op {}".format(
        datetime.datetime.now().strftime("%B %d, %Y"))

    msg.attach(MIMEText(body, 'plain'))

    filename = 'ticker.txt'#"NAME OF THE FILE WITH ITS EXTENSION"
    attachment = open('C:/Users/Faiza/Desktop/ticker.txt', "rb")#"PATH OF THE FILE"

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    server_ssl.login(mail, ww)
    text = msg.as_string()
    server_ssl.sendmail(mail, mail, text)
    server_ssl.quit()

mail()
