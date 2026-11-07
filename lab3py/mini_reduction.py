
try:
    prix_initial = float(input("Prix du produit (€) : "))

    if prix_initial <= 0:
        print("Le prix doit être positif.")
        exit()

except ValueError:
    print("Saisie invalide pour le prix.")
    exit()

statut = input("Êtes-vous étudiant ? (o/n) ").strip().lower()

if statut not in ["o", "n"]:
    print("Réponse invalide.")
    exit()

try:
    fidelite = int(input("Fidélité (en années) : "))

    if fidelite < 0:
        print("La fidélité ne peut pas être négative.")
        exit()

except ValueError:
    print("Saisie invalide pour la fidélité.")
    exit()

reduction = 0.0

# Réduction étudiant : 10 %
if statut == "o":
    reduction += prix_initial * 0.10

# Réduction fidélité : 15 %
if fidelite >= 5:
    reduction += prix_initial * 0.15

# Réduction supplémentaire de 5 €
if prix_initial > 100:
    reduction += 5.0

# Calcul du prix final
prix_final = prix_initial - reduction

# Empêcher un prix négatif
if prix_final < 0:
    prix_final = 0.0

print("\n===== RÉSULTAT =====")
print(f"Prix initial : {prix_initial:.2f} €")
print(f"Réduction totale : {reduction:.2f} €")
print(f"Prix final : {prix_final:.2f} €")
