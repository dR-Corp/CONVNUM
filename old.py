import csv

# Nom des fichiers
input_file = "contacts.csv"  # Remplacez par le nom de votre fichier CSV original
output_file = "contacts_old.csv"  # Nom du fichier avec les modifications

# Lire et modifier le fichier
with open(input_file, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    # Conserver les en-têtes
    fieldnames = reader.fieldnames

    # Créer un nouveau fichier modifié
    with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        # Modifier chaque ligne
        for row in reader:
            if row["First Name"]:  # Vérifie si le prénom existe
                row["First Name"] += " OLD"
            writer.writerow(row)

print(f"Fichier mis à jour et enregistré sous le nom : {output_file}")