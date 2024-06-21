# OS - Modulo que possibilita interagir com o sistema operacional.
import os

# 1 - Consultar funcionalidades do módulo "os"
# help('os')

# 2 - Retornar a pasta atual
print(os.getcwd())

# 3- Listar arquivos e pastas
print(os.listdir())

# 4 - Apresentar a versão do SO
os.system('ver')

# 5 = Configurações da máquina
os.system('systeminfo')

# 6 - Ip config
os.system('ipconfig')

# 7 - Desligar o PC
os.system('shutdown /s') # desliga em um minuto - Windows
os.system('shutdown /s /t 0') # desliga imediatamente - Windows
os.system('shutdown now') # desliga imediatamente - Linux

os.system('shutdown /a') # Cancela o desligamento - 

