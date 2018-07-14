# Guilherme Neri Bustamante Sá 161150744
# O algoritmo feito é uma tentativa de realizar o min max com poda
# O algoritmo tenta buscar a melhor posição para jogar
# A partir da raiz, são gerados os filhos ate que eles encontrem um resultado
# apos encontrar um resultado, podas são realizadas para diminuir o espaço de busca da melhor solução
# a arvore gerada tem um limite de nivel igual a 16


from Tree import Tree
import sys

def getArgs():#funcao que pega os argumentos do terminal
    listArgs = []#armazena a lista de argumentos
    for param in sys.argv:
        listArgs.append(param)
    return listArgs#retorna a lista de argumentos

def main():
    args = getArgs()
    game = Tree(args[1], args[2], args[3], args[4], args[5:])#cria o objeto tree com os parametros passados (m, n, j, k, estado)
    l = game.play()#novo estado gerado pelo algoritmo
    g = args[5:]#estado antigo
    for i in range(len(l)):
        if(l[i] != g[i]):#acha a posição diferente
            print ("{1} {0}".format(i%int(args[2]),int((i - i%int(args[2]))/int(args[1]))))

if __name__ == '__main__':
    main()