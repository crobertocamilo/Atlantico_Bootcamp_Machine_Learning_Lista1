def eh_primo(lista):

    lista_primos = []

    for item in lista:
        primo = True

        for n in range(2,item // 2):
            if item % n == 0:
                primo = False
                break

        if primo == True:
            lista_primos.append(item)

    return lista_primos

numeros = [2,3,6,8,9,11,13,17,25,26,33] 

lista_primos = eh_primo(numeros)

print(f'Lista de números informada: {numeros}')

if len(lista_primos) > 0:
    print(f'\nNa lista informada, são primos os números: {lista_primos}')
else:
    print('Não há números primos em na lista informada!')




