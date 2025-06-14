# Matriz com resposta para cada item e o peso da pergunta. Obs: O peso de cada RESPOSTA corresponde ao seu índice.
# Uso: CalculaScoreIndividual(matriz, MatrizScore)
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

# Matriz com a solução para os problemas apresentados
# Uso: SugereMinimizacaoSintomas(MatrizMinimizacao)
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