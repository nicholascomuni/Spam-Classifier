import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource, reqparse
import pickle as pkl

with open("predictor.pkl",'rb') as file:
    transformer,classifier = pkl.load(file)

def PredictSpamHam(content):
    return classifier.predict(transformer.transform(content))

PredParser = reqparse.RequestParser()
PredParser.add_argument('content',type=str,required=True)

app = Flask(__name__)
api = Api(app)

class PredictSpam(Resource):
    def post(self):
        args = PredParser.parse_args()
        prediction = PredictSpamHam([args['content']])
        return {'prediction': prediction[0]}

api.add_resource(PredictSpam,"/predict")


if __name__ == "__main__":
    app.run(debug=True)
