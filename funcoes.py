def CalculaScoreIndividual(individuoDados):
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

    scoreIndividual = 0

    for respostaIndex in range(1, len(individuoDados)): # Para cada resposta dada por ele (o índice 0 não é resposta)
        resposta = individuoDados[respostaIndex]
        respostasPossiveis = MatrizBase[respostaIndex-1] # Cada índice da matriz parâmetro deve ser comparada com a MatrizBase começando em 0

        for respIndex in range(len(respostasPossiveis)): # Para cada índice de respostasPossiveis
            if resposta == respostasPossiveis[respIndex]: # Verifica se a resposta coincide com o valor naquele índice
                scoreIndividual += respIndex # Soma o índice (peso) ao score

    return scoreIndividual