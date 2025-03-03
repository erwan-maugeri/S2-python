import tkinter as tk

racine = tk.Tk() # creation de la fenêtre
racine.title('exemple') # ajoute un titre à la fenêtre

label1 = tk.Label(racine, text="hello")
label2 = tk.Label(racine, text="world")
label3 = tk.Label(racine, text="click on the button")
bouton = tk.Button(racine, text="click me", background="blue") # définir le bouton

bouton.grid(row=1, column=1) # positionnement du widget
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)

racine.mainloop() #trjrs mettre à la fin