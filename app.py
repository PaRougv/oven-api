from flask import Flask, jsonify
import joblib

app = Flask(__name__)
model, features = joblib.load("oven_time_predictor.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    return jsonify({"start_time": "05:42"})  # We'll improve this later

if __name__ == '__main__':
    app.run(host='0.0.0.0')