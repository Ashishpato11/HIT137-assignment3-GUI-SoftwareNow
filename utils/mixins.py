import datetime as dt

class LoggingMixin:
    """Mixin class for logging functionality - demonstrates multiple inheritance"""
    def __init__(self, *a, **k): 
        super().__init__(*a, **k)
        self.__log = []
        
    def _logger(self, msg): 
        e = f"[{dt.datetime.now().strftime('%H:%M:%S')}] {msg}"
        self.__log.append(e)
        print(e)
        
    @property
    def log_history(self): 
        return tuple(self.__log)
    
    def clear_logs(self):
        """Clear the log history"""
        self.__log.clear()
        
class ValidatorMixin:
    """Mixin class for input validation - demonstrates multiple inheritance"""
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
    
    def validate_text_input(self, text):
        """Validate text input"""
        if not text or not text.strip():
            raise ValueError("Text input cannot be empty")
        if len(text.strip()) < 3:
            raise ValueError("Text input too short (minimum 3 characters)")
        return text.strip()
    
    def validate_file_path(self, file_path):
        """Validate file path"""
        import os
        if not file_path:
            raise ValueError("File path cannot be empty")
        if not os.path.exists(file_path):
            raise ValueError(f"File does not exist: {file_path}")
        return file_path