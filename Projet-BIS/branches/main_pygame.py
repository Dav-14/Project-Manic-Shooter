try:
    import os
    import sys
    import time
    import pygame
    import json
    from pygame.locals import *

    import pre_settings.Settings as Settings
    import Entity.Reactor as Rct
    import Entity.EntityGroup as ENTGroup
    import Entity.SpaceShip as spaceShip
    import Entity.Ally as Ally
    import Entity.Bullet as Blt
except ImportError as error:
    print(error.__class__.__name__ + " : " + error.msg)
    sys.exit(0)



def Jeux(Hht, Wth):
    Set = Settings.Settings()
    Set.read()

    Height, Width = Hht, Wth
    if Set.file_here:
        Height = Set._dict_["Height"] #Hauteur
        Width = Set._dict_["Width"] #Largeur
    fps = Set._dict_["fps"]

    pygame.init()
    print("DRIVER :",pygame.display.get_driver())
    input()
    Window = pygame.display.set_mode((Width,Height))
    pygame.display.set_caption("Manic Shooter : Shot'em up !")
    Background = pygame.image.load(os.path.join("..","Ressources","Background","Background.jpg")).convert()
    Background = pygame.transform.scale(Background, (Width,Height))#Charge l'image

    ###################################
    #def waves(dictEnnemis, nb=5):#Valeur 5 ennemies de bases, on peut la changer en donnant nb=nombre en arguments
    #    for i in range(nb):
    #        print("i=",i)
    #        ennemi = mEnnemis.ennemis()
    #        ennemi.ajoutEnnemis(dictEnnemis, maGrille)
    #        dictEnnemis[i] = ennemi
    #    return dictEnnemis
    ###################################
    # Initialisation de la première vague d'énnemie

    def load_json_to_dict(path):
        with open(path) as file:#On récupère le fichier
            _dict_ = json.load(file)
        return _dict_
    
    _dict_Bullet_type = load_json_to_dict("JSON_File/Bullet_type.json")
    _dict_Patern = load_json_to_dict("JSON_File/Patern.json")

    ### Charge un dictionnaire de données sur les differentes "Balles" ###
    #lFile_path = ['Entity/Bullet/Bullet_type.json', 'Patern.json']

    __GroupBullet_Ennemy = ENTGroup.Entity()
    __GroupEnnemy = ENTGroup.Entity()
    __GroupBullet_Ally = ENTGroup.Entity()

    Spaceship = Ally.allyShip()
    Spaceship.Reactor_innit()
    Spaceship.bullet_type = "double"

    continuer = True
    while continuer:
        Window.blit(Background, (0,0))

        pressed = pygame.key.get_pressed()
        buttons = {pygame.key.name(k) for k,v in enumerate(pressed) if v}#Recupère le nom des touches PRESSE
        #print(buttons)
        if Set._dict_["up"] in buttons:
            Spaceship.up()
        if Set._dict_["down"] in buttons:
            Spaceship.down()
        if Set._dict_["left"] in buttons:
            Spaceship.left()
        if Set._dict_["right"] in buttons:
            Spaceship.right()
        if Set._dict_["s_shoot"] in buttons:
            now = pygame.time.get_ticks()
            if now - Spaceship.bullet_last_hit >= _dict_Bullet_type["typ_bullet"][Spaceship.bullet_type]["Cooldown"]:
                for i in range(_dict_Bullet_type["typ_bullet"][Spaceship.bullet_type]["n"]):
                    Bullet = Blt.bullet(Spaceship, _dict_Bullet_type, i)
                    __GroupBullet_Ally.add(Bullet)
                Spaceship.bullet_last_hit = now
        if 'escape' in buttons:
            pass
            #Set.get_key()
            #Set.change_settings("up")
            #Set.save_settings(Set._dict_)
            #print(Set._dict_["up"])
        if 'f' in buttons and 'i' in buttons and 'n' in buttons:
            continuer = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
                continuer = False
        #__followPos() A ajouter pour reactualisé les positions de nos objets
        ############################
        ############################
        #__Draw() A ajouter pour tout les BLITs
        ############################
        # 
        #Window.blit(Spaceship.Reactor.reactor_style, (Spaceship.Reactor.reactor_posX, Spaceship.Reactor.reactor_posY))#Affiche le reacteur du vaisseau
        Window.blit(Spaceship.image, (Spaceship.posX, Spaceship.posY))

        #print(__GroupBullet_Ally)
        __GroupBullet_Ally.update(_dict_Bullet_type)
        __GroupBullet_Ally.draw(Window)
        #__GroupEnnemy.__Draw()  Cette fonction devrais affiché normalement TOUT les énemies qui sont dans le groupe de SPRITE
        #Affiche le vaisseau
        ############################
        pygame.display.update()
        pygame.time.Clock().tick(fps)
    pygame.quit()
    quit()

