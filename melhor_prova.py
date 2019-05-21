from random import randint
from funcoes import *

def calcula_diferenca(score_5, score_4, tamanho):
    return (score_5/tamanho) - (score_4/tamanho)

tetas = [-1.0, -0.5, 0.0, 0.5, 1.0]
dados = leitura_dados('questoes.txt')
qtd_interacoes = 10000000
aluno5 = []
aluno4 = []

for tamanho_prova in [10, 20, 50]:
    melhor_prova = []
    maior_diferenca = 0
    
    for i in range(0, qtd_interacoes):
        score_aluno_5 = 0
        score_aluno_4 = 0
        
        prova = cria_prova(tamanho_prova)
        
        for questao in prova:
            score_aluno_5 = score_aluno_5 + probabilidade_acerto_aluno_j_questao_i(tetas, dados, questao, 5)
            score_aluno_4 = score_aluno_4 + probabilidade_acerto_aluno_j_questao_i(tetas, dados, questao, 4)
        
        diferenca = calcula_diferenca(score_aluno_5, score_aluno_4, tamanho_prova)
        if (diferenca > maior_diferenca):
            maior_diferenca = diferenca
            melhor_prova = prova
    
    melhor_prova.sort()
    for questao in melhor_prova:
        print(questao, end=' ')
    print()
    
    for a in range(1, 5):
        score_a = 0
        score_5 = 0
        for q in melhor_prova:
            score_a = score_a + probabilidade_acerto_aluno_j_questao_i(tetas, dados, q, a);
            score_5 = score_5 + probabilidade_acerto_aluno_j_questao_i(tetas, dados, q, 5);
        print(calcula_diferenca(score_5, score_a, tamanho_prova), end=' ')
    print()