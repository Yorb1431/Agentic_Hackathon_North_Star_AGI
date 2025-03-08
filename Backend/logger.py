class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')
    
    def read(self):
        with open(self.log_file, 'r') as f:
            return f.read()
        
    def clear(self):
        with open(self.log_file, 'w') as f:
            f.write('')
    
    def get_log_file(self):
        return self.log_file
    
    def __str__(self):
        return f"Logger({self.log_file})"
        
    
    
    

    