"""Programa que retorna a soma ou a média de determinada linha de uma matriz - Uri-1181"""
def linha_na_matriz(L, T):
    matriz = (
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (2.7, 2.5, 2.3, 2.0, 5.0, 6.3, 3.0, 6.2, 3.6, 10.3, 8.2, 12.6),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    )

    def soma_linha_matriz(L):
        soma_linha = 0
        for linha in matriz[L]:
            soma_linha += linha
        return soma_linha

    if T == 'S':
        resp = soma_linha_matriz(L)

    elif T == 'M':
        resp = soma_linha_matriz(L) / 12

    return resp


print(f"{linha_na_matriz(2, 'S'):.1f}")
print(f"{linha_na_matriz(5, 'S'):.1f}")
print(f"{linha_na_matriz(5, 'M'):.1f}")
print(f"{linha_na_matriz(7, 'M'):.1f}")
