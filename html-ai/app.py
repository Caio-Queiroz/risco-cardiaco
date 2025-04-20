from flask import Flask, request, jsonify
from flask_cors import CORS
import pymongo
from datetime import datetime
import pandas as pd
import joblib  # Corrigido: usar joblib em vez de pickle
import pickle
# Setup
app = Flask(__name__)
CORS(app)

# MongoDB
MONGO_URI = "mongodb+srv://cantanhede:teste1234@cluster0.va2dmwf.mongodb.net/cardio_risk_db?retryWrites=true&w=majority"
mongo_client = pymongo.MongoClient(MONGO_URI)

db = mongo_client["cardio_risk_db"]
predictions_col = db["predictions"]

# Modelo
with open('DT_from_pickle1.pkl', 'rb') as f:
    model = pickle.load(f)
# Mapeamento de gênero
def encode_gender(genero):
    return {"masculino": 0, "feminino": 1, "outro": 2}.get(genero.lower(), -1)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        print("📥 Dados recebidos:", data)

        features_dict = {
            "idade": [int(data["idade"])],
            "Genero": [encode_gender(data["genero"])],
            "frequencia_cardiaca": [int(data["frequencia_cardiaca"])],
            "pressao_sistolica": [int(data["pressao_sistolica"])],
            "pressao_diastolica": [int(data["pressao_diastolica"])],
            "glicose": [int(data["glicose"])],
            "ckmb": [float(data["ckmb"])],
            "troponina": [float(data["troponina"])]
        }


        df = pd.DataFrame(features_dict)
        prediction = model.predict(df)[0]

        result = {
            "nome": data["nome"],
            "idade": data["idade"],
            "genero": data["genero"],
            "frequencia_cardiaca": data["frequencia_cardiaca"],
            "pressao_sistolica": data["pressao_sistolica"],
            "pressao_diastolica": data["pressao_diastolica"],
            "glicose": data["glicose"],
            "ckmb": data["ckmb"],
            "troponina": data["troponina"],
            "data_inclusao": data["data_inclusao"],
            "risco": "Alto" if prediction == 1 else "Baixo",
            "created_at": datetime.now()
        }

        predictions_col.insert_one(result)
        return jsonify({"risco": result["risco"]})
    except Exception as e:
        print("❌ ERRO AO PREDIZER:", e)
        return jsonify({"error": str(e)}), 400


@app.route("/predictions", methods=["GET"])
def get_predictions():
    registros = list(predictions_col.find({}, {"_id": 0}))
    return jsonify(registros)

if __name__ == "__main__":
    app.run(debug=True)
