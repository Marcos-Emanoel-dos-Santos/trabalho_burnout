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

    scoreIndividual = 0

    for i in range(len(matriz)):
        linha = matriz[i] # Assim posso utilizar tanto o índice diretamente quanto o conteúdo da matriz naquele índice

        for colunaIndex in range(1, len(linha)): # Itera sobre cada coluna de cada linha da matriz passada como parâmetro
            respostaUsuario = linha[colunaIndex]

            for VetorRespostas in MatrizBase[colunaIndex-1]:
                for possivelRespostaIndex in range(len(VetorRespostas)): # Para cada resposta armazenada em cada linha da MatrizBase:
                    if respostaUsuario == VetorRespostas[possivelRespostaIndex]:
                        scoreIndividual += possivelRespostaIndex # Soma ao scoreIndividual de acordo com o índice (que equivale ao peso) de cada resposta
        if len(linha) == 10 and i == 0:
            linha.append("Score individual")
        elif len(linha) == 10:
            linha.append(scoreIndividual)