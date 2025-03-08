import re

class EmailParser:
    def __init__(self, raw_email):
        self.raw_email = raw_email
        self.sender = None
        self.subject = None
        self.body = None
        self.links = []


    def parse_email(self):
        self.sender = self._parse_sender()
        self.subject = self._parse_subject()
        self.body = self._parse_body()
        self.links = self._parse_links()

    def _parse_sender(self):
        sender = re.search(r'From: (.*)\n', self.raw_email).group(1)
        return sender
    
    def _parse_subject(self):
        subject = re.search(r'Subject: (.*)\n', self.raw_email).group(1)
        return subject
    

    def _parse_body(self):
        body = re.search(r'\n\n(.*)', self.raw_email, re.DOTALL).group(1)
        return body
    
    def _parse_links(self): 
        links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.body)
        return links
    
    def get_sender(self):
        return self.sender
    
    def get_subject(self):
        return self.subject
    
    def get_body(self):
        return self.body
    

    def get_links(self):
        return self.links
    
    def get_email(self):
        return {
            "sender": self.sender,
            "subject": self.subject,
            "body": self.body,
            "links": self.links
        }

    

    