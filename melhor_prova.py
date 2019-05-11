# TODO escrever em arquivo
from funcoes import *

def le_x_questoes(questoes, qtd):
    a = []
    for i in range(1, qtd+1):
        a.append(questoes[-i][0])
    return a
        

tetas = [-1.0,-0.5,0.0,0.5,1.0]
dados = leitura_dados('questoes.txt')

map_dif = []

for questao in range(1, 101):
    p_5 = probabilidade_acerto_aluno_j_questao_i(tetas, dados, questao, 5)
    p_4 = probabilidade_acerto_aluno_j_questao_i(tetas, dados, questao, 4)
        
    dif = p_5 - p_4
    map_dif.append([questao, dif])
    
map_dif = sorted(map_dif, key=lambda questao: questao[1])

for i in [10, 20, 50]:
    questoes = le_x_questoes(map_dif, i)
    for q in questoes:
        print("{}".format(q), end=" ")
    # TODO calcular a probabilidade 
    print()
    print()

# for questao in range(1, 101):
#     print("{}".format(questao), end=" ")
#     for aluno in range(1, 6):
#         print("{}".format(probabilidade_acerto_aluno_j_questao_i(tetas, dados, questao, aluno)), end=" ")
#     print("")