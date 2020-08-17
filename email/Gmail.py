import smtplib
from Email import Email

class Gmail:
    def __init__(self, username, password):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(username, password)

    def send(self, email: Email):
        self.server.sendmail(email.sender, email.to, email.mail)
