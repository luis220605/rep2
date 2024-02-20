def eImpar(n):
    if((n-1)%2 == 0):
        return True
    else:
        return False

n = int(input('Digite um número: '))
b1 = eImpar(n)
b2 = eImpar(n**2)
if(b1 and b2):
    print('a afirmação é correta, pois {0} é um número impar e {1}, o quadrado de {0}, também'.format(n, n**2))
    exp = input
else:
    if(not b1):
        print('o número não é impar')
    else:
        print('foi encontrado um contra-exemplo')
