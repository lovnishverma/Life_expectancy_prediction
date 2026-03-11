from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load saved model
model = joblib.load('model.joblib')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def index():
    pred = None
    
    if request.method == 'POST':
        # Extract features from the submitted form and convert types
        try:
            features = [
                float(request.form['adult_mortality']),
                float(request.form['infant_deaths']),
                float(request.form['alcohol']),
                float(request.form['percentage_expenditure']),
                float(request.form['hepatitis_b']),
                float(request.form['measles']),
                float(request.form['bmi']),
                float(request.form['under_five_deaths']),
                float(request.form['polio']),
                float(request.form['total_expenditure']),
                float(request.form['diphtheria']),
                float(request.form['hiv_aids']),
                float(request.form['gdp']),
                float(request.form['population']),
                float(request.form['thinness_1_19']),
                float(request.form['thinness_5_9']),
                float(request.form['income_composition']),
                float(request.form['schooling']),
                True if request.form['status_developing'] == 'True' else False
            ]
            
            # Predict using the model
            # Reshaping is handled by placing features in a nested list
            prediction_array = model.predict([features])
            pred = prediction_array[0]
            
        except Exception as e:
            pred = f"Error processing input: {e}"

    return render_template('predict.html', pred=pred)

if __name__ == '__main__':
    app.run(debug=True)
