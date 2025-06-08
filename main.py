from dados_coletados import lista_respostas
from funcoes import *

i = 0
for i in range(len(lista_respostas)):
    if i > 0: # Pula o cabeçalho
        print(CalculaScoreIndividual(lista_respostas[i]), f"Linha: {i}") # Teste inicial
        i += 1