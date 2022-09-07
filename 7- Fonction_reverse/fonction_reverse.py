# Inverser une chaîne de caractère en Python 

# Source = Revue Coding, n°18, p.28.

def reverse(s):
    str = ""
    # on ajoute chaque élément dans une variable
    # ... ce qui écrit l'inverse du mot
    for i in s :
        str = i + str
    return str

s = "Exemple"

print("Texte d'origine : ", end="")
print(s)

print("Texte inversé ", end="")
# appel de la fonction
print((reverse(s)))