# Convertir un fichier image PNG au format JPG
# Source : revue Coding, n°18, p.31
# pip install Pillow

import tkinter as tk
from tkinter import filedialog
from PIL import Image


# initialisation de la fenêtre
fenetre = tk.Tk()
# création d'un canvas
canvas = tk.Canvas(fenetre, width=300, height=250, bg='yellow', relief='raised')
canvas.pack()
# titre
label = tk.Label(fenetre, text="Convertisseur d'images", bg="yellow")
label.config(font=("helvetica", 20))
canvas.create_window(150, 60, window=label)

# ouvrir l'image à convertir
def getPNG():
    global mon_image
    import_file_path = filedialog.askopenfilename()
    mon_image = Image.open(import_file_path)


# Bouton pour choisir l'image
browse_png = tk.Button(text="Choix du fichier PNG", command=getPNG, bg="royalblue", fg="white", font=("helvetica", 12, "bold"))
canvas.create_window(150, 130, window=browse_png)

# fonction pour convertir l'image
def convert():
    global mon_image
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    mon_image.save(export_file_path)

# Bouton pour lancer la conversion
bouton_conversion = tk.Button(text="Conversion PNG vers JPG", command=convert, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas.create_window(150, 180, window=bouton_conversion)

# lancer la fenêtre
fenetre.mainloop()
