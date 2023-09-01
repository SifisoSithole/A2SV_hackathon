from flask import Flask, request, jsonify, session, redirect, url_for, make_response
from auth.auth import AuthManager
import uuid
from views import auth_views

auth_manager = AuthManager()

@auth_views.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        if auth_manager.create_user(email, password):
            return redirect(url_for('root'))
        else:
            return jsonify({'error': 'Username already exists'}), 400

@auth_views.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return jsonify({'error': 'Username or password are required'}), 400

        user = auth_manager.get_user(email)
        if user and auth_manager.check_password(email, password):
            # Create a session ID (you can use a UUID, for example)
            session_id = str(uuid.uuid4())

            # Store the session ID in the session dictionary with the user ID
            session[session_id] = user['_id']

            # Create a response and set a cookie with the session ID
            response = make_response(jsonify({'message': 'Login successful'}), 200)
            response.set_cookie('session_id', session_id)

            return response
        else:
            return jsonify({'error': 'Username and password are incorrect'}), 400

@auth_views.route('/logout', methods=['POST'])
def logout():
    session_id = request.cookies.get('session_id')
    session.pop(session_id, None)
    return jsonify({'message': 'Logout successful'}), 200

