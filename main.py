# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#   return render_template('index.html')

# if __name__ == '__main__':
#   app.run(port=5000)
# app.py
from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the trained model
with open('svc.pkl', 'rb') as f:
    model = pickle.load(f)

# Load LabelEncoder (assuming you saved it; if not, you'll need to handle encoding)
# If you didn't save the LabelEncoder, ensure that the encoding process is consistent
# For example, you can save it similarly to the model or handle encoding in another way

# Example: If the label encoder is saved
with open('label_encoder.pkl', 'rb') as f:
    le = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        symptoms = data.get('symptoms')

        if not symptoms:
            return jsonify({'error': 'No symptoms provided'}), 400

        # Preprocess the input data
        # This step depends on how your model expects the input
        # For example, you might need to convert symptoms to a specific format
        # Here, assuming symptoms are binary features matching the training data

        # Example: Convert symptoms list to a DataFrame row
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

