#Criação do dicionário XD!!!
aluno = {}
#ENTRADA DE DADOS
aluno["nome"] = input("Digite o nome do aluno: ")
aluno["curso"] = input("Digite o curso do aluno: ")
aluno["nota"] = float(input("Digite a sua nota: "))
#SAÍDA DE DADOS :P
print(f"O nome do aluno é: {aluno['nome']}")
print(f"O curso do aluno é: {aluno['curso']}")
print("Aprovado" if aluno["nota"] >= 18 else "Reprovado")