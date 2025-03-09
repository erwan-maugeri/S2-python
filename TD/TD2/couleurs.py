# ERWAN MAUGERI LDDMP
import tkinter as tk
import random as Ashkan

#fenetre
racine = tk.Tk()
racine.title("couleurs")

#canvas
canvas = tk.Canvas(racine, bg="black", height=256, width=256, highlightthickness=0)
canvas.grid(rowspan=4, row=0, column=1)

#focntions
def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    x0 = i
    y0 = j
    x1 = i+1
    y1 = j+1
    canvas.create_rectangle(x0, y0, x1, y1, width=0, fill=color)

def degrade_gris():
    for j in range(0,256):
        for i in range(0,256):
            draw_pixel(i, j, get_color(*[i]*3))

def ecran_aleatoire():
    for j in range(0,256):
        for i in range(0,256):
            draw_pixel(i, j, get_color(*[Ashkan.randint(0,255)]*3))

def degrade_2D():
    for i in range(0,256):
            for j in range(0,256):
                draw_pixel(i, j, get_color(255-j, 0, i))
                draw_pixel(j, i, get_color(255-i, 0, j))

def empty():
    canvas.delete("all")
    print('Canevas vidé')

#boutons
tk.Button(racine, text='Aléatoire', command=ecran_aleatoire).grid(row=0, column=0)
tk.Button(racine, text='Dégradé gris', command=degrade_gris).grid(row=1, column=0)
tk.Button(racine, text='Dégradé 2D', command=degrade_2D).grid(row=2, column=0)
tk.Button(racine, text='vider', command=empty).grid(row=3, column=0)

##
racine.mainloop()