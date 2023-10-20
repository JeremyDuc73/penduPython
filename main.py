import random

choix = ["mercredi", "fromage", "wagon", "kilogramme", "bonsoir", "gourmandise"]
solution = random.choice(choix)

tentatives = 7
affichage = ""
lettres_trouvees = ""

for l in solution:
    affichage = affichage + "_ "

while tentatives > 0:
    print("\nMot à deviner : ", affichage)
    proposition = input("proposez une lettre : ")[0:1].lower()

    if proposition == "":
        print("-> Veuillez saisir un caractère")
    elif proposition in lettres_trouvees:
        print("-> la lettre a déjà été trouvée")
    elif proposition.isnumeric():
        print("-> les chiffres et nombres ne sont pas acceptés")
    elif proposition in solution:
        lettres_trouvees = lettres_trouvees + proposition
        print("-> Bien vu!")
    else:
        tentatives = tentatives - 1
        print("-> La lettre n'est pas présente\n")
        if tentatives == 0:
            print(" ==========Y= ")
        if tentatives <= 1:
            print(" ||/       |  ")
        if tentatives <= 2:
            print(" ||        0  ")
        if tentatives <= 3:
            print(" ||       /|\ ")
        if tentatives <= 4:
            print(" ||       /|  ")
        if tentatives <= 5:
            print("/||           ")
        if tentatives <= 6:
            print("==============\n")

    affichage = ""
    for x in solution:
        if x in lettres_trouvees:
            affichage += x + " "
        else:
            affichage += "_ "

    if "_" not in affichage:
        print(">>> Gagné! <<<")
        break

print("\n    * Fin de la partie *    ")