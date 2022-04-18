import numpy as np
import pandas as pd
from flask import Flask, request, render_template, current_app
# from flask_ngrok import run_with_ngrok

# Modeling libs
import pickle

app = Flask(__name__)
model = pickle.load(open('static/saved_model/model.pkl', 'rb')) # import model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def getprediction():

    input = [float(x) for x in request.form.values()]
    final_input = [np.array(input)]
    prediction = model.predict(final_input)
    if (prediction == 1):
      prediction_value = 'Phising'
    else:
      prediction_value = 'Benign'


    return render_template('results.html', output=prediction_value)

if __name__ == "__main__":
    app.run()
