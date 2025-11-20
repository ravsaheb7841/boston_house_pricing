
````
# Boston House Price Prediction Web App

This is a **Flask-based web application** that predicts the price of a house in Boston using machine learning.  
The app uses the **Boston Housing Dataset** and provides predictions in **Lakh (₹)** with proper Indian formatting.

---

## 🛠 Features

- Predict house prices using 13 key features:
  - CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT
- Interactive web interface built with **HTML & Bootstrap**
- **Dark mode toggle** for user convenience
- Loading spinner while predictions are processed
- Graphs:
  - Predicted vs Actual house prices
  - Model performance metrics (MAE, MSE, RMSE, R²)
- Dataset preview included

---

## 📦 Tech Stack

- Python 3.x
- Flask
- Pandas, NumPy
- Scikit-learn (Machine Learning)
- Matplotlib (Graphs)
- Pickle (Model Saving / Loading)
- Bootstrap 5 (Frontend UI)

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_folder>
````

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
python app.py
```

5. Open your browser at:

```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
project_folder/
│
├── app.py                 # Main Flask app
├── requirements.txt       # Python dependencies
├── models/
│   ├── regmodel.pkl       # Trained ML model
│   └── scaling.pkl        # Feature scaler
├── dataset/
│   └── boston.csv         # Dataset
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── dataset.html
│   ├── graphs.html
│   └── about.html
└── static/
    └── pred_vs_actual.png # Generated graph
```

---

## 📊 Model Performance

* **MAE:** X.XXX
* **MSE:** X.XXX
* **RMSE:** X.XXX
* **R² Score:** X.XXX

*(Values depend on your trained model)*

---

## 👨‍💻 Author

* Developed by **Ravsaheb**
* GitHub: [Your GitHub Link]
* LinkedIn: [Your LinkedIn Link]

---

## 📄 License

This project is open-source and free to use for learning and personal purposes.

```
```
