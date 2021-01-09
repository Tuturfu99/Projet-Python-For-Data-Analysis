# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:48:41 2020

@author: Arthur Brasseur
"""

from flask import Flask, request, redirect, url_for, flash, jsonify,render_template
import numpy as np
import pickle as p
import json

app = Flask(__name__)
model = p.load(open('projetAPI.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]

    return render_template('index.html', prediction_text='Number of shares should be {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)

    


