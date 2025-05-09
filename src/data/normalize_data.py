import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Chemins
input_dir = "data/processed_data"
output_dir = "data/processed_data"
os.makedirs(output_dir, exist_ok=True)

# Chargement des données
X_train = pd.read_csv(os.path.join(input_dir, "X_train.csv"))
X_test = pd.read_csv(os.path.join(input_dir, "X_test.csv"))

# Sélection des colonnes numériques
num_cols = X_train.select_dtypes(include=["number"]).columns
X_train_num = X_train[num_cols]
X_test_num = X_test[num_cols]

# Normalisation
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_num)
X_test_scaled = scaler.transform(X_test_num)

# Conversion en DataFrame pour garder les colonnes d'origine
X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train_num.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test_num.columns)

# Sauvegarde
X_train_scaled.to_csv(os.path.join(output_dir, "X_train_scaled.csv"), index=False)
X_test_scaled.to_csv(os.path.join(output_dir, "X_test_scaled.csv"), index=False)