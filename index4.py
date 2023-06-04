import subprocess

comando = "ls -l"  # Comando Bash que queremos executar

resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

# Verifica se o comando foi executado com sucesso
if resultado.returncode == 0:
    saida = resultado.stdout  # Saída do comando
    print("Saída do comando:")
    print(saida)
else:
    erro = resultado.stderr  # Erro do comando
    print("Erro ao executar o comando:")
    print(erro)