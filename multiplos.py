def numeros_multiplos(a, b):
    if b > a:
        if b % a == 0:
            resposta = 'sao multiplos'
        else:
            resposta = 'nao sao multiplos'
    elif a > b:
        if a % b == 0:
            resposta = 'sao multiplos'
        else:
            resposta = 'nao sao multiplos'

    return resposta


if __name__ == '__main__':
    a = 4
    b = 8
    print(numeros_multiplos(a, b))
