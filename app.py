import pickle
from flask import Flask, request, render_template, jsonify
import numpy as np

app = Flask(__name__)

# Load model & scaler
model = pickle.load(open('regmodel.pkl', 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form inputs
        data = [float(x) for x in request.form.values()]
        final_input = scaler.transform(np.array(data).reshape(1, -1))

        # Model prediction
        output = model.predict(final_input)[0]
        rounded_output = round(output, 2)

        # Convert lakh → rupees (manual formatting)
        rupees = int(rounded_output * 100000)
        formatted_rupees = f"{rupees:,}"

        prediction_text = f"{rounded_output} lakh  (₹ {formatted_rupees})"

        return render_template('home.html', prediction_text=prediction_text)

    except Exception as e:
        return render_template('home.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
