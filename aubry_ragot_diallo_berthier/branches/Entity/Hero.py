import pygame

class hero:

    def __init__(self, mv_cooldown = None):
        if mv_cooldown == None:
            self.mv_cooldown = 200
        else:
            self.mv_cooldown = mv_cooldown
        #Constructeur

        now = pygame.time.get_ticks()
        #############################
        #Pour faire des mouvements alterné
        self.last_move_top = now#Gere les déplacement tous les X cooldowns
        self.last_move_bottom = now
        self.last_move_left = now
        self.last_move_right = now#On est obligé de creer 4 variables si l'on veut faire des mouvements
        #############################

        self.posX = 0#Position en X du héro.
        self.posY = 0#Position en Y du héro.
        self.c_Hero = "1"#Un hero vaut le chiffre 1.

    def ajoutHero(self, maGrille): #Permet l'ajout du héro.

        self.posY = maGrille.ligne - 1 #On obtient les coordonnees Y
        self.posX = int(maGrille.colonne/2) #On obtient les coordonnees X du hero.
        maGrille.grid[self.posY][self.posX] = self.c_Hero # ajout du hero dans le centre de la liste


    def haut(self, maGrille):#Permet de faire déplacer le héro vers la gauche.
        now = pygame.time.get_ticks()
        if (self.posY - 1 >= 0) and (now - self.last_move_top >= self.mv_cooldown):
            self.last_move_top = pygame.time.get_ticks() #Vérifie que la position ne depasse pas la grille en haut.
            self.last_move = pygame.time.get_ticks()
            maGrille.grid[self.posY][self.posX] = "-"#Remplace la position precedente
            self.posY -= 1#Lui donne une nouvelle direction
            maGrille.grid[self.posY][self.posX] = self.c_Hero#Applique la direction

    def bas(self, maGrille):#Permet de faire se déplacer le héro sur la droite.
        now = pygame.time.get_ticks()
        if (self.posY + 1 < maGrille.ligne) and (now - self.last_move_bottom >= self.mv_cooldown):
            self.last_move_bottom = pygame.time.get_ticks()#Vérifie que la position ne dépasse pas la grille en bas.
            maGrille.grid[self.posY][self.posX] = "-"#Remplace la position precedente
            self.posY += 1#Lui donne une nouvelle direction
            maGrille.grid[self.posY][self.posX] = self.c_Hero#Applique la direction

    def gauche(self, maGrille):
        now = pygame.time.get_ticks()
        if self.posX - 1 >= 0 and (now - self.last_move_left >= self.mv_cooldown):
            self.last_move_left = pygame.time.get_ticks() #On vérifie que la position future ne depasse pas la grille a gauche
            maGrille.grid[self.posY][self.posX] = "-"
            self.posX -= 1 #On change sa position
            maGrille.grid[self.posY][self.posX] = self.c_Hero #On "ecrit" sa positons dans la grille

    def droite(self, maGrille):
        now = pygame.time.get_ticks()
        if self.posX + 1 < maGrille.colonne and (now - self.last_move_right >= self.mv_cooldown):
            self.last_move_right = pygame.time.get_ticks()
            c_Hero = "1"#On vérifie que la position future ne depasse pas la grille a droite
            maGrille.grid[self.posY][self.posX] = "-"
            self.posX += 1#On change sa position
            maGrille.grid[self.posY][self.posX] = c_Hero#On "ecrit" sa positons dans la grille
