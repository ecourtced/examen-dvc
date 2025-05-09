import os
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Paths
input_path = "data/processed_data"
models_path = "models"
os.makedirs(models_path, exist_ok=True)

# Chargement des données
X_train = pd.read_csv(os.path.join(input_path, "X_train_scaled.csv"))
y_train = pd.read_csv(os.path.join(input_path, "y_train.csv")).values.ravel()

# Chargement des meilleurs paramètres
with open(os.path.join(models_path, "meilleurs_parametres.pkl"), "rb") as f:
    best_params = pickle.load(f)

# Entraînement du modèle
model = RandomForestRegressor(random_state=42, **best_params)
model.fit(X_train, y_train)

# Sauvegarde du modèle entraîné
with open(os.path.join(models_path, "modele_entraine.pkl"), "wb") as f:
    pickle.dump(model, f)