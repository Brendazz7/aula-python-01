import subprocess
import os
def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print("Erro ao executar comando: ", e)
#1
def mostrar_ip(): 
    executar_comando("ipconfig")
#2
def renovar_ip():
    executar_comando("ipconfig /renew")
#3
def mostrar_ip_completo():
    executar_comando("ipconfig /all")
#4
def ping_host():
    host = input("Digite o ip ou o HOSTNAME: ")
    executar_comando(f"ping {host}")
#5
def listar():
    executar_comando("dir")
#6
def info_sistema():
    executar_comando("systeminfo")
#7
def tarefas_executadas():
    executar_comando("tasklist")
#8
def estatística_rede():
    executar_comando("netstat")
#9
def exluir_processo():
    host1 = input("digite o ip ou HOSTNAME")
    executar_comando(f"taskkill /pid {host1}")
#10
def desligar_pc():
    executar_comando("shutdown")
def menu():
    while True:
        print ("\n===========Ferramenta de rede===========")
        print ("\n 1 - MOSTRAR IP")
        print ("\n 2 - RENOVAR IP")
        print ("\n 3 - MOSTRAR CONFIG DE REDE")
        print ("\n 4 - PING")
        print ("\n 5 - LISTAR")
        print ("\n 6 - INFO SISTEMA")
        print ("\n 7 - TAREFAS EXECUTADAS")
        print ("\n 8 - ESTATISTICA REDE")
        print ("\n 9 - EXCLUIR PROCESSOS")
        print ("\n 10 - DESLIGAR PC")
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
            case "5":
                listar()
            case "6":
                info_sistema()
            case "7":
                tarefas_executadas()
            case "8":
                estatística_rede()
            case "9":
                exluir_processo()
            case "10":
                desligar_pc()
            case "0":
                print("Saindo") 
                break
            case _:
                print("Eita caba sabido!!!")
if __name__=="__main__":
    menu()