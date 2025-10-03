# HIT137-assignment3-GUI-SoftwareNow
Group submission for S225 HIT137 Software Now - Assignment 3

A clean, functional GUI application demonstrating Object-Oriented Programming concepts with real Hugging Face AI models.A clean, functional GUI application demonstrating Object-Oriented Programming concepts with real Hugging Face AI models.
## Features## Features



- **Text Sentiment Analysis**: Real-time sentiment analysis using DistilBERT- **Text Sentiment Analysis**: Real-time sentiment analysis using DistilBERT

- **Image Classification**: Image recognition using Vision Transformer (ViT)- **Image Classification**: Image recognition using Vision Transformer (ViT)

- **Text-to-Image Generation**: AI image generation using Stable Diffusion- **Text-to-Image Generation**: AI image generation using Stable Diffusion

- **Clean OOP Design**: Multiple inheritance, decorators, polymorphism, encapsulation- **Clean OOP Design**: Multiple inheritance, decorators, polymorphism, encapsulation

- **Simple Interface**: User-friendly Tkinter GUI- **Simple Interface**: User-friendly Tkinter GUI

## Quick Start## Quick Start



1. **Install Dependencies**:1. **Install Dependencies**:

   ```bash   ```bash

   pip install torch transformers diffusers pillow   pip install torch transformers diffusers pillow

   ```   ```



2. **Run the Application**:2. **Run the Application**:

   ```bash   ```bash

   python main.py   python main.py

   ```   ```



## Usage## Usage



### Text Sentiment Analysis### Text Sentiment Analysis

- Select "Text Sentiment Analysis"- Select "Text Sentiment Analysis"

- Enter text and click "Run Model"- Enter text and click "Run Model"

- Get positive/negative sentiment with confidence score- Get positive/negative sentiment with confidence score



### Image Classification  ### Image Classification  

- Select "Image Classification"- Select "Image Classification"

- Browse and select an image file- Browse and select an image file

- Get object classification results- Get object classification results



### Text-to-Image Generation### Text-to-Image Generation

- Select "Text-to-Image Generation"- Select "Text-to-Image Generation"

- Enter image description (e.g., "astronaut in jungle")- Enter image description (e.g., "astronaut in jungle")

- Generated image saves to `generated_images/` folder- Generated image saves to `generated_images/` folder



## Technical Implementation## Technical Implementation



### Models Used### Models Used

- **Sentiment**: `distilbert-base-uncased-finetuned-sst-2-english`- **Sentiment**: `distilbert-base-uncased-finetuned-sst-2-english`

- **Image Classification**: `google/vit-base-patch16-224`- **Image Classification**: `google/vit-base-patch16-224`

- **Text-to-Image**: `runwayml/stable-diffusion-v1-5`- **Text-to-Image**: `runwayml/stable-diffusion-v1-5`



### OOP Concepts### OOP Concepts

- **Multiple Inheritance**: Controllers inherit from mixins- **Multiple Inheritance**: Controllers inherit from mixins

- **Decorators**: Logging, timing, error handling, validation- **Decorators**: Logging, timing, error handling, validation

- **Polymorphism**: Unified model interface- **Polymorphism**: Unified model interface

- **Encapsulation**: Private methods and data protection- **Encapsulation**: Private methods and data protection



### File Structure## File Structure

```

app/```

├── main.py                 # Application entry pointapp/

├── controllers/├── main.py              # Application entry point

│   └── app_controller.py   # Main controller with multiple inheritance├── controllers/

├── models/│   └── app_controller.py    # Main controller (multiple inheritance)

│   ├── base.py            # Base model adapter├── gui/

│   ├── text_sentiment.py  # Sentiment analysis model│   └── app_view.py         # Tkinter GUI implementation

│   ├── image_classifier.py # Image classification model├── models/

│   └── text_to_image_fast.py # Text-to-image model│   ├── base.py            # Abstract base class

├── gui/│   ├── text_sentiment.py  # Sentiment analysis model

│   └── app_view.py        # Tkinter GUI interface│   ├── image_classifier.py # Image classification model

└── utils/│   └── text_to_image.py   # Text-to-image model

    ├── decorators.py      # Custom decorators├── utils/

    └── mixins.py          # Mixin classes│   ├── mixins.py          # Reusable mixins for multiple inheritance

```│   └── decorators.py      # Multiple decorators

└── requirements.txt       # Dependencies

## Requirements```



- Python 3.8+## AI Models Used

- torch

- transformers1. **DistilBERT** (`distilbert-base-uncased-finetuned-sst-2-english`)

- diffusers   - Text sentiment analysis

- pillow   - Free Hugging Face model

- tkinter (included with Python)

2. **Vision Transformer** (`google/vit-base-patch16-224`)

## Assignment Compliance   - Image classification

   - Free Hugging Face model

This application demonstrates all required OOP concepts:

- ✅ Multiple inheritance (4+ classes)3. **Stable Diffusion** (`CompVis/stable-diffusion-v1-4`)

- ✅ Decorators (4 types: logging, timing, error handling, validation)   - Text-to-image generation (demonstration mode)

- ✅ Polymorphism (unified model interface)   - Free Hugging Face model

- ✅ Encapsulation (private methods, data protection)

- ✅ Method overriding (specialized implementations)## Technical Details



Built for HIT137 Advanced Programming assignment requirements.- **GUI Framework**: Tkinter (Python standard library)
- **AI Framework**: Hugging Face Transformers
- **Deep Learning**: PyTorch backend
- **Image Processing**: Pillow (PIL)
- **Design Pattern**: Model-View-Controller (MVC)

## Educational Value

This application serves as a comprehensive example of:
- Advanced OOP concepts in practice
- AI model integration
- GUI development with Python
- Software architecture principles
- Clean code organization

## Troubleshooting

### Common Issues:

1. **Import Errors**: Install all dependencies from requirements.txt
2. **Model Loading**: First run may take time to download models
3. **Memory Issues**: Models require sufficient RAM (4GB+ recommended)
4. **File Permissions**: Ensure write permissions for model cache

### Performance Tips:

- First model load takes longer (downloads from Hugging Face)
- Subsequent runs are faster (models cached locally)
- GPU acceleration available if CUDA is installed
- Close other applications if memory is limited

## License

This project is for educational purposes. Model licenses follow Hugging Face terms.

## Credits

- **Models**: Hugging Face Model Hub
- **Framework**: Python, Tkinter, PyTorch, Transformers
- **Design**: Object-Oriented Programming principles
