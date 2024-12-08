import os
import shutil

def move_labels(image_root_dir, label_root_dir):
    """
    Déplace les fichiers de labels associés aux images dans les sous-dossiers labels/train, labels/val, et labels/test.
    
    Args:
    - image_root_dir (str): Chemin du dossier contenant train/, val/, test/ avec les images.
    - label_root_dir (str): Chemin du dossier contenant les labels (tous regroupés).
    """
    for split in ['train', 'val', 'test']:
        img_dir = os.path.join(image_root_dir, split)
        label_split_dir = os.path.join(label_root_dir, split)

        # Créer le sous-dossier pour les labels s'il n'existe pas
        os.makedirs(label_split_dir, exist_ok=True)

        # Parcourir les fichiers d'images dans le dossier courant
        for image_file in os.listdir(img_dir):
            if image_file.endswith(('.jpg', '.png', '.jpeg')):
                # Remplacer l'extension de l'image par `.txt` pour trouver le label
                label_file = os.path.splitext(image_file)[0] + '.txt'
                label_path = os.path.join(label_root_dir, label_file)

                # Vérifier si le fichier de label existe
                if os.path.exists(label_path):
                    shutil.move(label_path, os.path.join(label_split_dir, label_file))
                    print(f"Déplacé: {label_file} -> {label_split_dir}")
                else:
                    print(f"Label manquant pour l'image : {image_file}")

# Chemins vers les répertoires
image_root_directory = './data/images/'  # Remplacez par le chemin vers vos dossiers train/, val/, test/
label_root_directory = './data/labels/'  # Remplacez par le chemin vers le dossier contenant les labels regroupés

# Exécution
move_labels(image_root_directory, label_root_directory)
