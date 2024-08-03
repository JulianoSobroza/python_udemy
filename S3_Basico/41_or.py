"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Digite a senha: ')

senha_permitida = '456'

if entrada == 'E' or 'e' and senha_digitada == senha_permitida:
    print('Acesso liberado')
else:
    print('Sair')

"""

"""
# Avaliação de curto circuito


print(True or True or 0 or 0)

"""

senha = input('Senha: ') or 'Sem senha'
print(senha)
