import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Def functie is niet nodig, maar was handig om 'Uit te zetten' met hashtag
# Je kan input weg doen en daar je standaard Mail, WW of bericht inschrijven ipv te typen.
# Als je dit wil gebruiken, moet je bij je mail dit https://myaccount.google.com/lesssecureapps aan zetten
def mail():
    mail = 'viphuhl@gmail.com'
    ww = 'Joh@nHU1'  # PAS OP! Het intypen van je WW wordt niet anders weergeven, dus als iemand meekijkt kan die het zien!

    msg = MIMEMultipart()

    msg['From'] = mail
    msg['To'] = mail
    msg['Subject'] = input("Mail onderwerp: ")

    body = str(input('Schrijf je bericht: ')) + "\n\nVerzonden op {}".format(
        datetime.datetime.now().strftime("%B %d, %Y"))  # Tijd wanneer verzonden

    Attach = input('Attachment(ja/nee): ')

    msg.attach(MIMEText(body, 'plain'))

    if Attach == 'ja':

        filename = input('Filename: ')  # "NAME OF THE FILE WITH ITS EXTENSION"
        attachment = open(input('File path: '), "rb")  # "PATH OF THE FILE"

    # codeerd de attachment naar assembly code
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    server_ssl.login(mail, ww)
    text = msg.as_string()
    server_ssl.sendmail(mail, mail, text)  # Stuurt naar zichzelf
    server_ssl.quit()

mail()
