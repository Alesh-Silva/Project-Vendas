import subprocess
import sys
import platform

def instalar_pacotes():
    pacotes_necessarios = ["pwinput"]
    sistema_operacional = platform.system().lower()

    if sistema_operacional == "linux":
        print("Sistema operacional Linux detectado.")
        print("# 1 Crie um ambiente virtual: python3 -m venv venv")
        print("# 2 Ative o ambiente virtual: source venv/bin/activate")
    else:
        for pacote in pacotes_necessarios:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])
                print(f"{pacote} instalado com sucesso.")
            except subprocess.CalledProcessError as e:
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



