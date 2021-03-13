import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "ilhami01201@gmail.com"

mesaj["To"] = "ilhami01201@gmail.com"

mesaj["Subject"] = "Smtp Mail Gönderme"


yazi = """

Smtp ile mail gönderiyorum.

ilo


"""


mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("ilhami01201@gmail.com","ilhami34")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail Başarıyla Gönderildi....")

    mail.close()

except:
    sys.stderr.write("Bir sorun oluştu!")
    sys.stderr.flush()
