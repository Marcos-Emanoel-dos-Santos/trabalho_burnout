from dados_coletados import lista_respostas as dados
from funcoes import *

def perc(riscos, nivel):
    tot = len(riscos)
    qtd = sum(1 for p in riscos if p[1] == nivel)
    return round((qtd / tot) * 100, 2)

def atualiza(dados):
    scores = CalculaScoreIndividual(dados)
    return ClassificaNivelRisco(scores)

def imprime(riscos, dados):
    print("\nNOME - SCORE - RISCO")
    for p in riscos:
        nome = dados[p[0]][0]
        s = p[1]
        r = s if isinstance(s, str) else "?"
        print(f"{nome} - {s if isinstance(s, int) else '?'} - {r if isinstance(s, str) else '?'}")

print("=#="*10)
print("ANÁLISE DE RISCO DE BURNOUT")
print("PUCPR - Ciência da Computação")
print("=#="*10)

riscos = atualiza(dados)

while True:
    op = TelaAbertura()

    while op not in "1234567" or len(op) != 1:
        print("Opção inválida! Tente novamente.")
        op = TelaAbertura()

    op = int(op)
    print()

    if op == 1:
        SugereMinimizacaoSintomas()

    elif op == 2:
        nome = input("Nome da pessoa (ex: Pessoa_25): ")
        achou = False
        for i in range(1, len(dados)):
            if dados[i][0].lower() == nome.lower():
                score = CalculaScoreIndividual(dados)[i-1][1]
                risco = ClassificaNivelRisco([[i, score]])[0][1]
                print(f"\nScore: {score}")
                print(f"Risco: {risco}")
                achou = True
                break
        if not achou:
            print("Pessoa não encontrada.")

    elif op == 3:
        imprime(riscos, dados)

    elif op == 4:
        print(f"Risco BAIXO: {perc(riscos, 'baixo')}%")

    elif op == 5:
        print(f"Risco MODERADO: {perc(riscos, 'moderado')}%")

    elif op == 6:
        print(f"Risco ALTO: {perc(riscos, 'alto')}%")

    elif op == 7:
        print("Encerrando o programa.")
        break
