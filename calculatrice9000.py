# On crée une liste vide pour stocker l'hitorique des calculs
historique = []

# On définit une fonction pour effectuer les calculs
def calculatrice(num1, type_opération, num2):
    # On vérifie le type d'opération et on effectue le calcul correspondant
    if type_opération == '+':
        result = num1 + num2
    elif type_opération == '-':
        result = num1 - num2
    elif type_opération == '*':
        result = num1 * num2
    elif type_opération == '/':
        result = num1 / num2
    else : 
        # Si l'opération n'est pas reconnue, on affiche un message d'erreur
        print("Opération incorrecte")
        return None
    
    # On affiche le résultat du calcul
    print(f"Le resultat de {num1} {type_opération} {num2} est {result}")
    
    # On ajoute le calcul et le résultat à l'historique
    calculation = f"{num1} {type_opération} {num2} = {result}"
    historique.append(calculation)

    return result

# On entre dans une boucle infinie pour permettre à l'utilisateur de faire plusieurs calculs
while True:
    # On demande à l'utilisateur d'entrer les nombres et l'opération
    # La fonction input() est utilisée pour obtenir l’entrée de l’utilisateur et int() est utilisée pour convertir cette entrée en un nombre entier.
    num1 = int(input('Entrer un premier nombre entier : '))
    type_opération = input('Entrer le type de calcul souhaité : ')
    num2 = int(input('Entrer un deuxième nombre entier : '))
    
    # On effectue le calcul et on ajoute le résultat à l’historique.
    calculatrice(num1, type_opération, num2)

    # Cette ligne définit une variable continuer à True. Cette variable est utilisée pour contrôler si l’utilisateur veut continuer à interagir avec l’historique ou revenir à la calculatrice.
    continuer = True
    # Cette ligne commence une autre boucle qui continuera à s’exécuter tant que la variable continuer est True
    while continuer:
        print("Voulez-vous voir l'historique des calculs ? (oui/non)")
        #Cette ligne obtient la réponse de l’utilisateur à la question précédente.
        user_input = input()
        if user_input.lower() == 'non':
            # Interrompt la boucle et le programme revient à la calculatrice.
            break
        elif user_input.lower() == 'oui':
            # Ces lignes parcourent chaque calcul dans l’historique et l’affichent à l’utilisateur.
            for calcul in historique:
                print(calcul)
            while True:
                print("Voulez-vous supprimer l'historique ? (oui/non)")
                user_input = input()
                if user_input.lower() == 'oui':
                    historique.clear()
                    print("L'historique a été supprimé.")
                    # La variable continuer est définie sur False, ce qui interrompt la boucle et le programme revient à la calculatrice.
                    continuer = False
                    break
                elif user_input.lower() == 'non':
                    continuer = False
                    break
                else:
                    print("Entrée non valide, veuillez réessayer")
        else:
            print("Entrée non valide, veuillez réessayer")