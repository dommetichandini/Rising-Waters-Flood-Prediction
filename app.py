from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model    = pickle.load(open("models/flood_model.pkl", "rb"))
scaler   = pickle.load(open("models/scaler.pkl", "rb"))
features = pickle.load(open("models/features.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = []
        for feature in features:
            value = request.form.get(feature, 0)
            input_data.append(float(value))

        input_array  = np.array(input_data).reshape(1, -1)
        input_scaled = scaler.transform(input_array)
        prediction   = model.predict(input_scaled)[0]

        if prediction == 1:
            return render_template("chance.html")
        else:
            return render_template("no_chance.html")

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)