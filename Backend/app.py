from flask import Flask, render_template, request
import re
from abc import ABC, abstractmethod

app = Flask(__name__)

# --- E-mail en analyzers ---

class Email:
    """
    Vertegenwoordigt een e-mail met onderwerp, afzender en inhoud.
    """
    def __init__(self, subject: str, sender: str, content: str):
        self.subject = subject
        self.sender = sender
        self.content = content
    
    def full_text(self) -> str:
        """
        Combineert onderwerp en inhoud tot één tekst voor analyse.
        """
        return f"{self.subject} {self.content}"

class Analyzer(ABC):
    """
    Abstracte basis klasse voor alle e-mail analyzers.
    """
    @abstractmethod
    def analyze(self, email: Email) -> int:
        pass

class KeywordAnalyzer(Analyzer):
    """
    Analyseert de e-mail op basis van bekende phishing-sleutelwoorden.
    """
    def __init__(self, keywords=None):
        if keywords is None:
            self.keywords = [
                "urgent", "click here", "update your account", "verify", 
                "login", "confirm", "password", "suspend", "immediately", 
                "security", "account", "bank", "limited time", "act now", 
                "risk", "warning"
            ]
        else:
            self.keywords = keywords
    
    def analyze(self, email: Email) -> int:
        score = 0
        text = email.full_text().lower()
        for keyword in self.keywords:
            if keyword in text:
                score += 1
        return score

class LinkAnalyzer(Analyzer):
    """
    Analyseert de e-mail op verdachte links.
    """
    def analyze(self, email: Email) -> int:
        score = 0
        # Zoek naar http(s) links
        links = re.findall(r'http[s]?://\S+', email.full_text())
        score += len(links)
        return score

class ExclamationAnalyzer(Analyzer):
    """
    Controleert of de e-mail overmatig gebruikmaakt van uitroeptekens.
    """
    def analyze(self, email: Email) -> int:
        score = 0
        exclamations = email.full_text().count("!")
        if exclamations > 3:
            score += 1
        return score

class PhishingDetector:
    """
    Combineert alle analyzers om te bepalen of een e-mail phishing is.
    """
    def __init__(self):
        self.analyzers = [
            KeywordAnalyzer(),
            LinkAnalyzer(),
            ExclamationAnalyzer()
        ]
    
    def evaluate(self, email: Email) -> int:
        total_score = 0
        for analyzer in self.analyzers:
            total_score += analyzer.analyze(email)
        return total_score
    
    def interpret_score(self, score: int) -> str:
        if score >= 5:
            return "Waarschuwing: Deze e-mail lijkt phishing te zijn!"
        elif score >= 3:
            return "Let op: Deze e-mail vertoont enkele phishing kenmerken."
        else:
            return "Deze e-mail lijkt veilig te zijn."

# --- Web routes ---

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        subject = request.form.get("subject", "")
        sender = request.form.get("sender", "")
        content = request.form.get("content", "")
        email = Email(subject, sender, content)
        detector = PhishingDetector()
        score = detector.evaluate(email)
        interpretation = detector.interpret_score(score)
        result = {
            "score": score,
            "interpretation": interpretation
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
