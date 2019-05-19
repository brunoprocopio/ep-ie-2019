import math
from random import randint

def leitura_dados (local_arquivo):
    arquivo = open(local_arquivo, 'r')
    dados = []
    for linha in arquivo:
        aux = linha.split()
        aux[0] = float(aux[0])
        aux[1] = float(aux[1])
        dados.append(aux)
    arquivo.close()
    return dados
    
def probabilidade_acerto_aluno_j_questao_i(teta, mapa, questao, aluno):
    
    ai = float(mapa[questao-1][0])
    bi = float(mapa[questao-1][1])
    teta_aluno_j = teta[aluno-1]
    
    e = math.exp (ai * (teta_aluno_j-bi))
    prob_acerto =  ( e ) / (1 + e)
    
    return prob_acerto

def cria_prova(tamanho):
    prova = []
    while len(prova) < tamanho:
        questao = (randint(1, 100))
        if questao not in prova:
            prova.append(questao)
    return prova
