import subprocess
import sys
import platform
import time

def instalar_pacotes():
    pacotes_necessarios = ["pwinput"]
    sistema_operacional = platform.system().lower()
    amarelo = '\033[1;33m'; tag = '\033[m'
    vermelho = '\033[1;31m';tag = '\033[m'

    reset = '\033[0m'

    for pacote in pacotes_necessarios:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])
            print(f"{pacote} instalado com sucesso.")
        except subprocess.CalledProcessError as e:
            if sistema_operacional == "linux":
                print(amarelo,f"Erro ao instalar {pacotes_necessarios}. Sistema operacional Linux 🐧 detectado.")
                time.sleep(4)
                print(reset,"# 1 Crie um ambiente virtual:",vermelho, "python3 -m venv venv")
                print(reset,"# 2 Ative o ambiente virtual:",vermelho,"source venv/bin/activate")
                print(amarelo,"# 3 Rode novamente o programa ")
                print(reset,"O erro que você está enfrentando indica que você está tentando \ninstalar pacotes globalmente no sistema e o ambiente Python parece ser externamente gerenciado.\nEm sistemas Linux, como o Ubuntu, você geralmente não deve instalar pacotes globalmente usando pip diretamente,\nPois isso pode interferir com o sistema operacional.")
            else:
                print(f"Erro ao instalar {pacote}: {e}")

if __name__ == "__main__":
    instalar_pacotes()



# Em sistemas Linux, como o Ubuntu, você geralmente não 
# deve instalar pacotes globalmente usando pip diretamente,
# pois isso pode interferir com o sistema operacional.]
# 1 Crie um ambiente virtual: python3 -m venv venv
# 2 Ative o ambiente virtual: source venv/bin/activate
# 3 depois python install_packages.py ou, rode o programa
# lembre depois de apagar a pasta [venv] antes de fazer push para o git 👍



