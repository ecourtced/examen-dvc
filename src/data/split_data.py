import os
import pandas as pd
from sklearn.model_selection import train_test_split

# Chemins
input_path = "data/raw_data/raw.csv"
output_dir = "data/processed_data"
os.makedirs(output_dir, exist_ok=True)

# Lecture des données
df = pd.read_csv(input_path)

# Séparation X/y
X = df.drop(columns=["silica_concentrate"])
y = df["silica_concentrate"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sauvegarde
X_train.to_csv(os.path.join(output_dir, "X_train.csv"), index=False)
X_test.to_csv(os.path.join(output_dir, "X_test.csv"), index=False)
y_train.to_csv(os.path.join(output_dir, "y_train.csv"), index=False)
y_test.to_csv(os.path.join(output_dir, "y_test.csv"), index=False)