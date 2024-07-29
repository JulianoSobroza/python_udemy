#50. Parte 1: Variáveis, constantes e complexidade de código
"""
No python escreve-se com letras maiúsculas as variáveis
que não receberão outros valores (que não mudarão)

"""

velocidade = int(input('Diga a velocidade: ')) # velocidade do carro
local_carro = int(input('Diga o local: ')) #local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # raio que o radar pega

vel_q_o_carro_cruzou_radar_1 = velocidade > RADAR_1

if vel_q_o_carro_cruzou_radar_1:
    print('Passou da velocidade')
else:
    print()     
if 99 >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE1) and \
        vel_q_o_carro_cruzou_radar_1:
    print('Foi multado')
