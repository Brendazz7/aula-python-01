import subprocess
import os
def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print("Erro ao executar comando: ", e)

def mostrar_ip(): 
    executar_comando("ipconfig")
def renovar_ip():
    executar_comando("ipconfig /renew")
def mostrar_ip_completo():
    executar_comando("ipconfig /all")
def ping_host():
    host = input("Digite o ip ou o HOSTNAME: ")
    executar_comando(f"ping {host}")
def menu():
    while True:
        print ("\n===========Ferramenta de rede===========")
        print ("\n 1 - MOSTRAR IP")
        print ("\n 2 - RENOVAR IP")
        print ("\n 3 - MOSTRAR CONFIG DE REDE")
        print ("\n 4 - PING")
        print ("\n 0 - SAIR")
        print ("\n=========== Criado pela namorada de Saw <3 ===========")
        opcao = str(input("Escolha: "))
        match opcao:
            case "1":
                mostrar_ip()
            case "2":
                renovar_ip()
            case "3":
                mostrar_ip_completo()
            case "4":
                ping_host()
            case "0":
                print("Saindo") 
                break
            case _:
                print("Eita caba sabido!!!")
if __name__=="__main__":
    menu()