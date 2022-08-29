# Application horloge numérique (Python, Tkinter)

import tkinter, tk
import time

# titre/taille de la fenêtre
fenetre = Tk()
fenetre.title("Horloge numérique avec Python")
fenetre.geometry("480x200")
# fonction redimensionnable (pour une fenêtre fixe = True(1,1))
fenetre.resizable(1,1)

# police d'écriture
text_font = ("Noto Serif", 80, 'bold')
# Autre exemple de police : System, Modern, Script, Consolas, Rubik, Agency FB...
# couleur arrière-plan
background = "#000000"
# couleur police
foreground = "#f8f8ff"
# largeur de bordure
border_width = 30 

# Label de l'application
label = Label(fenetre, font=text_font, bg=background, fg=foreground, bd=border_width)
# ajout d'une grille
label.grid(row=0, column=1)


# fonction principale :
def horloge_numerique():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, horloge_numerique)

# Lancement de l'application
horloge_numerique()
fenetre.mainloop()