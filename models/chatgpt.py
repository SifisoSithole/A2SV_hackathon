import json
import requests

class ChatGPT:
    def __init__(self, base_url="https://api.openai.com/v1/"):
        self.base_url = base_url
        self.openai_token = environ.get('OPENAI_API')
        self.openai_header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.openai_token}"
        }

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

        return response

