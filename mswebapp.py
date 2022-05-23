
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
        height = request.form['height']
        weight = request.form['weight']
        age = request.form['age']
        cholesterollvl = request.form['cholesterollvl']
        systolic = request.form['systolic']
        dystolic = request.form['dystolic']
        gender = request.form['gender']
        chestpain = request.form['chestpain']
        exangina = request.form['exangina']
        heartratemax = request.form['heartratemax']
        STDepression = request.form['STDep']
        cholesterol = request.form['cholesterol']
        trestbps = request.form['trestbps']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']
        smoke = request.form['smoke']
        stroke = request.form['stroke']
        physicalHealth = request.form['physicalHealth']
        mentalHealth = request.form['mentalHealth']
        diffWalking = request.form['diffWalking']
        diabetic = request.form['diabetic']
        skinCancer = request.form['skinCancer']
        
        # calculate bmi and obese
        bmi = round((float(weight) / (float(height) * float(height))), 2)
        obese = 0
        if(bmi > 30):
            obese = 1

        
        # collect data from form into three datapoints
        X1 = [[age, gender, chestpain, trestbps, cholesterol, fbs, restecg, heartratemax, exangina, STDepression,
              slope, ca, thal]]
        X2 = [[bmi, smoke, stroke, physicalHealth, mentalHealth, diffWalking, age, diabetic, skinCancer]]
        X3 = [[bmi, age, cholesterollvl, systolic, dystolic, obese]]
        
        # use each model to predict the outcome
        predicted1 = model1.predict(X1)
        predicted2 = model2.predict(X2)
        predicted3 = model3.predict(X3)
        
        predicted1 = "<p style=\"{color:red}\">YES</p>" if predicted1[0] == 1 else "<p style=\"{color:green}\">NO</p>"
        predicted2 = "<p style=\"{color:red}\">YES</p>" if predicted2[0] == 1 else "<p style=\"{color:green}\">NO</p>"
        predicted3 = "<p style=\"{color:red}\">YES</p>" if predicted3[0] == 1 else "<p style=\"{color:green}\">NO</p>"
          
        return render_template("predicted.html", content1=X1, content2=X2, content3=X3,
                               prediction1=predicted1, prediction2=predicted2,
                              prediction3=predicted3)
    
@app.route('/bye')
def bye():
    return render_template('bye.html')

if __name__ == '__main__':
    app.run(debug=True)
