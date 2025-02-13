from app import app
from flask import render_template

@app.route('/')
def index():
    title = "4blind-test"
    return render_template('index.html', title=title)