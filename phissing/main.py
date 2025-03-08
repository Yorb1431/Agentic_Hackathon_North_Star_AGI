import re

class PhishingDetector:
    def __init__(self):
        # Lijst van verdachte woorden en frasen
        self.suspicious_keywords = [
            "urgent", "immediately", "password", "account", "verify", "login",
            "security", "update", "bank", "paypal", "irs", "social security",
            "click here", "limited time", "offer", "prize", "winner", "congratulations"
        ]
        
        # Lijst van verdachte domeinen
        self.suspicious_domains = [
            "freegiftcards.com", "winprizes.com", "bank-security.com", "paypal-update.com"
        ]

    def check_suspicious_keywords(self, email):
        # Controleer op verdachte woorden
        score = 0
        for keyword in self.suspicious_keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', email, re.IGNORECASE):
                score += 1
        return score

    def check_suspicious_links(self, email):
        # Controleer op verdachte links
        score = 0
        links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', email)
        for link in links:
            for domain in self.suspicious_domains:
                if domain in link:
                    score += 1
        return score

    def check_sender(self, email):
        # Controleer op verdachte afzenders (eenvoudige controle)
        if "noreply" in email.lower() or "no-reply" in email.lower():
            return 1
        return 0

    def analyze_email(self, email):
        # Analyseer de e-mail en geef een score
        keyword_score = self.check_suspicious_keywords(email)
        link_score = self.check_suspicious_links(email)
        sender_score = self.check_sender(email)
        
        total_score = keyword_score + link_score + sender_score
        
        # Bepaal of de e-mail phishing is op basis van de score
        if total_score >= 3:
            return total_score, "Phishing detected! Be careful with this email."
        elif total_score >= 1:
            return total_score, "Suspicious email. Proceed with caution."
        else:
            return total_score, "Email seems safe."

def main():
    print("Welcome to the Phishing Email Detector!")
    email = input("Please paste your email content here:\n")
    
    detector = PhishingDetector()
    score, result = detector.analyze_email(email)
    
    print(f"\nPhishing Score: {score}")
    print(result)

if __name__ == "__main__":
    main()