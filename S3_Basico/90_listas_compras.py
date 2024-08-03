print( '[Lista de compras]')

lista_compras = ['Banana', 'Nescau']

while True:
    print("\nMenu:")
    print("[1] Adicionar item")
    print("[2] Remover item")
    print("[3] Listar itens")
    print("[4] Sair")

    try:
        opcao = int(input('Opção: '))

        match opcao:
            case 1: 
                item = input('Nome do item: ')
                lista_compras.append(item)
                print(f'Item {item} adicionado.')
            case 2: 
                indice_item = int(input('Indice do item: '))
                if 0 < indice_item <= len(lista_compras):
                    item_removido = lista_compras.pop(indice_item -1)
                    print(f'Item {item_removido} removido.')
                else:
                    print('Item indisponível')
            case 3:
                print('\n[Lista de compras]')
                for i, item, in enumerate(lista_compras):
                    print(f'[{i+1}] {item}')
            case _:
                print('\nOpção inválida')
    except ValueError:
        print('Não sei como chegar aqui')
