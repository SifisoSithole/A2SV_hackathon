import json
import requests
from os import environ

class ChatGPT:
    def __init__(self, base_url="https://api.openai.com/v1/"):
        self.base_url = base_url
        self.openai_token = environ.get('OPENAI_API')
        self.openai_header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.openai_token}"
        }

    def format_text_as_html(self, text_response):
        lines = text_response.split('\n')
        formatted_html = []

        for line in lines:
            if line.startswith('- '):
                formatted_html.append(f'<ul><li>{line[2:]}</li></ul>')
            elif line.startswith('1. '):
                formatted_html.append(f'<ol><li>{line[2:]}</li></ol>')
            elif line.startswith('# '):
                level = line.count('#')
                formatted_html.append(f'<h{level}>{line.strip("# ")}</h{level}>')
            else:
                formatted_html.append(f'<p>{line}</p>')

        return ''.join(formatted_html)

    def complete_chat(self, user_message, context=None, user_profile=None):
        messages = []

        if context:
            messages.append({"role": "system", "content": context})

        if user_profile:
            messages.append({"role": "user", "content": json.dumps(user_profile)})

        messages.append({"role": "user", "content": user_message})

        data = {
            "model": "gpt-3.5-turbo",
            "messages": messages
        }

        response = requests.post(self.base_url + "/chat/completions", headers=self.openai_header, json=data)
        response = json.loads(response.text)

        # Extract the model's response
        model_response = response['choices'][0]['message']['content']

        # Format the model's response as HTML
        formatted_response = self.format_text_as_html(model_response)
        print(formatted_response)

        return formatted_response

