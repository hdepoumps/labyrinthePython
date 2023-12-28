from generateur_labyrinthe import generateur_laby


# séléction des niveaux, on notera que les niveaux apres le 1 sont généré aléatoirement !!!
def niveaux(lvl):
    if lvl == 1:
        laby = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [2, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                [1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 3, 1]]

    elif lvl == 2:
        laby = generateur_laby(17)
    elif lvl == 3:
        laby = generateur_laby(25)
    elif lvl == 4:
        laby = generateur_laby(35)

    return laby
