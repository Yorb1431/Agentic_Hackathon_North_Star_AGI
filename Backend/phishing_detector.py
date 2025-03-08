def class PhishingDetector:
    def __init__(self, model_path: str):
        self.model = load_model(model_path)
    
    def predict(self, url: str) -> float:
        # Preprocess the URL
        # ...
        # ...
        # ...
        return self.model.predict(url)
    
    def __str__(self):
        return f"PhishingDetector({self.model})"
    
```