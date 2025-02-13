from app import app
from flask import render_template

@app.route('/')
def index():
    title = "Portfólio"
    return render_template('index.html', title=title)