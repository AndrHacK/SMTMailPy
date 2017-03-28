import smtplib

content = "Merhaba (Test)"

mail = smtplib.SMTP("smtpgmail.com",587)

mail.eclo()

mail.starttls()

mail.login("-your mail-","-your mail pass-")

mail.sendmail("-facebook@facesec.com-","-Send Mail-",content)

