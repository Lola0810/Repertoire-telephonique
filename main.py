def menu():
    listemenu = ["0 - quitter",
                 "1 : Ecrire dans le répertoire",
                 "2 - Recherche dans le répertoire"]

    # On loop la liste afin qu'elle s'affiche joliement
    for categorie in listemenu:
        print(categorie, end="\n")

    choix = int(input("Quel est votre choix ?"))
    if choix is None or choix > 2:
        menu()
    elif choix == 0:
        exit()
    elif choix == 1:
        nom = input("Nom (0 pour terminer)")

        if choix == 0:
            menu()
        else:
            choixUn(nom)

    elif choix == 2:
        # On stock le numero de telephone le résultat de la lecture du nom recherché
        nom = input("Entrez le nom demandé: ")
        with open('repertoire.txt', 'r') as f:
            # Regarde chaque ligne afin de trouver le bon numéro
            telephone = lecture(nom)
            # Si le resultat est trouvable alors il affiche le numéro
            if telephone is not None:
                print(f'Le numéro de la recherche est : {telephone}')
                menu()
                # Sinon il affiche "Inconnu"
            else:
                print('Inconnu')
                menu()

#Permet au programme de demander le numéro et de le return dans le programme
def demandernum():
    return input("Numéro de téléphone:")

#Permet de proposer un rename de l'utilisateur saisi
def choixUn(premierNom):
    telephone = demandernum()
    if len(telephone) > 10:
        print("Erreur le numéro comporte trop de chiffres. Veuillez réessayer.")
        choixUn(premierNom)
    else:
        nom = input("Nom (0 pour terminer)")
        if nom == '0':
            ecriture(premierNom, telephone)
        else:
            ecriture(nom, telephone)

#Permet d'écrire dans le répertoire le nom et le téléphone saisi
def ecriture(nom, telephone):
    with open('repertoire.txt', 'a') as f:
        f.write(nom + ' ' + telephone + '\n')
        f.close()

#Permet de lire dans le répertoire
def lecture(nom):
    with open('repertoire.txt', 'r') as f:
        # Regarde chaque ligne afin de trouver le bon numéro
        for ligne in f:
            # Permet de transformer la chaine de caractère en liste et sépare les éléments à chaque espace (supprimer l'espace)
            informations = ligne.split(' ')
            # Regarde le premier élément l'élément 0 de la liste de la ligne
            if nom == informations[0]:
                # On return le deuxieme élément de la liste de la liste
                return informations[1]
        return None


menu()