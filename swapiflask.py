from flask import Flask
from flask import request
import data

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/people/')
def person():
    if 'search' in request.args:
        return data.return_person(request.args['search'])
    else:
        return "People"

@app.route('/films/4/')
def film():
    return data.a_new_hope #"hello!!, films 4"

@app.route('/species/3/')
def species():
    return data.wookie #"hello!!, species 3"

@app.route('/starships/')
def starships():
    if 'search' in request.args:
        return data.return_starship(request.args['search'])
    elif 'page' in request.args:
        return data.return_starship_page(request.args['page'])
    else:
        return data.starships




