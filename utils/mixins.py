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