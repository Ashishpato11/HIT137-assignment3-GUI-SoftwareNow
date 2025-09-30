from abc import ABC, abstractmethod

class BaseModelAdapter(ABC):
    """Base class for all model adapters - demonstrates polymorphism"""
    
    def __init__(self, mid, task): 
        self.__mid = mid  # Private attribute - demonstrates encapsulation
        self.__task = task  # Private attribute - demonstrates encapsulation
        self._pipeline = None  # Protected attribute
        self._model_status = "Not Loaded"
    
    @property
    def model_id(self): 
        """Get model ID - demonstrates encapsulation through property"""
        return self.__mid
    
    @property
    def task_name(self): 
        """Get task name - demonstrates encapsulation through property"""
        return self.__task
    
    @property
    def status(self):
        """Get model status"""
        return self._model_status
    
    def is_loaded(self): 
        """Check if model is loaded"""
        return self._pipeline is not None
    
    @abstractmethod
    def load(self):
        """Abstract method - must be implemented by subclasses (polymorphism)"""
        pass
    
    @abstractmethod
    def predict(self, data):
        """Abstract method - must be implemented by subclasses (polymorphism)"""
        pass
    
    def info(self): 
        """Get model information - can be overridden (method overriding)"""
        return f'Model: {self.model_id}\nTask: {self.task_name}\nStatus: {self.status}'
    
    def preprocess_data(self, data):
        """Default preprocessing - can be overridden in subclasses"""
        return data
    
    def postprocess_result(self, result):
        """Default postprocessing - can be overridden in subclasses"""
        return result
