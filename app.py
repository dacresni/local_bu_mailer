from flask import Flask
from flask import render_template 
from flask import g
import sqlite3

app = Flask(__name__)

def home():
    return "<p>upload here</p> <input type='file' accept='csv'/>"

DATABASE = 'LOCAL_MAILER.DB'

def get_db():
    db = getattr(g, '_database',None)
    if db is None:
        db = g,_database = sqlite3.connect(DATABASE)
        return db
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload" method=['POST'])
def upload():
    file = request.files['file']
    db = get_db().cursor()
    
