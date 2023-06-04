# ----------------------------------------------------------------------------------------------

# Gerenciador de processos
# Descrição: Tarefa correspondente à nota da segunda avaliação.

# Data da Entrega: 07 de junho de 2023

# DCA-0125 Sistemas de Tempo Real
# Grupo:
# FRANCISCA PAULA DE SOUZA BRAZ
# CAUAN MARCELO LIMA

# ----------------------------------------------------------------------------------------------


from tkinter import *
import os
import subprocess

def update_entry_content():
    obter_texto()
    root.after(1000, update_entry_content)  # Chame esta função novamente após 1 segundo (1000 ms)
    

def getPs(filtro=None):
    if filtro:
        comando = f'ps -af -o pid,ppid,ni,%cpu,%mem,cmd | grep {filtro}'  # Comando Bash que queremos executar

    else:
        comando = 'ps -af -o pid,ppid,ni,%cpu,%mem,cmd'
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

# ===== Criando interface =====
root = Tk()
root.title("Gerenciador de Processos")
largura = 1300  # Defina a largura desejada da janela
altura = 700   # Defina a altura desejada da janela
root.geometry(f"{largura}x{altura}")# Define o tamanho da janela principal
root.configure(background = "MIDNIGHTBLUE")
root.resizable(width = True, height = True)

# ===== Carregando imagens =====
logo = PhotoImage(file = "logo.png")

# ===== Widgets =====
TopFrame = Frame(root, width = 1400, height = 60, bg = "MIDNIGHTBLUE", relief = "raise")
TopFrame.pack(side=TOP)

LogoLabel = Label(TopFrame, image = logo, bg = "MIDNIGHTBLUE")
LogoLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

MiddleFrame = Frame(root, width = 1400, height = 500, bg = "MIDNIGHTBLUE", relief = "raise")	
MiddleFrame.pack(side=TOP)

label = Label(MiddleFrame, text=getPs(),justify="left")
label.pack(side=TOP)

BottomFrame = Frame(root, width = 1400, height = 300, bg = "WHITE", relief = "raise")
BottomFrame.pack(side=BOTTOM)

labelPID = Label(BottomFrame, text="PID")
labelPID.place(relx = 0.28,rely = 0.1)

labelPrioNice = Label(BottomFrame, text="PRIORITY")
labelPrioNice.place(relx = 0.255,rely = 0.4)

labelCPU = Label(BottomFrame, text="CPU's")
labelCPU.place(relx = 0.27,rely = 0.7)

entry_PID = StringVar() 
entry_filter = Entry(BottomFrame, width = 10, textvariable=entry_PID, justify = "center")
entry_filter.place(relx = 0.3, rely=0.1)

entry_pri = StringVar() #Aqui comeca a funcionalidade do botao kill + entrada kill. A variavel nesse caso eh digitadoPID
prioNiceEntry = Entry(BottomFrame, width = 10, textvariable=entry_pri, justify = "center")
prioNiceEntry.place(relx = 0.3, rely=0.4)

entry_cpu= StringVar() #Aqui comeca a funcionalidade do botao kill + entrada kill. A variavel nesse caso eh digitadoPID
entry_chance_cpu = Entry(BottomFrame, width = 10, textvariable=entry_cpu, justify = "center")
entry_chance_cpu.place(relx = 0.3, rely=0.7)

killButton = Button(BottomFrame, text="KILL",  width = 12, command=kill_process, justify = "center")
killButton.place(relx = 0.4, rely=0.1)

stopButton = Button(BottomFrame, text = "STOP", width = 12, command=stop_process, justify = "center")
stopButton.place(relx = 0.5, rely=0.1)

continueButton = Button(BottomFrame, text = "CONTINUE ", width = 12, command=cont_process, justify = "center")
continueButton.place(relx = 0.6, rely=0.1)

filterButton = Button(BottomFrame, text = "REFRESH", width = 12, command=obter_texto, justify = "center")
filterButton.place(relx = 0.7, rely=0.1)

prioButton = Button(BottomFrame, text = "PRIORITY", width = 12, command=chage_pri, justify = "center")
prioButton.place(relx = 0.4, rely=0.4)

alocaButton = Button(BottomFrame, text = "CHAGE CPU", width = 12, command=chage_cpu, justify = "center")
alocaButton.place(relx = 0.4, rely=0.7)


update_entry_content()  # Inicialmente, chame a função para atualizar o conteúdo do Entry

root.mainloop()

