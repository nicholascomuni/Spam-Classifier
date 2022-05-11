import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource
import pickle as pkl

with open("teste.pkl",'rb') as file:
    transformer,classifier = pkl.load(file)

def predict_message(message):
    return classifier.predict(transformer.transform([message]))

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello !!"

@app.route('/predict',methods=['POST'])
def predict():
    """
    Fazer uma função que vai pegar o request.json separado por mensagens
    """
    predicted = predict_message(request.data)[0]
    """
    Retorna um json separado por mensagens
    """
    return predicted

if __name__ == "__main__":
    app.run(debug=True)


print(__name__)
