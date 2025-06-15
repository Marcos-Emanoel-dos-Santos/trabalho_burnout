from dados_coletados import lista_respostas
from MatrizesAuxiliares import *
from funcoes import *

print("=#="*10)
print("ANÁLISE COMPUTACIONAL DE RISCO DE BURNOUT")
print("PUCPR - Bacharelado em Ciência da Computação")
print("Disciplina: Raciocínio Algorítmico - Turma U")
print("Este programa analisa sintomas de burnout e sugere ações para minimizar seus efeitos.")
print("=#="*10)

# Cria a matriz de scores
MatrizIndividuoScore = CalculaScoreIndividual(lista_respostas, MatrizScore)
# Cria a matriz de classificação de riscos
MatrizRisco = ClassificaNivelRisco(MatrizIndividuoScore)
# Copia a matriz original e adiciona as colunas score e risco
lista_respostas = AtualizaMatrizScoreRisco(lista_respostas, MatrizIndividuoScore, MatrizRisco)

while True:
    print() # Pula uma linha. Apenas estética
    print(lista_respostas[3])
    oQueFazer = TelaAbertura() # Abertura do programa.
    
    # Passando da etapa anterior a resposta com certeza é um número, então ele é passado para int para facilitar o código
    oQueFazer = int(oQueFazer)

    print() # Pula uma linha. Apenas estética

    # NÃO SE APEGUEM AOS IFS, VOU DAR UM JEITO DE DIMINUIR A QUANTIDADE DE LINHAS
    # OK
    if oQueFazer == 1:
        SugereMinimizacaoSintomas(MatrizMinimizacao)
    elif oQueFazer == 2:
        print("Bana")
    elif oQueFazer == 3:
        print("Bana")
    elif oQueFazer == 4:
        imprimePercentual(MatrizIndividuoScore, "baixo")
    elif oQueFazer == 5:
        imprimePercentual(MatrizIndividuoScore, "moderado")
    elif oQueFazer == 6:
        imprimePercentual(MatrizIndividuoScore, "alto")
    elif oQueFazer == 7:
        print("Encerrando o programa.")
        break