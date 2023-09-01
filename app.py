from flask import Flask, request, jsonify, redirect, url_for, session, render_template
from functools import wraps
from flask_cors import CORS
from views import auth_views

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.register_blueprint(auth_views, url_prefix='/auth')
cors = CORS(app, resources={r"/*": {"origins": "*"}})

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session_id = request.cookies.get('session_id')
        if session_id not in session:
            return redirect(url_for('root'))
        return func(*args, **kwargs)
    return wrapper

@app.route('/', strict_slashes=False)
def root():
    # Render the login page HTML template
    return render_template('login.html')

@app.route('/signup', strict_slashes=False)
def return_signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
