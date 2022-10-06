'''Quelques exercices sur les fonctionsaa'''

# Demander le nom
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input(" Quel est votre nom ? ")
    return reponse_nom


# Demander l'age
def demander_age():
    age_int = 0
    while age_int == 0:
        age_chaine = input(" Quel est votre age ? ")
        try:
            age_int = int(age_chaine)
        except ValueError:
            print("ERREUR: Vous devez entrer un nombre pour l'age. ")
    return age_int


# fonction pour affficher les informations

def afficher_informations_personne(nom,age):
    print("Vous vous appelez " + nom + " vous avez " + str(age) + " ans.")
    print("L'an prochain, vous aurez " + str(age + 1) + " ans!")


# Appel des fonctions
nom = demander_nom()
age = demander_age()
response = afficher_informations_personne(nom, age)



