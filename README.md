# risco-cardiaco

# Equipe
- Diego Queiroz: Treinamento do modelo de machine learning e geração do arquivo .pkl com Scikit-learn
- Caio Queiroz: Desenvolvimento do backend (API Flask e integração com MongoDB).
- Matheus Menezes: Design e implementação do frontend (HTML/CSS/JS) e dashboard com Chart.js.
- Bruno Marques: Verificação de testes, conferência de dados, e garantia de qualidade do sistema.
- Lucas Henrique: Elaboração e execução dos testes do sistema.

O projeto utiliza um modelo de aprendizado de máquina para prever o risco de um paciente sofrer um ataque cardíaco, com base em variáveis clínicas como idade, pressão arterial, troponina, CK-MB, entre outras. Os dados são armazenados em MongoDB e visualizados via um dashboard interativo.

# Funcionalidades
- API Flask com predição de risco (endpoint /predict)
- Armazenamento automático em MongoDB Atlas
- Dashboard interativo com filtros e gráficos (Chart.js)
- Validação de dados no frontend
- Integração completa entre frontend, backend e banco

# Tecnologias Usadas
- MongoDB Atlas
- Chart.js
- HTML/CSS/JavaScript
- Modelo .pkl treinado

# Bibliotecas utlizadas
- flask: Flask, request, jsonify
- flask-cors: CORS
- pymongo
- scikit-learn
- joblib
- pandas

