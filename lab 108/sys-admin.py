# Importando bibliotecas
import os
import subprocess
import platform

# Determine o sistema operacional atual
current_os = platform.system()

# Defineo comando apropriado para listar o conteúdo do diretório
if current_os == "Windows":
    list_dir_command = ["cmd", "/c", "dir"]
else:
    list_dir_command = ["ls"]

# Executando um comando de listagem de diretórios usando os.system()
os.system(" ".join(list_dir_command))

# Executando um comando de listagem de diretórios usando subprocess.run()
subprocess.run(list_dir_command)

# Usando subprocess.run() com um argumento adicional para formato de listagem longa
if current_os == "Windows":
    list_dir_long_command = ["cmd", "/c", "dir"]
else:
    list_dir_long_command = ["ls", "-l"]

subprocess.run(list_dir_long_command)

# Usando subprocess.run() com dois argumentos adicionais para listar um arquivo específico
file_name = "README.md"
if current_os == "Windows":
    list_file_command = ["cmd", "/c", "dir", file_name]
else:
    list_file_command = ["ls", "-l", file_name]

subprocess.run(list_file_command)

# Executando uname -a ou comando equivalente
if current_os == "Windows":
    uname_command = ["cmd", "/c", "ver"]
else:
    uname_command = ["uname", "-a"]

subprocess.run(uname_command)

# Executando ps -x ou comando equivalente
if current_os == "Windows":
    ps_command = ["cmd", "/c", "tasklist"]
else:
    ps_command = ["ps", "-x"]

subprocess.run(ps_command)

# A função os.system executa o comando como uma string
# A função subprocess.run recebe uma lista de argumentos de comando
# Os comandos são definidos condicionalmente para lidar com sistemas do tipo Unix e Windows