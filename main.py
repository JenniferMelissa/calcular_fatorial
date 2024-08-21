#recursividade
#é uma coisa que chama ela mesma
#algo dentro de outra coisa
#é executado um numero finito de vezes mas nao sabemos quanto


#funcao fatorial
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
        #esta chamando a funcao dentro dele, ele executa a funcao e o valor executado da 2 vez, é o valor menos 1, e executa ate que o valor chegue no 0
       


#programa principal
if __name__ == '__main__':
    try:
        n = int(input('Informe um numero inteiro postivo: '))
        
        if n >= 0:
            print(f'O fatorial de {n} é {fatorial(n)}.')
        else:
            print(f'Não existe fatorial de {n}.')
    except:
        print('Não foi possível calcular o fatorial.')

