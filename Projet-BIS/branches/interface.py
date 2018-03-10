from tkinter import *
#from tkinter import ttk
#from PIL import Image, ImageTk
from main_pygame import *
#from pre_settings.Settings import *


#from PIL import Image, ImageTK

global couleurPrincipale
couleurPrincipale = "#E6DCBF"


class App:#Class de type App qui gère la fenêtre graphique de base.
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.config(bg=couleurPrincipale)
        self.frame.pack()

        self.jouer_button = Button(self.frame, text="Jouer", fg="#000000",#
        relief=RAISED, compound=CENTER,
        width=25, height=5, bg=couleurPrincipale,
        command=self.lancerPartie).pack()#Ajout d'un boutton pour lancer le jeux et quitter la fenêtre.

        self.settings_button = Button(self.frame, text="Paramètres", fg="#000000",
        relief=RAISED, compound=CENTER,
        width=25, height=5, bg=couleurPrincipale,
        command=self.settings).pack()#Ajout d'un boutton pour l'accès aux paramètres.

        self.quitter_button = Button(self.frame, text="Quitter", fg="#000000",
        relief=RAISED, compound=CENTER, bg=couleurPrincipale,
        width=25, height=5, command=self.quitterPartie).pack()#Ajout d'un boutton pour quitter la fenêtre.


    def lancerPartie(self):#Fonction lancerPartie qui va quitter la fenêtre puis lancer le jeu.
        self.master.destroy()
        self.master.quit()
        Jeux(900,800)

    def settings(self):#Fonction qui donneras accès aux paramètres du joueur.
        windows = Toplevel(self.master, bg=couleurPrincipale)
        windows.minsize(width=500, height=400)
        #lecture()#Problème avec la lecture du fichier.
        windows.settings_label = Label(windows, text="Accès aux paramètres", fg="#F73F0B", bg=couleurPrincipale, font=(18)).pack()
        #self.frame.destroy()

    def quitterPartie(self):#Fonction qui quitte la fenêtre.
        self.master.destroy()



root = Tk()



root.title("Le jeu trop bien !!!")
root.geometry("500x400")#Fenètre de 500 par 400

app = App(root)
app.frame.quit
root.mainloop()#Boucle principal
