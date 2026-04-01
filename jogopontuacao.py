pontos = {}
for i in range(3):
    nome = input("Digite o nome: ")
    pontuação = input("Digite os pontos iniciais: ")
    pontos[nome] = pontuação
for jogador, pontuação in pontos.items():
    print(f"{jogador} | {pontuação}")