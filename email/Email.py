class Email:
    def __init__(self, sender, to, subject, body):
        self.sender = sender
        self.to = to
        self.subject = subject
        self.body = body
        self.mail = f"From: {self.sender}\nTo: {self.to}\nSubject: {self.subject}\n\n{self.body}"
    def __str__(self):
        return(self.mail)
