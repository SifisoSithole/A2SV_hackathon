from flask import Flask, request, jsonify, session
from views import pest_detection_views
from models.chatgpt import ChatGPT
from models.db import Storage
from PIL import Image
from models.pestdetection import PestDetector
from auth.auth import login_required

chatGPT = ChatGPT()
storage = Storage()
pestdetection = PestDetector()

@login_required
@pest_detection_views.route('/', strict_slashes=False, methods=['POST'])
def pest_detection():
    session_id = request.cookies.get('session_id')
    file = request.files.get('image')

    if file:
        try:
            # Convert the uploaded file to a PIL Image
            image = Image.open(file.stream)
            detected_pest = pestdetection.detect_pest(image)
        except Exception as e:
            return jsonify({'error': f'Error processing image: {str(e)}'})

    user_id = session.get(session_id)
    user = storage.get_user(user_id=user_id)

    # Removing sensitive information from the user object
    del user['password']
    del user['email']

    # Context description for the chatbot
    context = "Welcome to the Pest Detection Assistant! I'm here to help you identify and manage pests in your agricultural crops. Please provide details about the pest or upload an image for analysis."

    # Use the detected pest information as part of the chat context
    if detected_pest:
        context += f" Detected pest: {detected_pest}"

    # Send the message and context to the chatbot for a response
    message = "Provide advice if the image provided is a pest and if it's dangerous"
    response = chatGPT.complete_chat(message, context=context)

    return jsonify({'response': response})
