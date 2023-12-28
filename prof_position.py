import random


def prof_position(laby, pos_pre, direction):
    # Si la position précédente est l'origine, choisir une position aléatoire dans le labyrinthe
    if pos_pre == [0, 0]:
        pos_x = random.randint(0, int((len(laby) - 3) / 2)) * 2 + 1
        pos_y = random.randint(0, int((len(laby) - 3) / 2)) * 2 + 1
        return [pos_x, pos_y], direction

    # Si la direction est nulle, choisir une direction aléatoire
    if direction == 0:
        direction = random.randint(1, 4)

    # Obtenir les valeurs des cases adjacentes
    haut = laby[pos_pre[1] - 1][pos_pre[0]]
    bas = laby[pos_pre[1] + 1][pos_pre[0]]
    droite = laby[pos_pre[1]][pos_pre[0] + 1]
    gauche = laby[pos_pre[1]][pos_pre[0] - 1]

    # 1: haut, 2: droite, 3: bas, 4: gauche
    direction_possible = []
    if haut == 0:
        direction_possible.append(1)
    if droite == 0:
        direction_possible.append(2)
    if bas == 0:
        direction_possible.append(3)
    if gauche == 0:
        direction_possible.append(4)

    # Coordonnées des cases adjacentes dans l'ordre : haut, droite, bas, gauche
    coordonnees_prochaine_case = [[pos_pre[0], pos_pre[1] - 1],
                                  [pos_pre[0] + 1, pos_pre[1]],
                                  [pos_pre[0], pos_pre[1] + 1],
                                  [pos_pre[0] - 1, pos_pre[1]]]

    # Dictionnaire des directions opposées
    opposite_directions = {1: 3, 2: 4, 3: 1, 4: 2}

    # Si la direction n'est pas nulle et il y a plus d'une direction possible, éliminer la direction opposée
    if len(direction_possible) > 1 and direction != 0:
        opposite_direction = opposite_directions.get(direction, None)
        if opposite_direction in direction_possible:
            direction_possible.remove(opposite_direction)

    # Traiter les différentes situations
    if direction in direction_possible:
        if direction % 2 == 0:
            valid_directions = {1, 3}
        else:
            valid_directions = {2, 4}

        valid_directions.intersection_update(direction_possible)
        if valid_directions:
            # Choisir une nouvelle direction valide aléatoire parmi les directions possibles
            new_direction = random.choice(list(valid_directions))
            return coordonnees_prochaine_case[new_direction - 1], new_direction
        else:
            # Continuer dans la direction actuelle
            return coordonnees_prochaine_case[direction - 1], direction
    else:
        # Choisir une nouvelle direction parmi les directions possibles
        new_direction = random.choice(direction_possible)
        return coordonnees_prochaine_case[new_direction - 1], new_direction
