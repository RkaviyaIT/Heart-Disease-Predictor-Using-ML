from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open('heart_disease_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        features = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak']),
            float(request.form['slope']),
            float(request.form['ca']),
            float(request.form['thal'])
        ]
        
        prediction = model.predict([features])
        
        prediction_text = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease Detected"
        
        return render_template('result.html', prediction_text=prediction_text)
    else:
        return render_template('predict.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
