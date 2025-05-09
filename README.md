# Examen DVC et Dagshub
Dans ce dépôt vous trouverez l'architecture proposé pour mettre en place la solution de l'examen. 

```bash       
├── examen_dvc          
│   ├── data       
│   │   ├── processed      
│   │   └── raw       
│   ├── metrics       
│   ├── models      
│   │   ├── data      
│   │   └── models        
│   ├── src       
│   └── README.md.py       
```
N'hésitez pas à rajouter les dossiers ou les fichiers qui vous semblent pertinents.

Vous devez dans un premier temps *Fork* le repo et puis le cloner pour travailler dessus. Le rendu de cet examen sera le lien vers votre dépôt sur DagsHub. Faites attention à bien mettre https://dagshub.com/licence.pedago en tant que colaborateur avec des droits de lecture seulement pour que ce soit corrigé.

Vous pouvez télécharger les données à travers le lien suivant : https://datascientest-mlops.s3.eu-west-1.amazonaws.com/mlops_dvc_fr/raw.csv.

## Les instructions pour lancer les scripts
   1 - python src/data/split_data.py
   2 - python src/data/normalize_data.py
   3 - python models/grid_search.py
   4 - python models/train_model.py

## connexion du repo à dagshub

## instructions pour effectuer l'examen 
    1 - dvc init
    2 - git add .
    3 - git commit -m "1er ajout des scripts et de la config dvc"
    4 - git push
    
    5 - dvc remote add origin s3://dvc
    6 - dvc remote modify origin endpointurl https://dagshub.com/cedric.ecourtemer/examen-dvc.s3
    
    ## Probleme de connexion au repo dagshub
    - dvc remote remove origin
    - dvc remote add origin https://dagshub.com/ecourtced/examen-dvc.dvc
    - dvc remote default origin
    - git add .dvc/config
    - git commit -m "Ajout du remote DagsHub comme remote DVC par défaut"
    - dvc push

    ### Résolution des problèmes liés à l'envoi dans GIT
    7 - git rm --cached data/processed_data/X_train_scaled.csv
    8 - git rm --cached data/processed_data/X_test_scaled.csv
    9 - git commit -m "stop tracking data/processed_data/X_train_scaled.csv et x_test_scaled.cvs"
    10 - git rm -r --cached 'models/meilleurs_parametres.pkl'
    11 - git commit -m "stop tracking models/meilleurs_parametres.pkl"     
    12 - git rm -r --cached 'models/modele_entraine.pkl'
    13 - git commit -m "stop tracking models/modele_entraine.pkl"
    14 - git rm -r --cached 'data/predictions.csv'
    15 - git commit -m "stop tracking data/predictions.csv"
    16 - git rm -r --cached 'metrics/scores.json'
    17 - git commit -m "stop tracking metrics/scores.json"
    18 - git rm -r --cached 'metrics/resultats.png'
    19 - git commit -m "stop tracking metrics/resultats.png" 

    
    ## phase de push
    git add dvc.lock data/.gitignore metrics/.gitignore
    dvc remote modify origin --local auth basic
    dvc remote modify origin --local user <ton_nom_utilisateur_dagshub>
    dvc remote modify origin --local password <ton_token>
    dvc push


