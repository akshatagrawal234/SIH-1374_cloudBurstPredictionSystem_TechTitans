from flask import Flask
from flask import Flask, request, jsonify, render_template

# app.py
from flask import Flask, request, jsonify, render_template
import joblib
import logging  # Import Flask's logging modul
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get data from the form or request
    input_data=request.form.get("input-field")
    
    # Log the received data for debugging purposes

    # Load your trained ML model
    model = joblib.load("xgboost.pkl")

    # Convert input_data to a 2D array-like structure
    input_data = [(input_data)]  # Assuming input_data is a single float value

    # Check the shape of input_data
      # Add this line for debugging

    # Make predictions using the model
    prediction = model.predict(input_data)

    return render_template("result.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)