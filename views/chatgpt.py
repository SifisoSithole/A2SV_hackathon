from flask import Flask, request, jsonify, session
from views import chatgpt_views
from models.chatgpt import ChatGPT
from models.db import Storage
from auth.auth import login_required

chatGPT = ChatGPT()
storage = Storage()

@chatgpt_views.route('/', strict_slashes=False, methods=['POST'])
@login_required  # Assuming you have a login_required decorator
def chat_bot():
    try:
        # Retrieve the user's session ID
        session_id = request.cookies.get('session_id')
        
        # Get the user's ID from the session
        user_id = session.get(session_id)
        
        # Retrieve the user object from your storage
        user = storage.get_user(user_id=user_id)

        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Removing sensitive information from the user object
        del user['password']
        del user['email']
        del user['_id']


        # Get the user's message from the request JSON
        message = request.json['message']

        # Context description for the chatbot
        context = "Welcome to the Garden Assistant Chatbot! I'm here to assist you with gardening tips and advice based on your user profile. return response formated in html"

    
        response = chatGPT.complete_chat(message, context, user)

        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500
