import os
import pandas as pd
import pickle
import json
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Paths
data_path = "data/processed_data"
models_path = "models"
metrics_path = "metrics"
output_pred_path = "data/predictions.csv"
output_fig_path = os.path.join(metrics_path, "resultats.png")
os.makedirs(metrics_path, exist_ok=True)

# Chargement des données
X_test = pd.read_csv(os.path.join(data_path, "X_test_scaled.csv"))
y_test = pd.read_csv(os.path.join(data_path, "y_test.csv")).values.ravel()

# Chargement du modèle
with open(os.path.join(models_path, "modele_entraine.pkl"), "rb") as f:
    model = pickle.load(f)

# Prédictions
y_pred = model.predict(X_test)

# Sauvegarde des prédictions
pred_df = pd.DataFrame({"y_true": y_test, "y_pred": y_pred})
pred_df.to_csv(output_pred_path, index=False)

# Calcul des scores
scores = {
    "mse": mean_squared_error(y_test, y_pred),
    "mae": mean_absolute_error(y_test, y_pred),
    "r2": r2_score(y_test, y_pred)
}

# Sauvegarde des scores
with open(os.path.join(metrics_path, "scores.json"), "w") as f:
    json.dump(scores, f, indent=4)

# Affichage graphique
plt.figure(figsize=(8, 8))
plt.scatter(y_test, y_pred, alpha=0.5, label="Predictions")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", label="Ideal")
plt.xlabel("Valeurs réelles")
plt.ylabel("Prédictions")
plt.title("Prédictions vs Valeurs réelles")
plt.legend()
# Affichage des métriques sur le graphique
metrics_text = f"MSE: {scores['mse']:.2f}\nMAE: {scores['mae']:.2f}\nR²: {scores['r2']:.2f}"
plt.gcf().text(0.15, 0.85, metrics_text, fontsize=12, bbox=dict(facecolor="white", alpha=0.7))
plt.tight_layout()
plt.savefig(output_fig_path)
plt.close()