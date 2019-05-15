import numpy as np
import random 
import matplotlib.pyplot as plt
import math 


def leituraDados(localArquivo):
    arquivo = open(localArquivo, 'r')
    dados = []
    for linha in arquivo:
        aux = linha.split()
        aux[0] = float(aux[0])
        aux[1] = float(aux[1])
        dados.append(aux)
    arquivo.close()
    return dados

def probabilidadeAcertoAlunoJQuestaoI(questao,aluno):
    
    ai = float(dadosQuestoes[questao-1][0])
    bi = float(dadosQuestoes[questao-1][1])
    tetaAlunoj = tetaDoAluno[aluno-1]
    e = math.e
    numerador = math.exp(ai * (tetaAlunoj-bi))

    probAcerto = (numerador) / (1 + numerador)
    return probAcerto


def CriaProva (tamanho):
    prova = []
    while len(prova) < tamanho:
        from random import randint
        QuestaoSorteada = (randint(1, 100))
        if QuestaoSorteada not in prova:
            prova.append(QuestaoSorteada)
    return prova




tetaDoAluno = [-1.0,-0.5,0.0,0.5,1.0]
TamanhoProva = [10,20,50,100]

dadosQuestoes = leituraDados('questoes.txt')

aluno1 = []
aluno2 = []
score_aluno1 = 0
score_aluno2 = 0
tamanho_escolhido = 20
iteracoes = 1

for cont in range(0,iteracoes):
    provacriada = (CriaProva(tamanho_escolhido))
    for cont in range(0, tamanho_escolhido):
        aluno1.append(probabilidadeAcertoAlunoJQuestaoI(provacriada[cont], 5))
        aluno2.append(probabilidadeAcertoAlunoJQuestaoI(provacriada[cont], 4))
        score_aluno1 = score_aluno1 + aluno1[cont]
        score_aluno2 = score_aluno2 + aluno2[cont]

print(score_aluno1/tamanho_escolhido)
print(score_aluno2/tamanho_escolhido)
