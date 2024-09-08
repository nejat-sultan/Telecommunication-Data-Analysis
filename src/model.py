import joblib # type: ignore
from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)
model = joblib.load('model.pkl')  

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [data['features']]
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
