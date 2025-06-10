from dados_coletados import lista_respostas
from funcoes import *


TelaAbertura() # Abertura do programa.

while True:
    print() # Pula uma linha. Apenas estética
    print("O que deseja saber sobre o burnout?")

    # Cria a variável oQueFazer que guiará o curso do programa.
    oQueFazer = input('''1 - Perguntar sobre algo.
2 - Score e nível de risco de pessoa solicitada.
3 - Impressão de todas as pessoas.
4 - Exibir percentual de pessoas com nível de risco baixo.
5 - Exibir percentual de pessoas com nível de risco moderado.
6 - Exibir percentual de pessoas com nível de risco alto.
7 - Encerrar o programa.
Digite aqui: ''')
    
    # Se o input for incorreto, pede novamente ao usuário
    while oQueFazer not in "1234567" or len(oQueFazer) > 1 or len(oQueFazer) < 1:
        print("Ops! O que foi digitado não está entre as opções!")
        oQueFazer = input("O que deseja saber sobre o burnout? ")

    # Passando da etapa anterior a resposta com certeza é um número, então ele é passado para int para facilitar o código
    oQueFazer = int(oQueFazer)

    # PERGUNTAR SOBRE
    #MatrizFuncoes = [
    #    SugereMinimizacaoSintomas
    #]
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