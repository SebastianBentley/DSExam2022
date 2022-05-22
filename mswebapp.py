
# Import libraries
import numpy as np

# from sklearn.externals 
import joblib
import pickle
from flask import Flask, request, jsonify, render_template

# create an instance (our app)
app = Flask(__name__, template_folder='./templates')
# app = Flask(__name__, template_folder='somefolder')

model1 = joblib.load('./deploy/data1_model.pkl')
model2 = joblib.load('./deploy/data2_model.pkl')
model3 = joblib.load('./deploy/data3_model.pkl')

@app.route('/', methods=['GET', 'POST'])

@app.route('/predict')
def predict():
    return render_template('prediction.html')

@app.route('/predicted', methods=['GET', 'POST'])
def predicted():
    if request.method == 'POST':
        x1 = request.form['x1']
        x2 = request.form['x2']
        X = [[x1, x2]]
        predicted = model2.predict(X)
          
        return render_template("predicted.html", content=X, prediction=predicted)
    
@app.route('/bye')
def bye():
    return render_template('bye.html')

if __name__ == '__main__':
    app.run(debug=True)
