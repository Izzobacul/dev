import smtplib
from Email import Email

class Gmail:
    def __init__(self, username, password):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(username, password)

    def send(self, email: Email):
        self.server.sendmail(email.username, email.to, email.mail)

if __name__ == '__main__':
    email = Email('example@gmail.com', 'example@example.com', 'Hey how are you!', 'Hello there :)')

    gmail = Gmail('example@gmail.com', 'password123')
    gmail.send(email)
