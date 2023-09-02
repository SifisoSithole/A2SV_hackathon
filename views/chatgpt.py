from flask import Flask, request, jsonify, session
from views import chatgpt_views
from models.chatgpt import ChatGPT
from models.db import Storage
from auth.auth import login_required

chatGPT = ChatGPT()
storage = Storage()

@login_required
@chatgpt_views.route('/', strict_slashes=False)
def chat_bot():
    session_id = request.cookies.get('session_id')
    user_id = session[session_id]
    user = storage.get_user(user_id=user_id)
    del user['password']
    del user['email']
    response = chatGPT.complete_chat("Hi")
    return jsonify(response)
