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
        comando = f'kill -SIGKILL {PID}'  # Comando Bash que queremos executar
        print(comando)
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(resultado)

def stop_process(PID=None):
    PID = entry_PID.get()
    if PID:
        comando = f'kill -SIGKILL {PID}'  # Comando Bash que queremos executar
        print(comando)
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(resultado)

def cont_process(PID=None):
    PID = entry_PID.get()
    if PID:
        comando = f'kill -SIGKILL {PID}'  # Comando Bash que queremos executar
        print(comando)
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(resultado)

def obter_texto():
    label.config(text=getPs(entry_filter.get()))  # Atualiza o texto do rótulo com o texto inserido

root = Tk()

container1 = Frame(root)
container1.pack()

label = Label(container1, text=getPs(),justify="left")
label.pack()

container2 = Frame(root)
container2.pack()
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

entry_pri = Entry(container2)
entry_pri.grid(row=4, column=0)

button_pri = Button(container2, text="Prioridade", command=obter_texto)
button_pri.grid(row=4, column=1)

entry_cpu = Entry(container2)
entry_cpu.grid(row=5, column=0)

button_cpu = Button(container2, text="CPU", command=obter_texto)
button_cpu.grid(row=5, column=1)
root.mainloop()

