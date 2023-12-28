import random


# Le code suivant permet de créer un labyrinthe de facon aleatoire
# Le labyrinthe a été créé selon la vidéo ci-dessous qui vous explique le fonctionnement global
# https://www.youtube.com/watch?v=K7vaT8bZRuk

# Le labyrinthe sera toujours carré avec une arête de longueur "dimension" qui correspond aux nombres de cellules
def generateur_laby(dimension):
    # Le labyrinthe doit toujours être impair donc si ce n'est pas le cas, on lui rajoute une colonne
    if dimension % 2 == 0:
        dimension += 1

    # On crée une matrice remplie de 1 suivant la dimension définie
    # Pour dimension = 7 on aurait :
    # [[1,1,1,1,1,1,1],
    #  [1,1,1,1,1,1,1],
    #  [1,1,1,1,1,1,1],
    #  [1,1,1,1,1,1,1],
    #  [1,1,1,1,1,1,1],
    #  [1,1,1,1,1,1,1],
    #  [1,1,1,1,1,1,1]]
    maze = [[1] * dimension for _ in range(dimension)]

    # On remplace tous les chemins disponibles en commençant par 4.
    # 2 et 3 seront utilisé pour le départ et la fin.
    # Pour dimension = 7 on aurait :
    # [[1,1,1,1,1,1,1],
    #  [1,4,1,5,1,6,1],
    #  [1,1,1,1,1,1,1],
    #  [1,7,1,8,1,9,1],
    #  [1,1,1,1,1,1,1],
    #  [1,10,1,11,1,12,1],
    #  [1,1,1,1,1,1,1]]
    nombre_de_case_vide = 4
    for x in range(1, dimension, 2):
        for y in range(1, dimension, 2):
            maze[x][y] = nombre_de_case_vide
            nombre_de_case_vide += 1
    maze = creation_depart_arrivee(dimension, maze)
    maze = suppression_mur(dimension, maze)
    maze = labyrinthe_propre(dimension, maze)
    return maze


# On définit la case départ et celle de fin
# Les cases seront choisi aléatoirement sur les bandes de droite et gauche
# random.randint(0, int((dimension - 3) / 2)) * 2 + 1 permet de définir une case accessible par le futur labyrinthe
# Donc pour dimension = 7 on pourrait avoir un emplacement_entree égale à 1 3 ou 5
# Voici une éventualité de labyrinthe :
# [[1,1,1,1,1,1,1],
#  [2,4,1,5,1,6,1],
#  [1,1,1,1,1,1,1],
#  [1,7,1,8,1,9,3],
#  [1,1,1,1,1,1,1],
#  [1,10,1,11,1,12,1],
#  [1,1,1,1,1,1,1]]
def creation_depart_arrivee(dimension, maze):
    emplacement_entree = random.randint(0, int((dimension - 3) / 2)) * 2 + 1
    # dimension//15 va permettre d'éviter que la sortie soit caché par le chronomètre
    emplacement_sortie = random.randint(0+dimension//15, int((dimension - 3) / 2)) * 2 + 1

    maze[emplacement_entree][0] = 2
    maze[emplacement_sortie][-1] = 3

    return maze


# On va supprimer tous les murs nécessaires afin que tous les points du labyrinthe soient relié pour cela, on
# comparera tous les points avec des abscisses et ordonnées impaires pour vérifier leur égalité.
# Toujours dans notre exemple précédent, on pourrait avoir :
# [[1,1,1,1,1,1,1],
#  [2,9,1,9,8,9,1],
#  [1,7,1,1,1,9,1],
#  [1,9,9,9,9,9,3],
#  [1,7,1,1,1,1,1],
#  [1,9,7,9,9,9,1],
#  [1,1,1,1,1,1,1]]
def suppression_mur(dimension, maze):
    fusion_pas_fini = True
    while fusion_pas_fini:
        same_number = True
        for x in range(1, dimension, 2):
            for y in range(1, dimension, 2):
                if maze[1][1] != maze[x][y]:
                    same_number = False
        if same_number:
            fusion_pas_fini = False
        maze = fusion_aleatoire_mur(dimension, maze)
    return maze


# On fusionne aléatoirement 2 case entre un mur On pourrait avoir ce résultat :
# [[1,1,1,1,1,1,1],
#  [2,4,1,5,1,9,1],
#  [1,1,1,1,1,9,1],
#  [1,7,1,8,1,9,3],
#  [1,1,1,1,1,1,1],
#  [1,10,1,11,1,12,1],
#  [1,1,1,1,1,1,1]]
def fusion_aleatoire_mur(dimension, maze):
    mur_x = random.randint(1, int(dimension - 2))
    # suivant mur_x, on n'aura pas les memes possibilités pour mur_y car on ne peut par exemple supprimer un mur aux
    # coordonnées x=2 y=2, parce qu'il n'y a pas de case numéroté autre que 1 sur ces extrémités donc on doit avoir
    # un mur_x ou mur_y pair et l'autre impair.
    if mur_x % 2 == 0:
        mur_y = random.randint(1, int((dimension - 1) / 2)) * 2 - 1
        # on vérifie qu'ils ne sont pas relié par un chemin
        if maze[mur_y][mur_x - 1] != maze[mur_y][mur_x + 1]:
            # on définit de numéro que l'on utilisera pour remplacer les autres numéros
            besoin_de_remplacer = maze[mur_y][mur_x + 1]
            # on remplace tous les murs d'un côté par la valeur de l'autre
            for x in range(1, dimension, 2):
                for y in range(1, dimension, 2):
                    if maze[x][y] == besoin_de_remplacer:
                        maze[x][y] = maze[mur_y][mur_x - 1]
            # on modifie la valeur du mur afin qu'il ne soit plus égale à 1.
            maze[mur_y][mur_x] = maze[mur_y][mur_x - 1]

    else:
        mur_y = random.randint(1, int((dimension - 3) / 2)) * 2
        if maze[mur_y - 1][mur_x] != maze[mur_y + 1][mur_x]:
            besoin_de_remplacer = maze[mur_y + 1][mur_x]
            for x in range(1, dimension, 2):
                for y in range(1, dimension, 2):
                    if maze[x][y] == besoin_de_remplacer:
                        maze[x][y] = maze[mur_y - 1][mur_x]
            maze[mur_y][mur_x] = maze[mur_y - 1][mur_x]
    return maze


# On remplace tout ce qui n'est pas un 1 2 ou 3 par un chemin (0)
# [[1,1,1,1,1,1,1],
#  [2,0,1,0,0,0,1],
#  [1,0,1,1,1,0,1],
#  [1,0,0,0,0,0,3],
#  [1,0,1,1,1,1,1],
#  [1,0,0,0,0,0,1],
#  [1,1,1,1,1,1,1]]
def labyrinthe_propre(dimension, maze):
    for x in range(1, dimension):
        for y in range(1, dimension):
            if maze[x][y] not in [1, 2, 3]:
                maze[x][y] = 0

    return maze
