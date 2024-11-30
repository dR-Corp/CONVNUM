import re

def normalize_and_modify_numbers(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        # Identifier les lignes contenant des numéros (TEL ou itemX.TEL)
        if re.match(r"^TEL|^item\d+\.TEL", line):
            # Extraire le numéro et supprimer les espaces
            number = re.sub(r"[^\d+]", "", line.split(":")[1].strip())

            # Vérifier les numéros béninois et appliquer les modifications
            if number.startswith("+229") or number.startswith("00229") or number.startswith("229"):
                # Remplacer le préfixe par "+229 01"
                modified_number = re.sub(r"^\+?229|^00229", "+22901", number)
                updated_line = f"{line.split(':')[0]}:{modified_number}\n"
            elif len(number) == 8 and number.isdigit():
                # Pour les numéros de 8 chiffres sans indicatif, ajouter "+229 01"
                modified_number = f"+22901{number}"
                updated_line = f"{line.split(':')[0]}:{modified_number}\n"
            else:
                # Garder les autres numéros inchangés
                updated_line = line
            updated_lines.append(updated_line)
        else:
            # Garder les autres lignes inchangées
            updated_lines.append(line)

    # Écrire les modifications dans un nouveau fichier
    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(updated_lines)

# Chemins des fichiers d'entrée et de sortie
input_file = "contacts.vcf"  # Remplacez par le chemin de votre fichier source
output_file = "new_contacts.vcf"  # Le fichier modifié

# Exécuter la fonction
normalize_and_modify_numbers(input_file, output_file)

print(f"Fichier VCF mis à jour sauvegardé sous : {output_file}")
