"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from AlecViewWeb import app


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/bot')
def bot():
    """Renders the contact page."""
    return render_template('bot.html',title='Bot', year=datetime.now().year,)
     

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
     
    )
