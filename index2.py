from tkinter import *

def obter_texto():
    texto = entry.get()  # Obtém o texto inserido no campo de entrada
    label.config(text=texto)  # Atualiza o texto do rótulo com o texto inserido

root = Tk()

entry = Entry(root)
entry.pack()

button = Button(root, text="Obter Texto", command=obter_texto)
button.pack()

label = Label(root, text="")
label.pack()

root.mainloop()

