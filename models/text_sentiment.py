from transformers import pipeline
from models.base import BaseModelAdapter
from utils.mixins import LoggingMixin, ValidatorMixin, ConfigurableMixin
from utils.decorators import log_action, timing_decorator, error_handler, validate_input
class TextSentimentAdapter(BaseModelAdapter, LoggingMixin, ValidatorMixin, ConfigurableMixin):
    """Text sentiment analysis model - demonstrates multiple inheritance"""
    
    def __init__(self, mid='distilbert-base-uncased-finetuned-sst-2-english'): 
        # Initialize all parent classes properly
        BaseModelAdapter.__init__(self, mid, 'sentiment-analysis')
        LoggingMixin.__init__(self)
        ValidatorMixin.__init__(self)
        ConfigurableMixin.__init__(self)
        self._logger("TextSentimentAdapter initialized")
    
    @log_action()
    @timing_decorator
    @error_handler
    def load(self):
        """Load the sentiment analysis model - demonstrates method overriding"""
        if not self.is_loaded(): 
            self._model_status = "Loading..."
            self._pipeline = pipeline('sentiment-analysis', model=self.model_id)
            self._model_status = "Loaded"
            self._logger(f"Model {self.model_id} loaded successfully")
    
    @log_action()
    @timing_decorator
    @error_handler
    @validate_input(input_type='text')
    def predict(self, data):
        """Predict sentiment - demonstrates polymorphism and decorators"""
        if not self.is_loaded(): 
            self.load()
        
        # Preprocess data (method overriding)
        processed_data = self.preprocess_data(data)
        
        # Make prediction
        result = self._pipeline(str(processed_data))
        
        # Postprocess result (method overriding)
        return self.postprocess_result(result[0])
    
    def preprocess_data(self, data):
        """Override base preprocessing for text data"""
        validated_data = self.validate_text_input(data)
        return validated_data
    
    def postprocess_result(self, result):
        """Override base postprocessing for sentiment results"""
        return {
            'label': result['label'],
            'confidence': round(result['score'], 4),
            'model': self.model_id,
            'task': self.task_name
        }
    
    def info(self):
        """Override base info method - demonstrates method overriding"""
        base_info = super().info()
        return f"{base_info}\nSpecialization: Text Sentiment Analysis\nSupported: English text"
