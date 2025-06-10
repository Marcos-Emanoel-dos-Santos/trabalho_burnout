def TelaAbertura():
    print("=#="*10)
    print("ANÁLISE COMPUTACIONAL DE RISCO DE BURNOUT")
    print("PUCPR - Bacharelado em Ciência da Computação")
    print("Disciplina: Raciocínio Algorítmico - Turma U")
    print("Este programa analisa sintomas de burnout e sugere ações para minimizar seus efeitos.")
    print("=#="*10)
    
def CalculaScoreIndividual(matriz):
    # Cria uma matriz com as possíveis respostas para cada pergunta, e em ordem
    # É visível, pela tabela de pesos, que é possível relacionar peso ao índice,
    # Ex: algo no índicie 0 também tem peso 0. Usei isso para a lógica.
    MatrizScore = [
        ["Nunca", "Às vezes", "Frequentemente", "Todos os dias"],
        ["Sim", "Com dificuldade", "Não conseguiu"],
        ["Sim", "Neutro", "Nada motivado(a)"],
        ["Não", "Um pouco", "Sim, constantemente"],
        ["Não", "Às vezes", "Quase sempre"],
        ["Não", "Já tive essa semana", "Tenho todos os dias"],
        ["Não", "Levemente", "Muito"],
        ["Não", "Com esforço", "Me isolei totalmente"],
        ["Sim", "Não tive tempo", "Nem vontade tive"]
    ]

    listaScores = []

    for individuoIndex in range(len(matriz)): # Para cada indivíduo da matriz
        if individuoIndex > 0:
            scoreIndividual = 0

            for respostaIndex in range(1, len(matriz[individuoIndex])): # Para cada uma de suas respostas
                resposta = matriz[individuoIndex][respostaIndex]
                possiveisRespostas = MatrizScore[respostaIndex-1]

                for respIndex in range(len(possiveisRespostas)):
                    if resposta == possiveisRespostas[respIndex]: # Verifica se a resposta coincide com o valor naquele índice
                        scoreIndividual += respIndex # Soma o índice (peso) ao score

            listaScores.append([individuoIndex, scoreIndividual])

    return listaScores

def ClassificaNivelRisco(matriz):
    MatrizRisco = []
    for individuo in matriz:
        if individuo[1] <= 10:
            individuo.append("baixo")
        elif individuo[1] <= 20:
            individuo.append("moderado")
        else:
            individuo.append("alto")
        MatrizRisco.append(individuo)

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

#def CalculaPercentual():

#def AtualizaMatrizScoreRisco():

#def ImprimeMatrizScoreRisco():