import pickle
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

app = Flask(__name__)

# Load model & scaler safely
model = pickle.load(open('models/regmodel.pkl', 'rb'))
scaler = pickle.load(open('models/scaling.pkl', 'rb'))

# Load dataset
df = pd.read_csv("dataset/boston.csv")


# HOME PAGE
@app.route('/')
def home():
    return render_template('home.html')


# DATASET PAGE
@app.route('/dataset')
def dataset():
    head_html = df.head().to_html(classes='table table-bordered table-striped')
    shape = df.shape
    return render_template("dataset.html", table=head_html, shape=shape)


# PREDICTION PAGE
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = []

        for value in request.form.values():
            if value == "":
                return render_template("home.html",
                                       prediction_text="Invalid Input! Values cannot be empty.")

            if float(value) < 0:
                return render_template("home.html",
                                       prediction_text="Invalid Input! Values cannot be negative.")

            data.append(float(value))

        final_input = scaler.transform(np.array(data).reshape(1, -1))
        output = model.predict(final_input)[0]

        rounded_output = round(output, 2)
        rupees = int(rounded_output * 100000)
        formatted_rupees = f"{rupees:,}"

        prediction_text = f"{rounded_output} lakh (₹ {formatted_rupees})"

        return render_template('home.html', prediction_text=prediction_text)

    except Exception as e:
        print("Prediction Error:", e)
        return render_template('home.html',
                               prediction_text="Error occurred during prediction!")


# GRAPH PAGE
@app.route('/graphs')
def graphs():

    target_col = "MEDV"

    if target_col not in df.columns:
        return "ERROR: MEDV column not found!"

    y_true = df[target_col][:200]
    X_sample = df.drop(target_col, axis=1)[:200]

    scaled = scaler.transform(X_sample)
    y_pred = model.predict(scaled)

    # GRAPH
    graph_path = "static/pred_vs_actual.png"

    plt.figure()
    plt.scatter(y_true, y_pred)
    plt.xlabel("Actual Price (MEDV)")
    plt.ylabel("Predicted Price")
    plt.title("Predicted vs Actual")
    plt.savefig(graph_path)
    plt.close()

    # METRICS
    mae = round(mean_absolute_error(y_true, y_pred), 3)
    mse = round(mean_squared_error(y_true, y_pred), 3)
    rmse = round(np.sqrt(mse), 3)
    r2 = round(r2_score(y_true, y_pred), 3)

    metrics = {"MAE": mae, "MSE": mse, "RMSE": rmse, "R2 Score": r2}

    return render_template("graphs.html", metrics=metrics, graph_path=graph_path)


# ABOUT PAGE
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
