def message_niveau(avancement):
    # apres page d'accueil (01)
    if avancement == 1:
        message_afficher = "Un tremblement de terre a eu lieu a Bordeaux _nvous êtes bloqué dans l'école EPSI vous devez _nrentrer  chez vous avant que Bordeaux _ndisparaisse de la carte. _nVous avez une 80 secondes."
    # apres page d'accueil (02)
    elif avancement == 2:
        message_afficher = "Attention des décombres vous empêche de sortir _nde la salle de cours ! Trouvez la sortie !"
    # apres niveau 1
    elif avancement == 11:
        message_afficher = "Vous venez de sortir de la classe maintenant _nil faut trouver les escalier du batiment !"
    # apres niveau 2
    elif avancement == 21:
        message_afficher = "Félicitation vous avez trouvé les escalier !!! _nMalheureusement la porte est inaccessible _ntrouver la sortie de secours !"
    # deuxieme message apres niveau 2
    elif avancement == 22:
        message_afficher = "Attention le prof de python ne veut pas vous _nlaisser partir ! _nNe vous faites pas attraper !"
    # apres niveau 3
    elif avancement == 31:
        message_afficher = "Echappé vous de la ville !"
    # apres niveau 4
    elif avancement == 41:
        message_afficher = "Felicitation vous vous êtes échappé _navant le temps imparti !"
    else :
        return

    return message_afficher
