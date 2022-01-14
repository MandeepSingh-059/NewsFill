from flask import Flask, render_template, request
import pickle
import app2
from pycaret.anomaly import *
from sklearn.neighbors import KNeighborsClassifier
from subprocess import call

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def home():
    time = request.form['a']
    place = request.form['b']
    curr_loc = request.form['c']
    amount=int(request.form['d'])
    type=request.form['e']
    merchant=request.form['f']
    any_invalid=request.form['g'] 
    any_recurr_debits=request.form['h']
    
    call(["python", "app2.py"])
    return render_template('after.html',data=app2.func(time,place,curr_loc,amount,type,merchant,any_invalid,any_recurr_debits))


if __name__ == "__main__":
    app.run(debug=True)