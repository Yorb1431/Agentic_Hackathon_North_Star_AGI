import re
class  FeatureExtractor:
    def __init__(self, raw_email):
        self.raw_email = raw_email
        self.sender = None
        self.subject = None
        self.body = None
        self.links = []
        self.features = {}
        
    def extract_features(self):
        self.sender = self._extract_sender()
        self.subject = self._extract_subject()
        self.body = self._extract_body()
        self.links = self._extract_links()
        self.features = self._extract_features()
        
    def _extract_sender(self):
        sender = re.search(r'From: (.*)\n', self.raw_email).group(1)
        return sender
    
    def _extract_subject(self):
        subject = re.search(r'Subject: (.*)\n', self.raw_email).group(1)
        return subject
    
    def _extract_body(self):
        body = re.search(r'\n\n(.*)', self.raw_email, re.DOTALL).group(1)
        return body
    
    def _extract_links(self): 
        links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.body)
        return links
    
    def _extract_features(self):
        return {
            "sender": self.sender,
            "subject": self.subject,
            "body": self.body,
            "links": self.links
        }
    
    def get_sender(self):
        return self.sender
    
    def get_subject(self):
        return self.subject
    
    def get_body(self):
        return self.body
    
    def get_links(self):
        return self.links
    
    def get_features(self):
        return self.features