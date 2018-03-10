import json
import pygame
#####LE CHANGER EN JSON FILE, Utilisation plus simple
class Settings:
    def __init__(self):
        self.path = "JSON_File/Settings.json"#Par rapport a main_pygame.py

        self._default_dict_ = {u"up":"up",u"down":"down",u"right":"right",u"left":"left",u"s_shoot":"space",u"score":{},u"language":"Francais",u"Width":900,u"Height":900, u"fps":60}

        self._dict_ = self._default_dict_

        self.file = None

        self.file_here = None

        self.key_hold = None

    def read(self):#Fonction qui va faire une lecture du file pour en extraire des informations.
        try:    
            self.load_json_to_dict()
            self.file_here = True
        except:
            self.default_save()
            self.file_here = False

    def default_save(self):
        self.save_settings(self._default_dict_)
        self.load_json_to_dict()

    def load_json_to_dict(self):
        tmp = {}

        with open(self.path) as self.file:#On récupère le fichier
            self._dict_ = json.load(self.file)

        if len(self._dict_) < len(self._default_dict_):#Si l'on a rajouté un paramètre
            for i in self._dict_:#On récupere les différences dans un dictionnaire temporaire
                if self._dict_[i] != self._default_dict_[i]:
                    tmp[i] = self._dict_
            self._dict_ = self._default_dict_#On remet le dictionnaire que l'on utilise par default

            for i in tmp:#Enfin, on remet les paramètres personnalisé de l'utilisateur
                self._dict_[i] = tmp[i]
            self.save_settings(self._dict_)#Pour finir, on sauvegarde

    def get_key(self):
        get = True
        while get:
            #On récupere les touches de la même manière que pour déplacer notre vaisseau
            pressed = pygame.key.get_pressed() # already familiar with that
            buttons = [pygame.key.name(k) for k,v in enumerate(pressed) if v]
            for i in buttons:
                if i != "numlock" and i != "caps lock" and i != "escape":
                    self.key_hold = i
                    #print("KEY = " + self.key_hold)
                    get = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
                        get = False

    def change_settings(self, key):

        if self.key_hold != None:
            for i in self._dict_:
                if self._dict_[i] == self.key_hold:
                    self._dict_[i] = "No assignement"
                    #print(i + "No longer Assign")
            self._dict_[key] = self.key_hold

        #if "n'appuie pas sur le bouton save":
            #self.load_json_to_dict() #On remet les paramètres d'avant
        #else:
            #self.save_settings(self.__dict__)

    def save_settings(self,__dict__):
        with open(self.path, "w") as self.file:
            json.dump(__dict__, self.file, sort_keys=True, indent=4) 


#    Settings = Settings()
#   print(Settings._dict_)
#    Settings.read()
#    print(Settings._dict_["up"])
#    print(Settings._dict_)
#    Settings.default_save()
#    print(Settings._dict_["up"])
#    print(Settings._dict_)

