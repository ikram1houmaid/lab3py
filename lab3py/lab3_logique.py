
age = 22
permis = True
casier_vierge = False

# Opérateur AND
peut_conduire = (age >= 18) and permis
print("Peut conduire :", peut_conduire)

# Opérateur OR
peut_louer_voiture = (age >= 21) or (permis and casier_vierge)
print("Peut louer une voiture :", peut_louer_voiture)

# Opérateur NOT
sanction = not casier_vierge
print("Sanction :", sanction)
