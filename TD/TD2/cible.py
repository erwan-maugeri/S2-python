# ERWAN MAUGERI LDDMP

import tkinter as tk

racine = tk.Tk()
racine.title("cible")

WIDTH, HEIGHT, THIKNESS = 500, 500, 10

canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH, bg='black')
canvas.grid(row=0, column=0)
color = ["blue", "green", "black", "yellow", "magenta", "red"]

x0 = 0
y0 = 0
x1 = WIDTH
y1 = HEIGHT

for i in range(HEIGHT//THIKNESS//2):
    canvas.create_oval(x0, y0, x1, y1, fill=color[i%6], outline="")
    x0 += THIKNESS
    y0 += THIKNESS

    x1 -= THIKNESS
    y1 -= THIKNESS

racine.mainloop()