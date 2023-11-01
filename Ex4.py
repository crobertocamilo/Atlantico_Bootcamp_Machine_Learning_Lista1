def ordenar_lista(dados):

    lista_ordenada = sorted(dados, key=lambda pessoa: pessoa[0])
    return lista_ordenada

dados = [('Felipe', 15), ('Tiago', 35), ('Reinaldo', 38), ('Karine', 46)]

dados_ordenados = ordenar_lista(dados)

print('\nEm ordem alfabética de nome:')
for item in dados_ordenados:
    print(item)