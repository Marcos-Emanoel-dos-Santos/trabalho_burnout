from dados_coletados import lista_respostas
from funcoes import *

print("=#="*10)
print("ANÁLISE COMPUTACIONAL DE RISCO DE BURNOUT")
print("PUCPR - Bacharelado em Ciência da Computação")
print("Disciplina: Raciocínio Algorítmico - Turma U")
print("Este programa analisa sintomas de burnout e sugere ações para minimizar seus efeitos.")
print("=#="*10)

MatrizScore = CalculaScoreIndividual(lista_respostas)
MatrizRisco = ClassificaNivelRisco(MatrizScore)
lista_respostas = AtualizaMatrizScoreRisco(lista_respostas, MatrizScore, MatrizRisco)

while True:
    print() # Pula uma linha. Apenas estética
    print(lista_respostas[1])
    oQueFazer = TelaAbertura() # Abertura do programa.
    
    # Se o input for incorreto, pede novamente ao usuário
    while oQueFazer not in "1234567" or len(oQueFazer) > 1 or len(oQueFazer) < 1:
        print("Ops! O que foi digitado não está entre as opções!")
        oQueFazer = input("O que deseja saber sobre o burnout? ")

    # Passando da etapa anterior a resposta com certeza é um número, então ele é passado para int para facilitar o código
    oQueFazer = int(oQueFazer)


    print() # Pula uma linha. Apenas estética
    if oQueFazer == 1:
        SugereMinimizacaoSintomas()
    elif oQueFazer == 2:
        print("Bana")
    elif oQueFazer == 3:
        print("Bana")
    elif oQueFazer == 4:
        print("Bana")
    elif oQueFazer == 5:
        print("Bana")
    elif oQueFazer == 6:
        print("Bana")
    elif oQueFazer == 7:
        print("Encerrando o programa.")
        break