from dados_coletados import lista_respostas
from funcoes import *


print("Bem-vindo! Esta aplicação tem o intuito de fornecer informações acerca do burnout.")
while True:
    print("O que deseja fazer agora?")

    # Cria a variável oQueFazer que guiará o curso do programa.
    oQueFazer = input('''1 - Perguntar sobre algo.
2 - Score e nível de risco de pessoa solicitada.
3 - Impressão de todas as pessoas.
4 - Exibir percentual de pessoas com nível de risco baixo.
5 - Exibir percentual de pessoas com nível de risco moderado.
6 - Exibir percentual de pessoas com nível de risco alto.
7 - Encerrar o programa.
''')
    
    # Se o input for incorreto, pede novamente ao usuário
    while oQueFazer not in "1234567" or len(oQueFazer) > 1:
        print("Ops! Este número não está entre as opções.")
        oQueFazer = input("O que deseja fazer agora?")

    # Passando da etapa anterior a resposta com certeza é um número, então ele é passado para int para facilitar o código
    oQueFazer = int(oQueFazer)

    if oQueFazer == 7:
        print("Finalizando o programa.")
        break
    else:
        print() # pular uma linha (só estética)
        TelaAbertura(oQueFazer)
        