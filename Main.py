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


def probabilidadeAcertoAlunoJQuestaoI(questao, aluno):
    ai = float(dadosQuestoes[questao - 1][0])
    bi = float(dadosQuestoes[questao - 1][1])
    tetaAlunoj = tetaDoAluno[aluno - 1]
    e = math.e
    numerador = math.exp(ai * (tetaAlunoj - bi))

    probAcerto = (numerador) / (1 + numerador)
    return probAcerto


def CriaProva(tamanho):
    return random.sample(range(1, 101), tamanho)


tetaDoAluno = [-1.0, -0.5, 0.0, 0.5, 1.0]
tamanho_prova = [10, 20, 50, 100]

dadosQuestoes = leituraDados('questoes.txt')

aluno1 = []
aluno2 = []
aluno3 = []
aluno4 = []
aluno5 = []
score_aluno = np.zeros(5)
score_final = np.zeros(5)

iteracoes = 5000
for a in range(0, len(tamanho_prova)):
    for cont in range(0, iteracoes):
        provacriada = (CriaProva(tamanho_prova[a]))
        score_aluno = np.zeros(5)
        for cont in range(0, tamanho_prova[a]):
            aluno1.append(probabilidadeAcertoAlunoJQuestaoI(provacriada[cont], 1))
            aluno2.append(probabilidadeAcertoAlunoJQuestaoI(provacriada[cont], 2))
            aluno3.append(probabilidadeAcertoAlunoJQuestaoI(provacriada[cont], 3))
            aluno4.append(probabilidadeAcertoAlunoJQuestaoI(provacriada[cont], 4))
            aluno5.append(probabilidadeAcertoAlunoJQuestaoI(provacriada[cont], 5))

        for i in range(0, tamanho_prova[a]):
            score_aluno[0] += np.random.choice([0, 1], p=[1 - aluno1[i], aluno1[i]])
            score_aluno[1] += np.random.choice([0, 1], p=[1 - aluno2[i], aluno2[i]])
            score_aluno[2] += np.random.choice([0, 1], p=[1 - aluno3[i], aluno3[i]])
            score_aluno[3] += np.random.choice([0, 1], p=[1 - aluno4[i], aluno4[i]])
            score_aluno[4] += np.random.choice([0, 1], p=[1 - aluno5[i], aluno5[i]])
        indice_max = np.argmax(score_aluno)
        score_final[indice_max] += 1
    print "Prova de",tamanho_prova[a],"questoes"
    print (score_final)
    print "-------------------------------------"