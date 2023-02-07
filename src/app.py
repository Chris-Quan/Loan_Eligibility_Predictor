from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import pickle
import pandas as pd
import joblib

# App definition
app = Flask(__name__)



# importing models
regressor = joblib.load('Regression_pipeline.pickle')

#
@app.route('/predict', methods=['POST','GET'])
def predict():

   if flask.request.method == 'POST':

       data = request.get_json()
       print(data)

       prediction = str(regressor.predict(pd.DataFrame(data, index=[0]))
                        
       return prediction






if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5555)