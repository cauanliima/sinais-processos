from tkinter import *
import os
import subprocess

def getPs(filtro=None):
    if filtro:
        comando = f'ps -auf | grep {filtro}'  # Comando Bash que queremos executar
    else:
        comando = 'ps -auf'
    print(comando)
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    print(resultado)
    return resultado.stdout

def kill_process(PID=None):
    PID = entry_PID.get()
    if PID:
        comando = f'kill -9 {PID}'  # Comando Bash que queremos executar
        print(comando)
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(resultado)

def stop_process(PID=None):
    PID = entry_PID.get()
    if PID:
        comando = f'kill -19 {PID}'  # Comando Bash que queremos executar
        print(comando)
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(resultado)

def cont_process(PID=None):
    PID = entry_PID.get()
    if PID:
        comando = f'kill -18 {PID}'  # Comando Bash que queremos executar
        print(comando)
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(resultado)
        
def chage_pri(PID=None):
    PID = entry_PID.get()
    nice = entry_pri.get()
    if PID:
        comando = f'renice -n {nice} {PID}'  # Comando Bash que queremos executar
        print(comando)
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(resultado)
        
def chage_cpu(PID=None):
    PID = entry_PID.get()
    CPU = entry_cpu.get()
    if PID:
        comando = f'taskset -cp {CPU} {PID}'  # Comando Bash que queremos executar
        print(comando)
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(resultado)

def obter_texto():
    label.config(text=getPs(entry_filter.get()))  # Atualiza o texto do rótulo com o texto inserido


root = Tk()

largura = 1300  # Defina a largura desejada da janela
altura = 700   # Defina a altura desejada da janela

# Define o tamanho da janela principal
root.geometry(f"{largura}x{altura}")

# Configurar tamanho da célula do grid para ocupar todo o espaço disponível na janela
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


container1 = Frame(root)
container1.grid(row=0, column=0, sticky="nsew")

label = Label(container1, text=getPs(),justify="left")
label.pack()

# Container principal para centralizar os dois containers
container = Frame(root)
container.grid(row=1, column=0, sticky="nsew")

# Configurar tamanho das células do grid dentro do container
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)
container.grid_columnconfigure(1, weight=1)

container2 = Frame(container)
container2.grid(row=0, column=0, sticky="e")

entry_filter = Entry(container2)
entry_filter.grid(row=0, column=0)

button_filter = Button(container2, text="Atualizar", command=obter_texto)
button_filter.grid(row=0, column=1)

entry_PID = Entry(container2)
entry_PID.grid(row=2, column=0)

button_KILL = Button(container2, text="Kill", command=kill_process)
button_KILL.grid(row=1, column=1)

button_STOP = Button(container2, text="Stop", command=stop_process)
button_STOP.grid(row=2, column=1)

button_CONT = Button(container2, text="Continue", command=cont_process)
button_CONT.grid(row=3, column=1)

container3 = Frame(container)
container3.grid(row=0, column=1, sticky="w")

entry_pri = Entry(container3)
entry_pri.grid(row=4, column=0)

button_pri = Button(container3, text="Prioridade", command=chage_pri)
button_pri.grid(row=4, column=1)

entry_cpu = Entry(container3)
entry_cpu.grid(row=5, column=0)

button_cpu = Button(container3, text="CPU", command=chage_cpu)
button_cpu.grid(row=5, column=1)
root.mainloop()

