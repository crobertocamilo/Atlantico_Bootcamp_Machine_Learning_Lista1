lista = [2, 8, 85, 17, 23, 65]
print(f'Lista original: {lista}')

#Dada uma lista, é possível encontrar seu menor e maior elementos, ordenando-a e a seguir pegando o primeiro [0] e o último valor da lista [-1], respectivamente:

lista.sort()
print(f'Lista ordenada: {lista} \nMenor elemento da lista: {lista[0]} \nMaior elemento da lista: {lista[-1]}')