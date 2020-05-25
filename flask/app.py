from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

#create bot
bot = ChatBot('Alec',storage_adapter='chatterbot.storage.SQLStorageAdapter',           
  database_uri='sqlite:///database.sqlite3'
)
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.custom")

@app.route('/')
def index():
 
    return render_template(
        'index.html',
    )

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":    
    app.run()
