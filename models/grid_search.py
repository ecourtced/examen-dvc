import os
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

# path
input_path = "data/processed_data"
models_path = "models"
os.makedirs(models_path, exist_ok=True)

# Chargement des données
X_train = pd.read_csv(os.path.join(input_path, "X_train_scaled.csv"))
y_train = pd.read_csv(os.path.join(input_path, "y_train.csv")).values.ravel()

# Définition du modèle et de la grille
model = RandomForestRegressor(random_state=42)
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 5, 10],
    "min_samples_split": [2, 5, 10]
}

# GridSearchCV
grid_search = GridSearchCV(model, param_grid, cv=5, scoring="neg_mean_squared_error", n_jobs=-1)
grid_search.fit(X_train, y_train)

# Sauvegarde des meilleurs paramètres
with open(os.path.join(models_path, "meilleurs_parametres.pkl"), "wb") as f:
    pickle.dump(grid_search.best_params_, f)