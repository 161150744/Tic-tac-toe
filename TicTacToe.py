# Guilherme Neri Bustamante Sá 161150744
# O algoritmo feito é uma tentativa de realizar o min max com poda
# O algoritmo tenta buscar a melhor posição para jogar
# A partir da raiz, são gerados os filhos ate que eles encontrem um resultado
# apos encontrar um resultado, podas são realizadas para diminuir o espaço de busca da melhor solução
# a arvore gerada tem um limite de nivel igual a 16


from Node import Node
import sys

def show(state, m, n):
    for j in range(n):
        print('\t{}'.format(j), end='')
    print()
    print()
    print()
    for i in range(m):
        print(i, end='')
        for j in range(n):
            if(state[i*n+j] == '-1'):
                print('\to', end='')
            elif(state[i*n+j] == '1'):
                print('\tx', end='')
            elif(state[i*n+j] == '0'):
                print('\t+', end='')
        print()

def main(args):
    l=0
    c=0
    state=args[4:]
    if(int(args[2])==-1):
        while(l>=0 and c>=0):
            show(state, int(args[0]), int(args[1]))
            l=int(input('\nnumero da linha '))
            c=int(input('\nnumero da coluna '))
            state[l*int(args[1])+c]='1'
            game = Node(int(args[2]), state, 1, int(args[2]), 0, int(args[0]), int(args[1]), int(args[3]))
            state=game.make_the_move()
    else:
        while(l>=0 and c>=0):
            game = Node(int(args[2]), state, 1, int(args[2]), 0, int(args[0]), int(args[1]), int(args[3]))
            state=game.make_the_move()
            show(state, int(args[0]), int(args[1]))
            l=int(input('\nnumero da linha '))
            c=int(input('\nnumero da coluna '))
            state[l*int(args[1])+c]='-1'

if __name__ == '__main__':
    main(sys.argv[1:])