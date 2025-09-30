from PIL import Image
from transformers import pipeline
from models.base import BaseModelAdapter
from utils.mixins import LoggingMixin, ValidatorMixin, ConfigurableMixin
from utils.decorators import log_action, timing_decorator, error_handler, validate_input
class ImageClassifierAdapter(BaseModelAdapter, LoggingMixin, ValidatorMixin, ConfigurableMixin):
    """Image classification model - demonstrates multiple inheritance"""
    
    def __init__(self, mid='google/vit-base-patch16-224'): 
        # Initialize all parent classes properly
        BaseModelAdapter.__init__(self, mid, 'image-classification')
        LoggingMixin.__init__(self)
        ValidatorMixin.__init__(self)
        ConfigurableMixin.__init__(self)
        self._logger("ImageClassifierAdapter initialized")
    
    @log_action()
    @timing_decorator
    @error_handler
    def load(self):
        """Load the image classification model - demonstrates method overriding"""
        if not self.is_loaded(): 
            self._model_status = "Loading..."
            self._pipeline = pipeline('image-classification', model=self.model_id)
            self._model_status = "Loaded"
            self._logger(f"Model {self.model_id} loaded successfully")
    
    @log_action()
    @timing_decorator
    @error_handler
    @validate_input(input_type='file')
    def predict(self, data):
        """Predict image class - demonstrates polymorphism and decorators"""
        if not self.is_loaded(): 
            self.load()
        
        # Preprocess data (method overriding)
        processed_data = self.preprocess_data(data)
        
        # Make prediction
        result = self._pipeline(processed_data)
        
        # Postprocess result (method overriding)
        return self.postprocess_result(result[0])
    
    def preprocess_data(self, data):
        """Override base preprocessing for image data"""
        validated_path = self.validate_file_path(data)
        img = Image.open(validated_path) if not isinstance(data, Image.Image) else data
        return img
    
    def postprocess_result(self, result):
        """Override base postprocessing for classification results"""
        return {
            'label': result['label'],
            'confidence': round(result['score'], 4),
            'model': self.model_id,
            'task': self.task_name
        }
    
    def info(self):
        """Override base info method - demonstrates method overriding"""
        base_info = super().info()
        return f"{base_info}\nSpecialization: Image Classification\nSupported: Common image formats (JPG, PNG, etc.)"
