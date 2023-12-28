# Escepsi

Ce programme Python est un jeu de labyrinthe simple réalisé avec la bibliothèque Pygame. L'objectif du jeu est de s'échapper du labyrinthe avant le temps imparti, en évitant les obstacles.

## Prérequis

- Python 3.x
- vérifier que cous étes dans le bon répertoire
  ```
    cd labyrinthe
  ```
- Pygame (installé via `pip install pygame`)
- Numpy (installé via `pip install numpy`)

## Lancement du jeu

`python escepsi.py`

## Contrôles

- Utilisez les flèches directionnelles (Haut, Bas, Gauche, Droite) pour déplacer le joueur dans le labyrinthe.
- Appuyez sur la touche "p" pour choisir entre deux joueurs (disponible uniquement dans le menu).
- Appuyez sur la touche "n" pour passer au niveau suivant.
- Appuyez sur la touche "q" pour quitter le jeu.
- Appuyez sur la touche "h" pour rentrer dans le menu d'aide.

## Fonctionnement du jeu
- Le joueur commence à partir du point de départ et doit atteindre la porte de sortie pour terminer un niveau.
- Le professeur patrouille dans le labyrinthe et peut entraîner la défaite du joueur s'ils se croisent.
- Le joueur peut choisir son personnage en appuyant sur la touche "p" au début du jeu.
- Le jeu affiche des messages d'aide et d'instructions tout au long du parcours.
- Le chronomètre mesure le temps mis par le joueur pour terminer un niveau.
- Si le joueur termine un niveau, le temps écoulé est affiché. En cas d'échec, un message de défaite est affiché.

Amusez-vous bien en explorant les labyrinthes et en essayant de gagner !

## Créateur du jeu :

- BOISSON Anaïs
- DEPOUMPS Hugo