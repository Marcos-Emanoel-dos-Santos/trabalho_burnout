def TelaAbertura():
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

    return oQueFazer

# Retorna uma matriz com indivíduos e score de cada um na forma [individuo, score]
def CalculaScoreIndividual(matriz, MatrizScore):
    listaScores = []

    for individuoIndex in range(len(matriz)): # Para cada indivíduo da matriz
        scoreIndividual = 0
        if individuoIndex > 0:

            for respostaIndex in range(1, len(matriz[individuoIndex])): # Para cada uma de suas respostas
                resposta = matriz[individuoIndex][respostaIndex]
                possiveisRespostas = MatrizScore[respostaIndex-1]

                for respIndex in range(len(possiveisRespostas)):
                    if resposta == possiveisRespostas[respIndex]: # Verifica se a resposta coincide com o valor naquele índice
                        # Soma o índice (valor) multiplicado pelo peso no score
                        scoreIndividual += respIndex*MatrizScore[respIndex][-1]
        # Adiciona o indivíduo e seu score a uma matriz
        listaScores.append([individuoIndex, scoreIndividual])

    return listaScores # Retorna o resultado

# retorna uma matriz com indivíduos e nível de risco na forma [individuo, nivelRisco]
def ClassificaNivelRisco(matriz):
    MatrizRisco = [] # Matriz que armazenará o risco e a posição de cada um na lista_resposta

    for i in range(len(matriz)): # armazena a forma [pessoa, risco] sendo "pessoa" a posição de cada um em lista_resposta
        if matriz[i][1] <= 10:
            MatrizRisco.append([i, "baixo"])
        elif matriz[i][1] <= 20:
            MatrizRisco.append([i, "moderado"])
        else:
            MatrizRisco.append([i, "alto"])

    return MatrizRisco


def SugereMinimizacaoSintomas(MatrizMinimizacao):
    print("Digite o número que corresponda ao sintoma que deseja saber sobre:")
    usuarioInput = input('''1 - Cansaço físico
2 - Energia para tarefas
3 - Motivação pelo trabalho
4 - Procrastinação
5 - Sentido no trabalho 
6 - Pensamentos negativos
7 - Isolamento emocional 
8 - Isolamento social 
9 - Fez algo prazeroso
''')
    # Enquanto o usuário não digitar uma resposta válida, pede uma nova resposta
    while usuarioInput not in "123456789" or len(usuarioInput) > 1 or len(usuarioInput) < 1:
        usuarioInput = ("Inválido. Tente novamente.")
    # Depois de aceita, a resposta com certeza é um número inteiro e, portanto, int() não retornará erro.
    usuarioInput = int(usuarioInput)
    print("Resposta:")
    print(MatrizMinimizacao[usuarioInput-1]) # busca na matriz a resposta correspondente ao input e imprime
    print() # pular uma linha (só estética)

def CalculaPercentual(matriz_risco):
    # Contadores para cada nível de risco
    baixo = 0
    moderado = 0
    alto = 0
    
    # Total de pessoas
    total_pessoas = len(matriz_risco)
    
    # Contagem dos níveis de risco
    for individuo in matriz_risco:
        nivel = individuo[1]
        if nivel == "baixo":
            baixo += 1
        elif nivel == "moderado":
            moderado += 1
        elif nivel == "alto":
            alto += 1

    # Cálculo dos percentuais (arredondados para 2 casas decimais)
    percentual_baixo = f"{(baixo / total_pessoas)*100:.2f}"
    percentual_moderado = f"{(moderado / total_pessoas)*100:.2f}"
    percentual_alto = f"{(alto / total_pessoas) * 100:.2f}"

    # Retorna uma matriz com os percentuais
    return [["baixo", percentual_baixo], ["moderado", percentual_moderado], ["alto", percentual_alto]]


def AtualizaMatrizScoreRisco(matriz, matScore, matRisco):
    # Transforma cada lista de indivíduo em uma lista contendo apenas seu nome
    for i in range(len(matriz)):
        matriz[i] = [matriz[i][0]]

    # Adiciona score e risco ao cabeçalho da matriz
    matriz[0].append("score")
    matriz[0].append("risco")

    for i in range(1, len(matriz)): # Para cada item da matriz, pulando o cabeçalho
        matriz[i].append(matScore[i-1][1]) # Adiciona score à matriz original
        matriz[i].append(matRisco[i-1][1]) # Adiciona risco à matriz original

    return matriz


def ImprimeMatrizScoreRisco(matriz):
   if len(matriz) == 1: # Se for uma pessoa específica
        print("Pessoa, Score, Risco")
        print(f"{matriz[0][0]}, {matriz[0][1]}, {matriz[0][2]}")
   else: # Se for a matriz toda
       print("Pessoa, Score, Risco")
       for i in range(1, len(matriz)):
           print(f"{matriz[i][0]}, {matriz[i][0] }, {matriz[i][0]}") 
           # ['pessoa_1', 12, 'moderado']

# FUNÇÕES PRÓPRIAS DA EQUIPE

#Retorna um indivíduo ou todos os indivíduos da matriz em caso de individuo=-1, dependendo do parâmetro colocado
def buscaDadosMatriz(matriz, pessoa=-1):

    pessoa = int(pessoa) # Transforma o input em int

    while pessoa > 120 or (pessoa < 1 and pessoa != -1): # Verifica se o valor é válido
        pessoa = input("Digite um valor válido: Entre 1 e 120.")
    
    if pessoa != -1: # Se 
        return [matriz[pessoa]]
    return matriz #retorna toda a matriz  


    

# Imprime o percentual de indivíduos em certa faixa tendo como parâmetros uma matriz de referência
# e o nivel de risco que deseja que seja exibido
def imprimePercentual(MatrizIndividuoScore, risco):
    percentuais = CalculaPercentual(ClassificaNivelRisco(MatrizIndividuoScore))

    if risco == 'baixo':
        print(f"Percentual de pessoas com risco BAIXO: {percentuais[0][1]}%")
    elif risco == 'moderado':
        print(f"Percentual de pessoas com risco MODERADO: {percentuais[0][1]}%")
    else:
        print(f"Percentual de pessoas com risco ALTO: {percentuais[0][1]}%")