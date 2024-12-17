import string
def chiffre_cesar(texte, decalage):
    alphabet = string.ascii_lowercase
    texte_chiffre = ""
    for char in texte:
        if char.islower():
            indice = alphabet.index(char)
            nouveau_indice = (indice + decalage) % 26
            texte_chiffre += alphabet[nouveau_indice]
        else:
            texte_chiffre += char
            
    return texte_chiffre
texte = "bonjour"
decalage = 3
texte_chiffre = chiffre_cesar(texte, decalage)
print(texte_chiffre)
def dechiffre_cesar(texte_chiffre, decalage):
    # Définir l'alphabet des lettres minuscules
    alphabet = string.ascii_lowercase
    texte_dechiffre = ""
    
    for char in texte_chiffre:
        # Si le caractère est une lettre minuscule
        if char.islower():
            # Trouver l'indice du caractère dans l'alphabet
            indice = alphabet.index(char)
            # Appliquer le décalage négatif avec modulo 26
            nouveau_indice = (indice - decalage) % 26
            # Ajouter le caractère déchiffré à la chaîne résultat
            texte_dechiffre += alphabet[nouveau_indice]
        else:
            # Si ce n'est pas une lettre minuscule, on laisse le caractère inchangé
            texte_dechiffre += char
            
    return texte_dechiffre

# Exemple d'utilisation
texte_chiffre = "erqmxxu"
decalage = 3
texte_dechiffre = dechiffre_cesar(texte_chiffre, decalage)
print(texte_dechiffre)  # Affiche "bonjour"

def dechiffre_cesar(texte_chiffre, decalage):
    alphabet = string.ascii_lowercase
    texte_dechiffre = ""
    
    for char in texte_chiffre:
        if char.islower():
            indice = alphabet.index(char)
            nouveau_indice = (indice - decalage) % 26
            texte_dechiffre += alphabet[nouveau_indice]
        else:
            texte_dechiffre += char
    
    return texte_dechiffre

def brute_force(texte_chiffre):
    # Appliquer tous les décalages possibles de 0 à 25
    for decalage in range(26):
        texte_dechiffre = dechiffre_cesar(texte_chiffre, decalage)
        print(f"Décalage {decalage}: {texte_dechiffre}")

# Exemple d'utilisation
texte_chiffre = "erqmxxu"  # Exemple de texte chiffré
brute_force(texte_chiffre)
# Fonction de chiffrement de César, que nous utiliserons dans le chiffrement de Vigenère
def chiffre_cesar(texte, decalage):
    alphabet = string.ascii_lowercase
    texte_chiffre = ""
    
    for char in texte:
        if char.islower():
            indice = alphabet.index(char)
            nouveau_indice = (indice + decalage) % 26
            texte_chiffre += alphabet[nouveau_indice]
        else:
            texte_chiffre += char
    
    return texte_chiffre

# Fonction de chiffrement de Vigenère
def chiffre_vigenere(texte, cle):
    texte_chiffre = ""
    cle = cle.lower()  # S'assurer que la clé est en minuscules
    
    for i, char in enumerate(texte):
        if char.islower():  # Si c'est une lettre minuscule
            decalage = string.ascii_lowercase.index(cle[i % len(cle)])  # Trouver le décalage basé sur la clé
            texte_chiffre += chiffre_cesar(char, decalage)
        else:
            texte_chiffre += char  # Si ce n'est pas une lettre, on l'ajoute tel quel
    
    return texte_chiffre

# Exemple d'utilisation
texte = "bonjour"
cle = "clé"
texte_chiffre = chiffre_vigenere(texte, cle)
print(texte_chiffre)  # Affiche le texte chiffré avec la clé "clé"

