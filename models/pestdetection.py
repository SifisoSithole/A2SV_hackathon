import torch
from transformers import ResNetForImageClassification, PreTrainedTokenizerFast
from PIL import Image

class PestDetector:
    def __init__(self, model_name="microsoft/resnet-50"):
        self.model = ResNetForImageClassification.from_pretrained(model_name)
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained(model_name)

    def detect_pest(self, image_path):
        image = Image.open(image_path)
        inputs = self.tokenizer(images=image, return_tensors="pt")
        
        outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()

        return predicted_class

