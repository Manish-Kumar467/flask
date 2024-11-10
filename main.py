from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

# Load the SVC model
model = joblib.load('svc.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Expecting JSON data
    symptoms_str = data.get('symptoms')  # Symptoms as comma-separated string
    
    # Convert comma-separated symptoms string to a list
    symptoms_list = symptoms_str.split(',')
    
    # Ensure the list is in a format the model expects
    input_data = np.array(symptoms_list).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(input_data)
    predicted_disease = prediction[0]
    
    # Return the prediction as JSON
    return jsonify({'disease': predicted_disease})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
