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
    return oQueFazer

# Retorna uma matriz com indivíduos e score de cada um na forma [individuo, score]
def CalculaScoreIndividual(matriz):
    # Cria uma matriz com as possíveis respostas para cada pergunta, e em ordem
    # É visível, pela tabela de pesos, que é possível relacionar peso ao índice,
    # Ex: algo no índicie 0 também tem peso 0. Usei isso para a lógica.
    MatrizScore = [
        ["Nunca", "Às vezes", "Frequentemente", "Todos os dias", 3],
        ["Sim", "Com dificuldade", "Não conseguiu", 2],
        ["Sim", "Neutro", "Nada motivado(a)", 3],
        ["Não", "Um pouco", "Sim, constantemente", 2],
        ["Não", "Às vezes", "Quase sempre", 3],
        ["Não", "Já tive essa semana", "Tenho todos os dias", 3],
        ["Não", "Levemente", "Muito", 2],
        ["Não", "Com esforço", "Me isolei totalmente", 2],
        ["Sim", "Não tive tempo", "Nem vontade tive", 2]
    ]

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

        listaScores.append([individuoIndex, scoreIndividual])

    return listaScores

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


def SugereMinimizacaoSintomas(): # O input será um número de 1 a 9
    MatrizMinimizacao = [
        "Evite estudar até tarde e reduza o uso de telas à noite. Incorpore pausas estratégicas durante o dia (técnica Pomodoro, por exemplo).",
        "Organize sua rotina começando por pequenas vitórias, como arrumar a cama ou tomar café — isso ativa o cérebro e gera estímulo. ",
        "Busque aplicar conteúdos em projetos reais, participar de hackathons, ou explorar temas que te inspiram dentro do curso.",
        "Use listas com entregas claras e realistas por dia. Elimine distrações e crie um ambiente de foco (limpo, silencioso, com metas visíveis).",
        "Converse com colegas e professores, entenda o impacto do que você está estudando e crie conexões com seus valores pessoais.",
        "Reconheça o limite entre cansaço e sofrimento. Conversar com alguém que compreenda sua trajetória pode aliviar a sobrecarga emocional.",
        "Mesmo em poucos minutos, práticas como respiração guiada ou alongamentos reduzem o acúmulo emocional.",
        "Uma ligação de 5 minutos ou uma pausa para café com alguém confiável ajuda a recuperar o senso de pertencimento." ,
        "Desenhar, ouvir música, assistir algo leve, cozinhar... O prazer gratuito recarrega energia emocional e combate a anedonia."
    ]
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
    while usuarioInput not in "123456789" or len(usuarioInput) > 1 or len(usuarioInput) < 1:
        usuarioInput = ("Inválido. Tente novamente.")
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
    matriz[0].append("score")
    matriz[0].append("risco")
    for i in range(1, len(matriz)):
        while len(matriz[i]) < 12:
            matriz[i].append(None)
        matriz[i][10] = matScore[i-1][1]
        matriz[i][11] = matRisco[i-1][1]
    return matriz

#def ImprimeMatrizScoreRisco():