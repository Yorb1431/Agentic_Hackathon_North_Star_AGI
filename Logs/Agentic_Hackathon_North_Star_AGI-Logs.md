# Agentic_Hackathon_North_Star_AGI
## Brainstorm
- ## brainstorm Phising e-mail detecter
- De gebruiker ontvangt een e-mail
- De Gebruker plaats de e-mail in de detecter bot
-De bot controleert de e-mail en analyseert hem ook
- De bot geeft een score als het phissing of echt is. 

Plan van aanpak
Onderzoek en Data Verzamelen

Verzamel een dataset met phishing- en legitieme e-mails.
Kijk naar patronen in phishing-e-mails (zoals verdachte links, afzenderadres, spellingfouten, en verzoeken om gevoelige informatie).
Project Structuur Opzetten

Maak een duidelijke mapstructuur (bijvoorbeeld main.py, email_analyzer.py, model.py, etc.).
Gebruik een virtuele omgeving (venv) om afhankelijkheden te beheren.
Functionaliteit Bepalen

E-mails inlezen en verwerken.
Tekstanalyse uitvoeren (zoals spamfilters en taalmodellen).
Een AI-model trainen of een bestaande API (zoals OpenAI GPT) gebruiken.
De gebruiker een phishing-score geven.
Implementatie

Bouw een EmailParser om e-mails te analyseren.
Maak een FeatureExtractor die verdachte patronen opspoort.
Gebruik een PhishingDetector die AI of een rule-based systeem gebruikt.
Voeg een UserInterface toe (CLI of een simpele webapp).
Testen en Verbeteren

Test met echte phishing- en legitieme e-mails.
Optimaliseer detectiealgoritmes.
Deployen en Gebruikersfeedback

Maak een API of webinterface voor gebruikers.
Verzamel feedback en verbeter het model