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
    print(2025-age)
    
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
    else:
        print("Exercice non reconnu.")


if __name__ == "__main__":
    main()
