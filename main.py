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

def exercice8():
    nombre=int(input("Selectionner votre nombre a diviser "))
    number=int(input("Selectionner votre diviseur "))
    if number==0:
        print("On ne peut pas diviser par 0")
    print("Votre résultat est", nombre/number)

def exercice9():
    nombre=int(input("Selectionner votre nombre "))
    puissance=int(input("Selectionner votre puissance "))
    print("Votre résultat est", nombre*puissance)

def exercice10():
    nombre=int(input("Selectionner un nombre qui sera multiplié par 2 "))
    print("Votre résultat est", nombre*2)

def exercice11():
    nombre=int(input("Selectionner un nombre qui sera divisé par 2 "))
    print("Votre résultat est", nombre/2)

def exercice12():
    for i in range(5):
        print("Ceci est mon message")

def exercice13():
    for i in range(1, 6):
        print(i)

def exercice14():
    nombre=int(2)
    for i in range(1, 6):
        print(f"{i} X 2", nombre*i)

def exercice15():
    nombre=int(input("Entrez la longueur d'un coté en centimètre "))
    print("Le carré à un périmètre de ",nombre*4)
    

def exercice16():
    nombre=int(input("Entrez la longueur d'un coté en centimètre "))
    print("Le carré à une aire de ",nombre*nombre)

def exercice17():
    nombre=int(input("Inserez les Euros "))
    print(f"{nombre} Euros font ",nombre*1.1,"Dollars")

def exercice18():
    nombre=int(input("Inserez les minutes "))
    print(nombre*60,"secondes")


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
    elif choix == "8":
        exercice8()
    elif choix == "9":
        exercice9()
    elif choix == "10":
        exercice10()
    elif choix == "11":
        exercice11()
    elif choix == "12":
        exercice12()
    elif choix == "13":
        exercice13()
    elif choix == "14":
        exercice14()
    elif choix == "15":
        exercice15()
    elif choix == "16":
        exercice16()
    elif choix == "17":
        exercice17()
    elif choix == "18":
        exercice18()
    else:
        print("Exercice non reconnu.")


if __name__ == "__main__":
    main()
