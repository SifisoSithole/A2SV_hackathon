from flask import Flask, request, jsonify, redirect, url_for, session, render_template
from flask_cors import CORS
from views import auth_views
from views import chatgpt_views

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.register_blueprint(auth_views, url_prefix='/auth')
app.register_blueprint(chatgpt_views, url_prefix='/chat')
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', strict_slashes=False)
def root():
    return render_template('index.html')

@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')

@app.route('/login', strict_slashes=False)
def login_page():
    return render_template('login.html')

@app.route('/signup', strict_slashes=False)
def return_signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
