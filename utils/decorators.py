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

def timing_decorator(func):
    """Decorator to measure execution time"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Log timing if logger exists
        if hasattr(self, '_logger'):
            self._logger(f'[TIMING] {self.__class__.__name__}.{func.__name__} took {execution_time:.4f}s')
        else:
            print(f'[TIMING] {self.__class__.__name__}.{func.__name__} took {execution_time:.4f}s')
        
        return result
    return wrapper