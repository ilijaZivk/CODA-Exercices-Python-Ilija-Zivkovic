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

def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    else:
        print("Exercice non reconnu.")


if __name__ == "__main__":
    main()
