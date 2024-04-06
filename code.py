import tkinter as tk
from tkinter import messagebox
import random
from tkinter import font

global liste_nombre
global seconds

def est_triee(liste):
    # liste.remove(0)
    n = len(liste)
    for i in range(n - 2):
        if liste[i] > liste[i + 1]:
            return False
    return True

def update_button_text():
    seconds += 1
    button.config(text=f"{seconds} Sec")
    root.after(1000, update_button_text)  # Planifie la prochaine mise à jour dans 1 seconde



def on_button_click(element, button):
    # Action à effectuer lors du clic sur le bouton
    indice = liste_nombre.index(element)
    button.destroy()
    try:
        if liste_nombre[indice-1] == 0:
            liste_nombre[indice-1] = element
            liste_nombre[indice] = 0
            affichage()
        elif liste_nombre[indice-5] == 0:
            liste_nombre[indice-5] = element
            liste_nombre[indice] = 0
            affichage()
        elif liste_nombre[indice+1] == 0:
            liste_nombre[indice+1] = element
            liste_nombre[indice] = 0
            affichage()
        elif liste_nombre[indice+5] == 0:
            liste_nombre[indice+5] = element
            liste_nombre[indice] = 0
            affichage()
    except:
        pass
    
    if est_triee(liste_nombre):
        messagebox.showinfo("Match terminé", f"Vous avez gagné la partie après {seconds}")
        random.shuffle(liste_nombre)
        seconds = 0.

def affichage():
    for i in liste_nombre:
        mod = liste_nombre.index(i)%5
        div = liste_nombre.index(i)//5
        bold_font = font.Font(weight="bold")
        if i == 0:
            button = tk.Button(root, text=i, width=4, height=2, command=lambda text=i: on_button_click(text, button), bg="blue", fg="blue", font=bold_font)
        else:
            button = tk.Button(root, text=i, width=4, height=2, command=lambda text=i: on_button_click(text, button), bg="white", fg="blue", font=bold_font)
        button.place(x=mod*50, y=div*50)

        
# Création de la fenêtre principale
root = tk.Tk()
root.title("Formulaire")

# Définition de la taille du formulaire
root.geometry("250x290")  # Largeur x Hauteur

# Initialisation d'une liste contenant 25 nombres allant de 0 à 24
liste_nombre = [i for i in range(25)]

# Trie aléatoire de la liste pour le jeu
random.shuffle(liste_nombre)

# Affichage les buttons sur le formulaire
affichage()

seconds = 0
bold_font = font.Font(weight="bold")
button = tk.Button(root, text=f"{seconds} Sec", width=6, height=2, bg="blue", fg="White", font=bold_font)
button.place(x=100, y=252)

# Démarrage de la mise à jour périodique
root.after(1000, update_button_text)
# Lancement de la boucle principale
root.mainloop()
