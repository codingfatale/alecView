from chatterbot import ChatBot
from chatterbot.logic import logic_adapter
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Alec',storage_adapter='chatterbot.storage.SQLStorageAdapter',           
  database_uri='sqlite:///database.sqlite3'
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.custom')

while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
