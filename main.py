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
    print(f"{nombre} Euros font",nombre*1.1,"Dollars")

def exercice18():
    nombre=int(input("Inserez les minutes "))
    print(nombre*60,"secondes")

def exercice19():
    nombre=int(input("Inserez le prix Hors Taxe "))
    print(nombre*1.2,"Tout Taxe Comprise")
    
def exercice20():
    prenom=input("Veuillez inserez votre prenom ")
    age=int(input("Veuillez inserez votre age "))
    print(f"Vous êtes {prenom} et vous avez {age} ans")

def exercice21():
    nombre=int(input("Inserez un Chiffre parmi -3, 0 ou 5 "))
    if nombre==0:
        print("Le résultat du test est Nul")
    if nombre==5:
        print("Le résultat du test est Positif")
    if nombre==-3:
        print("Le résultat du test est Négatif")

def exercice22():
    âge=int(input("Inserez votre âge "))
    if âge<18:
        print("Mineur")
    else:
        print("Majeur")

def exercice23():
    note=int(input("Inserez votre note "))
    if note>12:
        print("Validé")
    else:
        print("Non Validé")

def exercice24():
    nombre=int(input("Inserez un nombre"))
    number=int(input("Inserez un nombre"))
    if nombre>number:
       print(f"{nombre} est plus grand que {number}")
    elif nombre<number:
       print(f"{number} est plus grand que {nombre}")
    
def exercice25():
    nombre=int(input("Inserez un nombre "))
    number=int(input("Inserez un nombre "))
    if nombre>number:
       print(f"{nombre} et {number} ne sont pas croissant")
    elif nombre<number:
       print(f"{nombre} et {number} sont croissant")

def exercice26():
    nombre=int(input("Inserez un nombre "))
    diviseur=int(5)
    last_digit = nombre % 10
    if last_digit == 0 or last_digit == 5:
        print(f"{nombre} est un divisible de 5")
    elif last_digit != 0 or last_digit != 5:
        print(f"{nombre} est non divisible par 5")

def exercice27():
    âge=int(input("Inserez votre âge "))
    if âge<12:
        print("Enfant")
    elif âge>18:
        print("Adulte")
    elif 12 <= âge <= 17:
        print("Adolescent")

def exercice28():
    temperature=int(input("Inserez la température de l'eau "))
    if temperature<0:
        print("l'eau est solide")
    elif temperature>100:
        print("l'eau est gazeuse")
    elif 0 <= temperature <= 100:
        print("l'eau est liquide")

def exercice29():
    note=int(input("Entrez votre note"))
    if note<10.99:
        print("Recalé")
    elif note<=13.99:
        print("Passable")
    elif note<=16.99:
        print("Bien")
    elif note<=20:
        print("Très bien")
      
def exercice30():
    n=int(input("Inserez votre nombre "))
    for n in range(1, n):
        print(n)

    
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
    elif choix == "19":
        exercice19()
    elif choix == "20":
        exercice20()
    elif choix == "21":
        exercice21()
    elif choix == "22":
        exercice22()
    elif choix == "23":
        exercice23()
    elif choix == "24":
        exercice24()
    elif choix == "25":
        exercice25()
    elif choix == "26":
        exercice26()
    elif choix == "27":
        exercice27()
    elif choix == "28":
        exercice28()
    elif choix == "29":
        exercice29()
    elif choix == "30":
        exercice30()
    else:
        print("Exercice non reconnu.")


if __name__ == "__main__":
    main()
