from flask import Flask, request, jsonify
import xgboost as xgb
import numpy as np

app = Flask(__name__)

# تحميل النموذج
model = xgb.XGBClassifier()
model.load_model("models/best_xgb_model.json")

@app.route("/")
def home():
    return "Welcome to the Disease Prediction API!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # جلب البيانات من الطلب بصيغة JSON
        input_data = request.get_json(force=True)

        # تحويل البيانات إلى مصفوفة NumPy
        features = np.array(input_data["features"]).reshape(1, -1)

        # إجراء التنبؤ
        prediction = model.predict(features)
        probability = model.predict_proba(features)

        return jsonify({
            "prediction": int(prediction[0]),
            "probability": probability.tolist()[0]
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
