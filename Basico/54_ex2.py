"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

from datetime import datetime

# Obter a data e hora atual
data_hora_atual = datetime.now()

# Extrair as horas, minutos e segundos
horas = data_hora_atual.hour
minutos = data_hora_atual.minute
segundos = data_hora_atual.second

if 0 < horas <= 11:
    print('Bom dia. São {} horas e {} minutos.'.format(horas, minutos))
elif 12 < horas <= 17:
    print('Boa tarde. São {} horas e {} minutos.'.format(horas, minutos))
elif 18 < horas <= 23:
    print('Boa noite. São {} horas e {} minutos.'.format(horas, minutos))