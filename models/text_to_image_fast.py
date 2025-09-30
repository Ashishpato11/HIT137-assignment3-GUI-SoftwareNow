#!/usr/bin/env python3
"""
Simple AI text-to-image model .
"""

from diffusers import DiffusionPipeline
from PIL import Image
import os
from datetime import datetime

class TextToImageModelFast:
    """Simple AI text-to-image generator"""
    
    def __init__(self):
        self.pipe = None
        
    def load(self):
        """Load the model"""
        if self.pipe is None:
            self.pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    
    def predict(self, prompt):
        """Generate image from prompt - input comes from GUI"""
        if self.pipe is None:
            self.load()
        
        # Simple generation like your example
        image = self.pipe(prompt).images[0]
        
        # Save image
        return self._save_image(image, prompt)
    
    def _save_image(self, image, prompt):
        """Save generated image"""
        # Create output directory
        output_dir = "generated_images"
        os.makedirs(output_dir, exist_ok=True)
        
        # Create filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_prompt = safe_prompt.replace(' ', '_') or "image"
        filename = f"AI_Generated_{timestamp}_{safe_prompt}.png"
        filepath = os.path.join(output_dir, filename)
        
        # Save image
        image.save(filepath, "PNG")
        full_path = os.path.abspath(filepath)
        
        return {
            'status': 'success',
            'image_path': full_path,
            'prompt': prompt,
            'message': f'Image saved to: {full_path}'
        }
    
    def is_loaded(self):
        """Check if model is loaded"""
        return self.pipe is not None

# Keep compatibility
TextToImageAdapterFast = TextToImageModelFast