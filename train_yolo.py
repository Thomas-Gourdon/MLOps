import os
from pathlib import Path

def train_yolov3(data_yaml, weights='yolov3.pt', img_size=416, batch_size=16, epochs=10, device='cuda:0'):
    """
    Entraîne un modèle YOLOv3 sur vos données personnalisées.
    
    Args:
    - data_yaml (str): Chemin vers le fichier de configuration des données (data.yaml).
    - weights (str): Poids initiaux (pré-entraînés ou personnalisés).
    - img_size (int): Taille des images d'entrée (ex. 640x640).
    - batch_size (int): Taille du batch.
    - epochs (int): Nombre d'époques.
    - device (str): Appareil utilisé pour l'entraînement ('cuda' ou 'cpu').
    """

    train_script_path = "./yolov3/train.py"  # Chemin vers train.py
    data_yaml_path = './data/data.yaml'  # Chemin relatif à la racine de votre projet


    os.system(f"""
        python {train_script_path} --img {img_size} --batch {batch_size} --epochs {epochs} \
        --data {data_yaml_path} --weights {weights} --device {device}
    """)

# Chemin vers le fichier de configuration des données
data_yaml_path = 'yaml'  # Assurez-vous que le chemin est correct

# Entraîner le modèle
train_yolov3(data_yaml=data_yaml_path, weights='yolov3.pt', img_size=416, batch_size=16, epochs=1, device='cpu')
