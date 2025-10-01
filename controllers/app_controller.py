import threading
import os
from utils.mixins import LoggingMixin, ConfigurableMixin
from utils.decorators import log_action, timing_decorator, error_handler
from models.text_sentiment import TextSentimentAdapter
from models.image_classifier import ImageClassifierAdapter
from models.text_to_image_fast import TextToImageAdapterFast as TextToImageAdapter

class AppController(LoggingMixin, ConfigurableMixin):
    """Main application controller - demonstrates multiple inheritance"""

    def __init__(self, view):
        # Initialize all parent classes properly
        LoggingMixin.__init__(self)
        ConfigurableMixin.__init__(self)
        self.view = view
        self.val = None

        # Initialize models - demonstrates polymorphism
        self.text_sentiment_m = TextSentimentAdapter()
        self.img_classifier_m = ImageClassifierAdapter()
        self.text_to_image_m = TextToImageAdapter()
        
        self.models = {
            'Text Sentiment Analysis': self.text_sentiment_m, 
            'Image Classification': self.img_classifier_m,
            'Text-to-Image Generation': self.text_to_image_m
        }

        # Populate the GUI with available models
        self.view.populate_models(list(self.models.keys()))
        self.view.on_run_clicked(self.run_async)
        
        self._logger("Controller initialized with Text Sentiment, Image Classification, and Text-to-Image models")

        def set_text_input(self, t):
        self.val = t

        @log_action()
        @timing_decorator
        @error_handler
        def run(self, model_name):
            """Run the selected model - demonstrates polymorphism through different model types"""
            self._logger(f"Running model: {model_name}")

        # Get the appropriate model - demonstrates polymorphism
        model = self.models.get(model_name)
        if not model:
            self.view.render_output(f"Error: Model '{model_name}' not found")
            return
        
         # Load the model
        self._logger(f"Loading model: {model_name}")
        model.load()
        
         # Get input based on model type and user selection
        input_data = self._get_input_data(model_name)
        if not input_data:
            return
        
        # Make prediction - all models implement predict() differently (polymorphism)
        self._logger(f"Making prediction with input data")
        result = model.predict(input_data)
        
        # Format and display result
        formatted_result = self.format_result(result, model_name)
        self.view.render_output(formatted_result)
        self._logger("Prediction completed successfully")
         def _get_input_data(self, model_name):
        """Get appropriate input data based on model type and user selection"""
        input_type = self.view.get_input_type()
        
        if model_name == "Text-to-Image Generation" or input_type == "Text":
         # Use text input
            input_data = self.val if self.val else self.view.get_text_input()
            if not input_data or not input_data.strip():
                self.view.render_output("Error: Please enter some text")
                return None
            return input_data
        
        elif input_type == "Image":
