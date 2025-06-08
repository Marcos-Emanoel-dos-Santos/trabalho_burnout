def CalculaScoreIndividual(matriz):
    # Cria uma matriz com as possíveis respostas para cada pergunta, e em ordem
    # É visível, pela tabela de pesos, que é possível relacionar peso ao índice,
    # Ex: algo no índicie 0 também tem peso 0. Usei isso para a lógica.
    MatrizBase = [
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
                possiveisRespostas = MatrizBase[respostaIndex-1]

                for respIndex in range(len(possiveisRespostas)):
                    if resposta == possiveisRespostas[respIndex]: # Verifica se a resposta coincide com o valor naquele índice
                        scoreIndividual += respIndex # Soma o índice (peso) ao score

            listaScores.append([individuoIndex, scoreIndividual])

    return listaScores