from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
api = Api(app)

model = pickle.load(open('Regression_pipeline.pkl', 'rb'))

class LoanRequest(Resource):
    def post(self):
        json_data = request.get_json()
         
        query_ = pd.DataFrame(json_data, index=[0])
        
        #try:
        prediction = model.predict(query_)
        #except Exception as e:
            #prediction= e
   
        
        if prediction == 'Y':
            return 'loan approved'
        elif prediction == 'N':
            return 'loan not approved'
        else:
            return 'error'
        
api.add_resource(LoanRequest, '/LoanRequest')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)