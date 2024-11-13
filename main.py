from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
import pickle
from flask_cors import CORS
# import os
# import requests


app = Flask(__name__)
CORS(app)

# Load the SVC model
model = joblib.load('./models/svc.pkl')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  # Access the Node.js service URL from the environment variable
  # nodejs_service_url = os.getenv("NODEJS_SERVICE_URL", "http://localhost:3000")  # Fallback to localhost for local testing
  try:
        data = request.json  # JSON input
        symptoms_list = data.get('symptoms', [])
        
        if not symptoms_list:
            return jsonify({'error': 'No symptoms provided'}), 400
        
        # Ensure input shape compatibility
        input_data = np.array([symptoms_dict.get(symptom, 0) for symptom in symptoms_list]).reshape(1, -1)
        
        # Predict
        prediction = model.predict(input_data)
        predicted_disease = diseases_list[prediction[0]]
        
        return jsonify({'disease': predicted_disease})
  except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000)

# from flask import Flask, request, jsonify
# import joblib
# import numpy as np
# import pandas as pd #
# import pickle #
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Allow CORS for all routes

# # Load the SVC model
# model = joblib.load('./models/svc.pkl')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.json  # JSON input
#         symptoms_list = data.get('symptoms', [])
        
#         if not symptoms_list:
#             return jsonify({'error': 'No symptoms provided'}), 400
        
#         # Ensure input shape compatibility
#         input_data = np.array([symptoms_dict.get(symptom, 0) for symptom in symptoms_list]).reshape(1, -1)
        
#         # Predict
#         prediction = model.predict(input_data)
#         predicted_disease = diseases_list[prediction[0]]
        
#         return jsonify({'disease': predicted_disease})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(port=8080, debug=True)

