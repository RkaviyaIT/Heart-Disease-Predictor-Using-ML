💓 Heart Disease Prediction Web App
This is a Flask-based web application that predicts the likelihood of heart disease based on input medical parameters using a trained Logistic Regression model.

🚀 Features
Predicts heart disease using 13 medical input values

Built with:

Python, Flask, HTML/CSS

Scikit-learn (ML model)

User-friendly interface with multiple pages (Home, About, Predict, Result)

Model training and saving included in project

🗂 Project Structure
php
Copy
Edit
├── static/                   # Static files (CSS, JS, Images)
├── templates/               # HTML Templates
│   ├── index.html
│   ├── about.html
│   ├── kaviya.html
│   ├── predict.html
│   └── result.html
├── app.py                   # Main Flask application
├── heart.csv                # Dataset (UCI Heart Disease dataset)
├── train_and_save_model.py  # Script to train and save model
├── heart_disease_model.pkl  # Saved ML model (Logistic Regression)
└── heart_disease_prediction.py  # Prediction logic (optional use)
⚙️ How to Run the Project
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Example requirements.txt:

nginx
Copy
Edit
flask
numpy
pandas
scikit-learn
3. Run the Flask App
bash
Copy
Edit
python app.py
Go to your browser and open: http://127.0.0.1:5000/

🧠 Model Details
Algorithm: Logistic Regression

Scaler: StandardScaler from Scikit-learn

Training/Test Split: 80/20

Accuracy: Printed in console after training

📊 Input Parameters (13 Features)
age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal

📌 Credits
Dataset: UCI Heart Disease Dataset

Developed by: Your Name

📷 Screenshot
<img width="1344" height="622" alt="image" src="https://github.com/user-attachments/assets/7ad78088-8cd6-4c93-9842-89e440100225" />
