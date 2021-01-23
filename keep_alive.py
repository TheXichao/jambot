from flask import Flask,render_template,redirect
from threading import Thread

app = Flask('')


#--------------------------------------------
@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template("index.html")
#--------------------------------------------------

@app.route('/test',methods=['GET'])
def poopoo():
  return render_template("pp.html")

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()