def diferenca(a, b):

    A = set(a)
    B = set(b)

    return (A - B).union(B - A)

a = [0, 1, 2, 3]
b = [3, 4, 5, 6]

a_diff_b = list(diferenca(a, b))

print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'\nElementos que estão em apenas uma das listas: {a_diff_b}')