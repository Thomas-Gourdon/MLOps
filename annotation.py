import os

# Dossier contenant vos fichiers labels
label_dir = "C:/Users/tomaz/Documents/Projet_Git/MLOps/data/labels/test"  # à modifier en fonction de votre chemin

# Dictionnaire qui associe les noms d'images aux classes
class_mapping = {
    "mure": 0,
    "pas_mure": 1,
    "tres_mure": 2,
    "pourrie": 3
}

# Fonction pour modifier le fichier txt avec la bonne classe
def update_label_file(label_file):
    # Extraire le nom de la classe à partir du nom du fichier label (avant le premier underscore)
    label_name = os.path.basename(label_file)
    
    # Identifier la classe à partir du début du nom du fichier
    for class_name in class_mapping:
        if label_name.startswith(class_name):
            class_id = class_mapping[class_name]
            
            # Ouvrir et modifier le fichier label
            with open(label_file, 'r') as f:
                lines = f.readlines()

            # Modifier chaque ligne avec la bonne classe
            for i in range(len(lines)):
                parts = lines[i].split()
                if len(parts) > 0:
                    parts[0] = str(class_id)  # Remplacer l'ID de la classe par la bonne classe
                    lines[i] = " ".join(parts) + '\n'
            
            # Réécrire les modifications dans le fichier
            with open(label_file, 'w') as f:
                f.writelines(lines)
            print(f"Le fichier {label_file} a été mis à jour avec la classe {class_id}.")
            return
    print(f"Aucune correspondance de classe pour le fichier label {label_name}.")

def process_directory(label_dir):
    # Parcourir tous les fichiers du répertoire labels
    for label_name in os.listdir(label_dir):
        # Vérifier si le fichier est un fichier label (extension .txt)
        if label_name.endswith('.txt'):
            label_file = os.path.join(label_dir, label_name)
            # Mettre à jour le fichier label
            update_label_file(label_file)

if __name__ == "__main__":
    # Lancer le traitement
    process_directory(label_dir)
