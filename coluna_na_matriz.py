"""Programa que retorna a soma ou a média de determinada coluna de uma matriz - Uri-1182"""


def coluna_na_matriz(C, T):
    matriz = (
        (0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 2.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 3.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 4.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 5.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 6.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 7.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 8.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 9.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 10.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 11.0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 12.0, 0, 0, 0, 0, 0, 0)
    )

    def soma_da_coluna(C):
        soma_coluna = 0
        for i in range(len(matriz)):
            for coluna in matriz[i]:
                if coluna == matriz[i][C]:
                    soma_coluna += coluna
        return soma_coluna

    if T == 'M':
        resp = soma_da_coluna(C) / 12

    elif T == 'S':
        resp = soma_da_coluna(C)

    return resp


print(f"{coluna_na_matriz(5, 'M'):.1f}")
print(coluna_na_matriz(5, 'S'))
