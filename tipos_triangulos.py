# Função com o objetivo de auxiliar no teste do funcionamento da ordenação da linha 38 e 39
def ordena_lados(l1, l2, l3):
    """ordena os lados para verificar se forma triângulos"""
    lados = sorted([l1, l2, l3], reverse=True)
    global a, b, c
    a, b, c = lados
    return [a, b, c]


def triangulo_retangulo(a, b, c): return a ** 2 == b ** 2 + c ** 2


def nao_triangulo(a, b,  c): return a >= b + c


def triangulo_acutangulo(a, b, c): return a ** 2 < b ** 2 + c ** 2


def triangulo_obtusangulo(a, b, c): return a ** 2 > b ** 2 + c ** 2


def triangulo_equilatero(a, b, c): return b == a == c


def triangulo_isosceles(a, b, c): return a == b or a == c or b == c


TRIANGULOS = ['TRIANGULO RETANGULO',
              'NAO FORMA TRIANGULO',
              'TRIANGULO ACUTANGULO',
              'TRIANGULO ACUTANGULO EQUILATERO',
              'TRIANGULO ACUTANGULO ISOSCELES',
              'TRIANGULO OBTUSANGULO',
              'TRIANGULO OBTUSANGULO ISOSCELES'
              ]


def triangulos(l1, l2, l3):
    ordena_lados(l1, l2, l3)
    if triangulo_retangulo(a, b, c):

        tipo_triangulo = TRIANGULOS[0]

    elif nao_triangulo(a, b, c):

        tipo_triangulo = TRIANGULOS[1]

    elif triangulo_acutangulo(a, b, c):

        tipo_triangulo = TRIANGULOS[2]

        if triangulo_equilatero(a, b, c):

            tipo_triangulo = TRIANGULOS[3]

        elif triangulo_isosceles(a, b, c):

            tipo_triangulo = TRIANGULOS[4]

    elif triangulo_obtusangulo(a, b, c):

        tipo_triangulo = TRIANGULOS[5]

        if triangulo_isosceles(a, b, c):

            tipo_triangulo = TRIANGULOS[6]

    return tipo_triangulo


if __name__ == '__main__':

    print(triangulos(5.0, 7.0, 7.0))
    print(ordena_lados(5.0, 7.0, 7.0))
    print(triangulos(5.0, 7.0, 2.0))
    print(ordena_lados(5.0, 7.0, 2.0))
