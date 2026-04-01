import json
import os
ARQUIVO = "notas.json"
def carregar_notas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []
def salvar_notas(notas):
    with open(ARQUIVO, "W") as f:
        json.dump(notas, f, indent=4)
def adicionar_nota():
    titulo =str(input("Título da nota: "))
    conteudo = str(input("Conteúdo da nota: "))
    notas = carregar_notas()
    nota = {
        "Título" = titulo
        "Conteúdo" = conteudo
        }