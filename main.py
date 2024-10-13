from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the trained model
with open('svc.pkl', 'rb') as f:
    model = pickle.load(f)

# Create and fit a new LabelEncoder
# Replace this with the actual labels you used during training
# Ensure that these labels match those in your training dataset
known_labels = ['Disease1', 'Disease2', 'Disease3']  # Example labels
le = LabelEncoder()
le.fit(known_labels)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        symptoms = data.get('symptoms')

        if not symptoms:
            return jsonify({'error': 'No symptoms provided'}), 400

        # Preprocess the input data
        # Assuming symptoms are binary features matching the training data
        input_data = pd.DataFrame([symptoms])

        # Add noise if necessary (as in your training script)
        noise_level = 0.15
        noise = np.random.normal(1, noise_level, input_data.shape)
        input_noisy = input_data * noise

        # Make prediction
        prediction_encoded = model.predict(input_noisy)
        prediction = le.inverse_transform(prediction_encoded)

        return jsonify({'predicted_disease': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
