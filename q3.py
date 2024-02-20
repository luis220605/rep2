def ePar(n):
    if(n%2 == 0):
        return True
    else:
        return False

n1 = int(input('Digite um número par: '))
b1 = ePar(n1)
n2 = int(input('Digite outro número par: '))
b2 = ePar(n2)
if(b1 and b2):
    if(ePar(n1*n2)):
        print('a afirmação é correta')
    else:
        print('foi encontrado um contra-exemplo')
else:
    print('ao menos um dos números é impar')