import numpy as np
import pygame

from Message_niveau import message_niveau
from niveau import niveaux
from gestion_affichage_labyrinthe import gestion_affichage_laby
from prof_position import prof_position

# Initialisation de Pygame
pygame.init()

# Chargement du premier niveau
laby = niveaux(1)
niveaux_actuel = 0

# Paramètres de la fenêtre de jeu
largeur, hauteur = 700, 700
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Labyrinthe")
fps = 60  # Fréquence de rafraîchissement de l'écran

# Chargement des images pour les différents éléments du jeu
mur = pygame.image.load("img/element_labyrinthe/mur_labyrinthe.svg")
point_arrivee = pygame.image.load("img/element_labyrinthe/PORTE.svg")
point_depart = pygame.image.load("img/element_labyrinthe/start.svg")
fond_gris = pygame.image.load("img/fondGris.svg")
img_accueil = pygame.image.load("img/EscEpsi.png")
img_aide = pygame.image.load("img/aide.png")
fond_entre_niv = pygame.image.load("img/fondEntrePage.png")
joueur_hugo = pygame.image.load("img/player/hugo.svg")
joueur_anais = pygame.image.load("img/player/anais.svg")
prof_img = pygame.image.load("img/prof_img.svg")
# Choix par défaut du joueur
joueur_img = joueur_anais

# Dimensionne l'image en fonction de la taille de la fenêtre et du nombre de lignes/colonnes
fond_gris = pygame.transform.scale(fond_gris, (largeur, hauteur))
img_accueil = pygame.transform.scale(img_accueil, (largeur, hauteur))
img_aide = pygame.transform.scale(img_aide, (largeur, hauteur))
fond_entre_niv = pygame.transform.scale(fond_entre_niv, (largeur, hauteur))
joueur_hugo = pygame.transform.scale(joueur_hugo, (largeur / 3, hauteur / 3))
joueur_anais = pygame.transform.scale(joueur_anais, (largeur / 3, hauteur / 3))

# Affichage de la structure du labyrinthe dans la console
for ligne in laby:
    print(ligne)

# Initialisation de variables pour la gestion du temps et de l'affichage
temps_ecoule = 0
horloge = pygame.time.Clock()
police = pygame.font.Font(None, 36)

# Variables pour le contrôle du flux du jeu
win = False
afficher_menu = True
aide = False
avancement = 0
demarage_chronometre = True
selection_joueur = False
pre_pos_prof = [0, 0]
direction_prof = 0
img_passe = 0
loose = False

# Couleurs utilisées dans le jeu
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Conversion de la liste du labyrinthe en matrice NumPy pour une manipulation aisée
matrice_laby = np.array(laby)

# Détermination de la position initiale du joueur
position_player_indices = np.where(matrice_laby == 2)
next_position = position_player_indices
position_x = position_player_indices[1][0]  # Coordonnée horizontale
position_y = position_player_indices[0][0]  # Coordonnée vertical

# Début de la boucle principale du jeu
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        # Gestion des événements (fermeture de la fenêtre, touches pressées, etc.)
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # action réalisable uniquement dans le labyrinthe
            if not win and avancement % 10 == 0 and avancement != 0:
                # HAUT
                if event.key == pygame.K_UP:
                    next_position = [position_player_indices[0][0] - 1, position_player_indices[1][0]]
                    # Vérifiez si la case suivante n'est pas un mur (valeur égale à 1 dans la matrice)
                    if matrice_laby[next_position[0]][next_position[1]] != 1:
                        position_player_indices[0][0] -= 1  # Maj la position uniquement si on peut monter

                # BAS
                if event.key == pygame.K_DOWN:
                    next_position = [position_player_indices[0][0] + 1, position_player_indices[1][0]]
                    # Vérifiez si la case suivante n'est pas un mur (valeur égale à 1 dans la matrice)
                    if matrice_laby[next_position[0]][next_position[1]] != 1:
                        position_player_indices[0][0] += 1  # Maj la position uniquement si on peut descendre

                # DROITE
                if event.key == pygame.K_RIGHT:
                    # position suivante vaut + 1 à droite
                    next_position = [position_player_indices[0][0], position_player_indices[1][0] + 1]

                    # si dans la matrice il y a un 0 dans la prochaine case
                    if matrice_laby[next_position[0]][next_position[1]] != 1:
                        # position joueur augmente de 1 vers la droite
                        position_player_indices[1][0] += 1  # Maj la position seulement si on peut avancer

                # GAUCHE
                if event.key == pygame.K_LEFT:
                    next_position = [position_player_indices[0][0], position_player_indices[1][0] - 1]
                    if matrice_laby[next_position[0]][next_position[1]] != 1:
                        position_player_indices[1][0] -= 1  # Maj la position seulement si on peut avancer

            # action se passant uniquement quand on est dans le menu
            elif avancement == 0:
                # choisir un joueur
                if event.key == pygame.K_p:
                    fenetre.fill(NOIR)
                    fenetre.blit(mur, (0, 0))
                    selection_joueur = not selection_joueur
                if event.key == pygame.K_h:
                    fenetre.fill(NOIR)
                    fenetre.blit(mur, (0, 0))
                    aide = not aide
                if selection_joueur:
                    if event.key == pygame.K_a:
                        joueur_img = joueur_anais
                        selection_joueur = False
                    if event.key == pygame.K_h:
                        joueur_img = joueur_hugo
                        selection_joueur = False
            if win or afficher_menu or avancement % 10 != 0 or loose:
                if event.key == pygame.K_n:
                    print("avancement :", avancement)
                    if avancement == 0:
                        avancement += 1
                    elif avancement == 1:
                        avancement += 1
                    elif avancement == 2:
                        avancement = 10
                    elif avancement == 10:
                        laby = niveaux(2)
                        avancement += 1
                    elif avancement == 11:
                        avancement = 20
                    elif avancement == 20:
                        avancement += 1
                        laby = niveaux(3)
                    elif avancement == 21:
                        avancement += 1
                    elif avancement == 22:
                        avancement = 30
                    elif avancement == 30:
                        laby = niveaux(4)
                        avancement += 1
                    elif avancement == 31:
                        avancement = 40
                    elif avancement == 40:
                        avancement = 41
                    elif avancement == 41:
                        loose = True
                    if loose:
                        laby = niveaux(1)
                        avancement = 0
                        afficher_menu = True
                        loose = False
                        mur = pygame.image.load("img/element_labyrinthe/mur_labyrinthe.svg")
                        point_arrivee = pygame.image.load("img/element_labyrinthe/PORTE.svg")
                        point_depart = pygame.image.load("img/element_labyrinthe/start.svg")
                        joueur_hugo = pygame.image.load("img/player/hugo.svg")
                        joueur_anais = pygame.image.load("img/player/anais.svg")
                        prof_img = pygame.image.load("img/prof_img.svg")
                        joueur_img = joueur_anais
                        temps_ecoule = 0
                    else:
                        win = False
                        afficher_menu = False

                        largeur_cellule = largeur // len(laby[0])
                        hauteur_cellule = hauteur // len(laby)

                        matrice_laby = np.array(laby)

                        # Trouver les indices où la valeur est égale à 2 (case de départ)
                        position_player_indices = np.where(matrice_laby == 2)

                        next_position = position_player_indices

                        # Extraire les valeurs des tableaux numpy

                        position_x = position_player_indices[1][0]  # horzontal
                        position_y = position_player_indices[0][0]  # verticale
                    if avancement % 10 == 1 and avancement != 0:
                        # permet de redimensionner les cases en fonctions de la nouvelle dimension du labyrinthe
                        mur, point_arrivee, point_depart, joueur_img, prof_img = gestion_affichage_laby(laby, largeur,
                                                                                                        hauteur, mur,
                                                                                                        point_arrivee,
                                                                                                        point_depart,
                                                                                                        joueur_img,
                                                                                                        prof_img)

            if event.key == pygame.K_q:
                done = True
    #  Mise à jour de l'affichage selon l'état du jeu (menu, jeu en cours, etc.)
    fenetre.fill(BLANC)
    # si on se trouve au menu
    if avancement == 0:
        if selection_joueur:
            fenetre.blit(joueur_hugo, (0, 0))
            fenetre.blit(joueur_anais, (200, 0))
        elif aide:
            fenetre.blit(img_aide, (0, 0))

        else:
            fenetre.blit(img_accueil, (0, 0))
    # si on se trouve dans une page de contexte
    elif avancement % 10 != 0:
        fenetre.blit(fond_entre_niv, (0, 0))
        message_afficher = message_niveau(avancement).split("_n")
        y = hauteur / 2 - len(message_afficher) / 2 * 40  # Position verticale initiale
        for ligne in message_afficher:
            texte_surface = police.render(ligne, True, BLANC)
            fenetre.blit(texte_surface, (70, y))
            y += 40
        texte_touche = "appuyer sur \"n\""

        texte_touche = police.render(texte_touche, True, BLANC)
        fenetre.blit(texte_touche, (largeur - 200, hauteur - 40))
    # si on se trouve dans un niveau
    elif (avancement % 10) == 0:

        # Dessiner le labyrinthe
        for i in range(len(laby)):
            for j in range(len(laby[0])):
                if laby[i][j] == 1:
                    fenetre.blit(mur, (j * largeur_cellule, i * hauteur_cellule))
                elif laby[i][j] == 2:
                    fenetre.blit(point_depart, (j * largeur_cellule, i * hauteur_cellule))
                elif laby[i][j] == 3:
                    fenetre.blit(point_arrivee, (j * largeur_cellule, i * hauteur_cellule))

        # Dessiner le joueur à sa nouvelle position
        fenetre.blit(joueur_img, (
            position_player_indices[1][0] * largeur_cellule, position_player_indices[0][0] * hauteur_cellule,
            largeur_cellule, hauteur_cellule))
        if len(laby) > 20:
            if img_passe == 0:
                pre_pos_prof, direction_prof = prof_position(laby, pre_pos_prof, direction_prof)
                img_passe += 1
            else:
                img_passe += 1
                if img_passe == 10:
                    img_passe = 0
            fenetre.blit(prof_img, (
                pre_pos_prof[0] * largeur_cellule, pre_pos_prof[1] * hauteur_cellule, largeur_cellule, hauteur_cellule))
        if not win:
            if demarage_chronometre:
                horloge.tick(60)
                demarage_chronometre = False
            temps_ecoule += horloge.tick(fps)

            if [pre_pos_prof[0], pre_pos_prof[1]] == [position_player_indices[1][0],
                                                      position_player_indices[0][0]] or temps_ecoule > 80000:
                loose = True
                horloge.tick(fps)
                police_win = pygame.font.Font(None, 50)
        if loose:
            demarage_chronometre = True
            temps_ecoule = 0
            fenetre.blit(fond_gris, (0, 0))
            # Message arrivé
            temps_texte_ligne1 = police_win.render("Vous avez perdu vous y était presque ! ", True, NOIR, BLANC)

            # Deuxième ligne du texte arrivée
            temps_texte_ligne2 = police_win.render("Retentez votre chance !", True, NOIR, BLANC)
            largeur_texte_1 = temps_texte_ligne1.get_rect()[2]
            hauteur_texte_1 = temps_texte_ligne1.get_rect()[3]

            largeur_texte_2 = temps_texte_ligne2.get_rect()[2]
            hauteur_texte_2 = temps_texte_ligne2.get_rect()[3]

            pygame.draw.rect(fenetre, BLANC, (
                largeur / 2 - largeur_texte_1 / 2 - 20, hauteur / 2 - hauteur_texte_1 - 20, largeur_texte_1 + 40,
                hauteur_texte_1 + hauteur_texte_2 + 40))

            fenetre.blit(temps_texte_ligne1, (largeur / 2 - largeur_texte_1 / 2, hauteur / 2 - hauteur_texte_1))
            fenetre.blit(temps_texte_ligne2, (largeur / 2 - largeur_texte_2 / 2, hauteur / 2))

        temps_texte = police.render("{:.2f} sec".format(temps_ecoule / 1000), True, NOIR, BLANC)
        fenetre.blit(temps_texte, (largeur - 100, 20))

        # Le joueur est arrivé à la porte
        if matrice_laby[position_player_indices[0][0], position_player_indices[1][0]] == 3:
            if not win:
                win = True
                horloge.tick(fps)
                demarage_chronometre = True
                police_win = pygame.font.Font(None, 50)

            fenetre.blit(fond_gris, (0, 0))
            # Message arrivé
            temps_texte_ligne1 = police_win.render("Vous avez fini le niveau en :", True, NOIR, BLANC)

            # Deuxième ligne du texte arrivée
            temps_texte_ligne2 = police_win.render("{:.2f} secondes !!!".format(temps_ecoule / 1000), True, NOIR, BLANC)
            largeur_texte_1 = temps_texte_ligne1.get_rect()[2]
            hauteur_texte_1 = temps_texte_ligne1.get_rect()[3]

            largeur_texte_2 = temps_texte_ligne2.get_rect()[2]
            hauteur_texte_2 = temps_texte_ligne2.get_rect()[3]

            pygame.draw.rect(fenetre, BLANC, (
                largeur / 2 - largeur_texte_1 / 2 - 20, hauteur / 2 - hauteur_texte_1 - 20, largeur_texte_1 + 40,
                hauteur_texte_1 + hauteur_texte_2 + 40))

            fenetre.blit(temps_texte_ligne1, (largeur / 2 - largeur_texte_1 / 2, hauteur / 2 - hauteur_texte_1))
            fenetre.blit(temps_texte_ligne2, (largeur / 2 - largeur_texte_2 / 2, hauteur / 2))

    # Actualisation de la fenêtre de jeu
    pygame.display.flip()
    # Contrôle de la fréquence de rafraîchissement
    clock.tick(fps)

pygame.quit()
