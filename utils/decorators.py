from functools import wraps
import time

def log_action(logger_attr: str = '_logger'):
    """Decorator to log method entry and exit"""
    def decorator(func):
        @wraps(func)
        def wrapper(self, *a, **k):
            logger = getattr(self, logger_attr, None)
            if logger: logger(f'[ENTER] {self.__class__.__name__}.{func.__name__}')
            result = func(self,*a,**k)
            if logger: logger(f'[EXIT ] {self.__class__.__name__}.{func.__name__}')
            return result
        return wrapper
    return decorator