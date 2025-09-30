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