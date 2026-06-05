from flask import Flask
# from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/')
def home():
    """Simple placeholder greeting"""
    return "Welcome to the Flask app!"  