from flask import Flask, redirect, render_template, request #, session
# from helpers import apology, login_required
# from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/')
def index():
    """Home page."""
    return render_template("index.html")