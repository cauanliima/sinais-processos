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

label = Label(root, text=getPs(),justify="left")
label.pack()

entry_filter = Entry(root)
entry_filter.pack()

button_filter = Button(root, text="Atualizar", command=obter_texto)
button_filter.pack()

entry_PID = Entry(root)
entry_PID.pack()

button_KILL = Button(root, text="Kill", command=kill_process)
button_KILL.pack()

button_STOP = Button(root, text="Stop", command=stop_process)
button_STOP.pack()

button_CONT = Button(root, text="Continue", command=cont_process)
button_CONT.pack()

entry_pri = Entry(root)
entry_pri.pack()

button_pri = Button(root, text="Prioridade", command=obter_texto)
button_pri.pack()

entry_cpu = Entry(root)
entry_cpu.pack()

button_cpu = Button(root, text="CPU", command=obter_texto)
button_cpu.pack()

root.mainloop()

