import csv
import re

# Fichiers
input_file = "contacts.csv"  # Fichier d'entrée
output_file = "contacts_new.csv"  # Fichier de sortie

# Fonction pour normaliser un numéro unique
def normalize_phone_number(phone):
    phone = re.sub(r'[^\d+]', '', phone)  # Supprimer espaces et caractères non numériques sauf '+'

    # Retirer l'indicatif béninois
    if phone.startswith("+229"):
        phone = phone[4:]
    elif phone.startswith("00229"):
        phone = phone[5:]
    elif phone.startswith("229") and len(phone) > 8:
        phone = phone[3:]
    
    return phone

# Fonction pour traiter les numéros multiples
def process_phone_numbers(phone_field):
    if not phone_field:
        return ""

    # Séparer les numéros multiples
    numbers = [normalize_phone_number(num.strip()) for num in phone_field.split(":::")]

    # Ajouter "01" si le numéro est un numéro béninois à 8 chiffres
    processed_numbers = [
        "+229 01" + num if re.match(r'^\d{8}$', num) else num for num in numbers
    ]

    # Recombiner les numéros
    return " ::: ".join(processed_numbers)

# Lecture et écriture des fichiers CSV
with open(input_file, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Traiter toutes les colonnes de numéros de téléphone
            for key in row.keys():
                if "Phone" in key and "Value" in key and row[key]:
                    row[key] = process_phone_numbers(row[key])
            writer.writerow(row)

print(f"Fichier mis à jour et sauvegardé sous le nom : {output_file}")
