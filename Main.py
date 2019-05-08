import numpy as np
import random 
import matplotlib.pyplot as plt
import math 


def leituraDados (localArquivo):
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
    
    e = math.exp (ai * (tetaAlunoj-bi))
    
    probAcerto =  ( e ) / (1 + e)
    
    return probAcerto



tetaDoAluno = [-1.0,-0.5,0.0,0.5,1.0]
dadosQuestoes = leituraDados('questoes.txt')
print (probabilidadeAcertoAlunoJQuestaoI(10,1))
