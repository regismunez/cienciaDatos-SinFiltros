import csv
import math
import random
from datetime import datetime, timedelta

random.seed(42)
n_muestras = 5000

# Generar timestamps
fecha_inicio = datetime(2024, 1, 1)
timestamps = [(fecha_inicio + timedelta(hours=i)).strftime('%Y-%m-%d %H:%M:%S') for i in range(n_muestras)]

# Feature 1: Drift gradual
feature_1 = []
for i in range(n_muestras):
    drift = 30 * (i / n_muestras)
    valor = (100 + drift) + random.gauss(0, 15 + 5 * (i / n_muestras))
    feature_1.append(round(valor, 4))

# Feature 2: Uniforme
feature_2 = [round(random.uniform(10, 100), 4) for _ in range(n_muestras)]

# Feature 3: Exponencial
feature_3 = [round(random.expovariate(1/5), 4) for _ in range(n_muestras)]

# Target: Concept drift
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

target = []
for i in range(n_muestras):
    if i < n_muestras // 2:
        prob = sigmoid(0.05 * (feature_2[i] - 50))
    else:
        prob = sigmoid(-0.05 * (feature_2[i] - 50))
    target.append(1 if random.random() < prob else 0)

# Prediction: Modelo viejo
prediction = []
probability = []
for i in range(n_muestras):
    prob_modelo = sigmoid(0.05 * (feature_2[i] - 50))
    probability.append(round(prob_modelo + random.gauss(0, 0.1), 4))
    prediction.append(1 if prob_modelo > 0.5 else 0)

# Escribir CSV
with open('datos_drift_simulado.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'feature_1', 'feature_2', 'feature_3', 'target', 'prediction', 'probability'])
    for i in range(n_muestras):
        writer.writerow([timestamps[i], feature_1[i], feature_2[i], feature_3[i], target[i], prediction[i], probability[i]])

print(f"CSV creado: {n_muestras} filas")
print(f"Columnas: timestamp, feature_1, feature_2, feature_3, target, prediction, probability")
print(f"Feature 1 media inicio: {sum(feature_1[:100])/100:.1f}")
print(f"Feature 1 media final: {sum(feature_1[-100:])/100:.1f}")
correctas = sum(1 for i in range(n_muestras) if target[i] == prediction[i])
print(f"Accuracy del modelo: {correctas/n_muestras:.2%}")
