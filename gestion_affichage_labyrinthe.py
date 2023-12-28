import pygame


def gestion_affichage_laby(laby, largeur_fenetre, hauteur_fenetre, wall, finish_point, start_point, joueur_img, prof_img):
    
    # definition de la taille d'une cellule en fonction de la fenêtre
    largeur_cellule = largeur_fenetre // len(laby[0])
    hauteur_cellule = hauteur_fenetre // len(laby)

    # adaptation de la taille de chaque image a la taille d'une cellule
    wall = pygame.transform.scale(wall, (largeur_cellule, hauteur_cellule))
    finish_point = pygame.transform.scale(finish_point, (largeur_cellule, hauteur_cellule))
    start_point = pygame.transform.scale(start_point, (largeur_cellule, hauteur_cellule))
    joueur_img = pygame.transform.scale(joueur_img, (largeur_cellule, hauteur_cellule))
    prof_img = pygame.transform.scale(prof_img, (largeur_cellule, hauteur_cellule))

    return wall, finish_point, start_point, joueur_img, prof_img
