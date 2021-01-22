from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "<a href='https://discord.com/api/oauth2/authorize?client_id=802228905380675625&permissions=0&scope=bot'>add jambob</a>"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()