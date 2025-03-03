import tkinter as tk
import random as Ashkan

racine = tk.Tk()
racine.title('Mon dessin')

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

# les fonctions

color = "yellow"

def circle():
    x0 = Ashkan.randint(0, CANVAS_WIDTH - 100)
    y0 = Ashkan.randint(0, CANVAS_HEIGHT - 100)
    x1 = x0 + 100
    y1 = y0 + 100
    canevas.create_oval(x0, y0, x1, y1, outline=color)

def square():
    x0 = Ashkan.randint(0, CANVAS_WIDTH - 100)
    y0 = Ashkan.randint(0, CANVAS_HEIGHT - 100)
    x1 = x0 + 100
    y1 = y0 + 100
    canevas.create_rectangle(x0, y0, x1, y1, outline=color)

def cross():
    x0 = Ashkan.randint(0, CANVAS_WIDTH - 80)
    y0 = Ashkan.randint(0, CANVAS_HEIGHT - 80)
    x1 = x0 + 80
    y1 = y0 + 80
    canevas.create_line(x0, y0, x1, y1, fill=color)
    canevas.create_line(x0+80, y0, x1-80, y1, fill=color)

def choose_color():
    global color
    color = input('choisir une couleur')

# le canevas


# colonne 1
cercle = tk.Button(racine, text="Cercle", command=circle)
carre = tk.Button(racine, text="Carré", command=square)
croix = tk.Button(racine, text="Croix", command=cross)

# colonne 2
choose = tk.Button(racine, text="Choisir une couleur", command=choose_color)
canevas = tk.Canvas(racine, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, background="black", highlightthickness=7, highlightbackground="red")

# on place
cercle.grid(row=1, column=0)
carre.grid(row=2, column=0)
croix.grid(row=3, column=0)

choose.grid(row=0, column=1)
canevas.grid(row=1, column=1, rowspan=3)

racine.mainloop()