from pymongo import MongoClient

client = MongoClient("mongodb+srv://cantanhede:teste1234@cluster0.va2dmwf.mongodb.net/cardio_risk_db?retryWrites=true&w=majority")
db = client["cardio_risk_db"]
colecao = db["predictions"]

dados = [
    {"nome": "Ana", "idade": 45, "genero": "feminino", "frequencia_cardiaca": 75, "pressao_sistolica": 120, "pressao_diastolica": 80, "glicose": 90, "ckmb": 1.2, "troponina": 0.1, "data_inclusao": "2025-04-15", "risco": "Baixo"},
    {"nome": "Bruno", "idade": 67, "genero": "masculino", "frequencia_cardiaca": 102, "pressao_sistolica": 160, "pressao_diastolica": 110, "glicose": 220, "ckmb": 35.0, "troponina": 2.5, "data_inclusao": "2025-04-14", "risco": "Alto"},
    {"nome": "Carlos", "idade": 52, "genero": "masculino", "frequencia_cardiaca": 80, "pressao_sistolica": 140, "pressao_diastolica": 90, "glicose": 180, "ckmb": 18.4, "troponina": 1.1, "data_inclusao": "2025-04-13", "risco": "Alto"},
    {"nome": "Daniela", "idade": 39, "genero": "feminino", "frequencia_cardiaca": 72, "pressao_sistolica": 115, "pressao_diastolica": 75, "glicose": 88, "ckmb": 0.9, "troponina": 0.05, "data_inclusao": "2025-04-12", "risco": "Baixo"},
    {"nome": "Eduardo", "idade": 60, "genero": "masculino", "frequencia_cardiaca": 95, "pressao_sistolica": 155, "pressao_diastolica": 100, "glicose": 210, "ckmb": 27.2, "troponina": 1.8, "data_inclusao": "2025-04-11", "risco": "Alto"},
    {"nome": "Fernanda", "idade": 42, "genero": "feminino", "frequencia_cardiaca": 78, "pressao_sistolica": 130, "pressao_diastolica": 85, "glicose": 100, "ckmb": 2.1, "troponina": 0.3, "data_inclusao": "2025-04-10", "risco": "Baixo"},
    {"nome": "Guilherme", "idade": 70, "genero": "masculino", "frequencia_cardiaca": 110, "pressao_sistolica": 170, "pressao_diastolica": 115, "glicose": 240, "ckmb": 38.5, "troponina": 2.9, "data_inclusao": "2025-04-09", "risco": "Alto"},
    {"nome": "Helena", "idade": 36, "genero": "feminino", "frequencia_cardiaca": 70, "pressao_sistolica": 110, "pressao_diastolica": 70, "glicose": 85, "ckmb": 0.8, "troponina": 0.02, "data_inclusao": "2025-04-08", "risco": "Baixo"},
    {"nome": "Igor", "idade": 58, "genero": "masculino", "frequencia_cardiaca": 98, "pressao_sistolica": 150, "pressao_diastolica": 95, "glicose": 190, "ckmb": 25.3, "troponina": 1.6, "data_inclusao": "2025-04-07", "risco": "Alto"},
    {"nome": "Joana", "idade": 40, "genero": "feminino", "frequencia_cardiaca": 76, "pressao_sistolica": 125, "pressao_diastolica": 82, "glicose": 95, "ckmb": 1.5, "troponina": 0.15, "data_inclusao": "2025-04-06", "risco": "Baixo"},
]

colecao.insert_many(dados)
print("10 registros inseridos com sucesso!")
