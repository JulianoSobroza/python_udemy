print(15*'▬' + ' CALCULADORA WHILE' + 15*'▬')
while True:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    operador = input('Operador +-*/: ')
    num1_float = 0
    num2_float = 0

    operadores_permitidos = '+-*/'
    numeros_validos = None

    try: 
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Digite um número válido')
        continue
 
    if operador not in operadores_permitidos:
        print('Digite um operador válido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    print('RESULTADO ↓↓↓↓')
    if operador == '+':
        print(num1_float + num2_float)
    elif operador == '-':
        print(num1_float - num2_float)
    elif operador == '*':
        print(num1_float * num2_float)
    elif operador == '/':
        print(num1_float / num2_float)


