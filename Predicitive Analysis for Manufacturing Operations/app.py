from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values safely
        temperature = float(request.form.get('temperature', 0))
        run_time = float(request.form.get('runtime', 0))
        machine_id = int(request.form.get('machine_id', 0))

        # Make prediction
        prediction = model.predict([[temperature, run_time, machine_id]])[0]
        predicted_downtime = "Yes" if prediction == 1 else "No"

        return render_template('index.html', prediction=predicted_downtime)

    except ValueError:
        return "Invalid input! Please enter valid numbers.", 400
if __name__ == '__main__':
    app.run(debug=True)