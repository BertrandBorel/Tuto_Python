# Créer un générateur de mot de passe avec Python
# Source = Revue Coding, n°18, p.27-28.

import random

# L'utilisateur rentre la longueur du mot de passe
longueur_mdp = int(input("Longueur du mot de passe : "))

# caractères pouvant composer le mdp
caracteres = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# on prend un échantillon en fonction de la longueur du mdp
p = "".join(random.sample(caracteres, longueur_mdp))
print(p)