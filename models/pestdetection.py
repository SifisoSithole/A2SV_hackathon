import torch
from transformers import AutoImageProcessor, ResNetForImageClassification
from PIL import Image

class PestDetector:
    def __init__(self, model_name="microsoft/resnet-50"):
        self.processor = AutoImageProcessor.from_pretrained(model_name)
        self.model = ResNetForImageClassification.from_pretrained(model_name)


    def detect_pest(self, image):
        inputs = self.processor(image, return_tensors="pt")
        
        with torch.no_grad():
            logits = self.model(**inputs).logits

        predicted_label = logits.argmax(-1).item()
        return self.model.config.id2label[predicted_label]

