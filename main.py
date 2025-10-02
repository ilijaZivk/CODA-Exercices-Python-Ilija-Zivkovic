def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")
 
def exercice2():
    prenom=input("Quel est votre prenom")
    print("Votre prénom est ", prenom)

def exercice3():
    print("Premiere ligne")
    print("Deuxieme ligne")
    print("Troisieme ligne")

def exercice4():
    age=int(input("Insérez votre année de naissance "))
    print("Vous avez", 2025-age,"ans")

def exercice5():
    nombre=int(input("Selectionner votre nombre a additionner "))
    number=int(input("Selectionner votre autre nombre "))
    print("Votre résultat est", nombre+number)

def exercice6():
    nombre=int(input("Selectionner votre nombre a soustraire "))
    number=int(input("Selectionner votre nombre "))
    print("Votre résultat est", nombre-number)

def exercice7():
    nombre=int(input("Selectionner votre nombre a multiplier "))
    number=int(input("Selectionner votre multiplicateur "))
    print("Votre résultat est", nombre*number)

    
def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exercice4()
    elif choix == "5":
        exercice5()
    elif choix == "6":
        exercice6()
    elif choix == "7":
        exercice7()
    else:
        print("Exercice non reconnu.")


if __name__ == "__main__":
    main()
