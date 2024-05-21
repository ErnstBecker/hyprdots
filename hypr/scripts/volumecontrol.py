import subprocess
import re
import sys

# Função para obter o volume atual
def get_current_volume():
    # Executa o comando pactl e captura a saída
    output = subprocess.check_output(["pactl", "list", "sinks"]).decode("utf-8")
    # Usa uma expressão regular para encontrar a linha que contém o volume
    volume_match = re.search(r'Volume:.*?(\d+)%', output, re.DOTALL)
    # Se o valor de volume for encontrado, retorna-o como um número inteiro
    if volume_match:
        return int(volume_match.group(1))
    else:
        # Se não for encontrado, retorna 0
        return 0

# Definindo o limite de volume
volume_limit = 150

# Obtendo a ação passada como argumento
action = sys.argv[1]

# Obtendo o volume atual
current_volume = get_current_volume()

# Calculando o novo volume com base na ação
if action == "--inc":
    new_volume = min(current_volume + 5, volume_limit) # Aumenta o volume em 5%, mas não ultrapassa o limite
elif action == "--dec":
    new_volume = max(current_volume - 5, 0) # Diminui o volume em 5%, sem cair abaixo de zero
else:
    sys.exit(1) # Sai do script se a ação não for reconhecida

# Define o novo volume usando o comando pactl
subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{new_volume}%"])
