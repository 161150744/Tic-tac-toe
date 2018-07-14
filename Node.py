class Node:
    def __init__(self, m, n, j, k, state, cost, father):
        self.cost = int(cost)#nivel na arvore
        self.state = state#esatdo
        self.result = self.resultTest(int(m), int(n), int(j), int(k))# testa se o estado é final e retorna um resultado
        self.father = father#pai
        self.sons = []#lista de filhos
        self.MinMax()#decide se é MIN ou MAX
        self.flag = True#flag de poda

    def __str__(self):
        return self.state#retorna um estado
    
    def addSon(self, m, n, j, k, state):#adiciona um filho na lista de filhos
        self.sons.append(Node(m, n, j, k, state, self.cost+1, self))

    def vertical(self, m, n, gamer, k):#função que verifica se alguem ganhou na vertical
        x = 0#numro de x's
        o = 0#numero de o's
        winner = 0#quem ganhou
        zeros = 0#numero de zeros
        for j in range(n):#percorre o j no tamanho maximo da linha
            x = 0#volta o numero de x's para 0
            o = 0#volta o numero de o's para 0
            if winner == 0:#se ainda não tiver um vencedor
                for i in range(m):#percorre o i no tamanho maximo da coluna
                    if(self.state[i*n+j] == '0'):#se a posição atual for um 0
                        zeros += 1#aumenta o numero de zeros
                        x = 0#zera o numero de x's em sequencia
                        o = 0#zera o numero de o's em sequencia
                    elif(self.state[i*n+j] == '1'):#se a posição atual for um 1
                        x += 1#aumenta o numero de x's em sequencia
                        o = 0#zera o numero de o's em sequencia
                    elif(self.state[i*n+j] == '2'):#se a posição atual for um 2
                        x = 0#zera o numero de x's em sequencia
                        o += 1#aumenta o numero de o's em sequencia
                    if(x == k):#se o numero de x's em sequencia for igual a sequencia
                        winner = 1#o ganhador é o numero 1
                        break#para
                    elif(o == k):#se o numero de o's em sequencia for igual a sequencia
                        winner = 2#o ganhador é o 2
                        break#para
        if winner == 0 and zeros > 0:#se niinguem ganhou, porem ainda existem zeros, retorna None
            return None
        elif winner == 0 and zeros == 0:#se ninguem ganhou, porem não existe mais zeros, retorna 0
            return 0
        elif int(winner) == gamer:#se o jogador ganhou, retorna +1
            return 1
        else:#se o jogador não ganhou, retorna -1
            return -1

    def horizontal(self, m, n, gamer, k):#mesma coisa da funcao anterior, porem percorrendo a coluna primeiro e depois a linha
        x = 0
        o = 0
        winner = 0
        zeros = 0
        for i in range(m):
            x = 0
            o = 0
            if winner == 0:
                for j in range(n):
                    if(self.state[i*n+j] == '0'):
                        zeros += 1
                        x = 0
                        o = 0
                    elif(self.state[i*n+j] == '1'):
                        x += 1
                        o = 0
                    elif(self.state[i*n+j] == '2'):
                        x = 0
                        o += 1
                    if(x == k):
                        winner = 1
                        break
                    elif(o == k):
                        winner = 2
                        break
        if winner == 0 and zeros > 0:
            return None
        elif winner == 0 and zeros == 0:
            return 0
        elif int(winner) == gamer:
            return 1
        else:
            return -1

    def diagonal1(self, m, n, gamer, k):#testa a diagonal direita, baixo
        x = 0
        o = 0
        winner = 0
        zeros = 0
        for g in range(m):#guarda a posição na coluna em que o teste atual vai começar para testar as dioganais acima da diagonal princiapal da matriz transposta
            i = g
            j = 0
            x = 0
            o = 0
            while(i < m and j < n):#aumenta i e j sem que eles passem do limite da matriz
                if winner == 0:
                    if(self.state[i*n+j] == '0'):#conta o numero de zeros
                        zeros += 1
                        x = 0
                        o = 0
                    elif(self.state[i*n+j] == '1'):#conta o numero de x's
                        x += 1
                        o = 0
                    elif(self.state[i*n+j] == '2'):#conta o numero de o's
                        x = 0
                        o += 1
                    if(x == k):#testa se o x venceu
                        winner = 1
                        break
                    elif(o == k):#testa se o o venceu
                        winner = 2
                        break
                i += 1
                j += 1
        for g in range(n):#termina os testes, abaixo da dioganal principal da matriz transposta
            i = 0
            j = g
            x = 0
            o = 0
            while(i < m and j < n):
                if winner == 0:
                    if(self.state[i*n+j] == '0'):
                        zeros += 1
                        x = 0
                        o = 0
                    elif(self.state[i*n+j] == '1'):
                        x += 1
                        o = 0
                    elif(self.state[i*n+j] == '2'):
                        x = 0
                        o += 1
                    if(x == k):
                        winner = 1
                        break
                    elif(o == k):
                        winner = 2
                        break
                i += 1
                j += 1
        if winner == 0 and zeros > 0:
            return None
        elif winner == 0 and zeros == 0:
            return 0
        elif int(winner) == gamer:
            return 1
        else:
            return -1

    def diagonal2(self, m, n, gamer, k):#testa a diagonal direita, cima
        x = 0
        o = 0
        winner = 0
        zeros = 0
        for g in range(m):#guarda a posição na coluna em que o teste atual vai começar para testar as dioganais acima da diagonal princiapal da matriz transposta
            i = g
            j = 0
            x = 0
            o = 0
            while(i >= 0 and j < n):#incrementa o j e decrementa o i sem passar dos limites da matriz
                if winner == 0:
                    if(self.state[i*n+j] == '0'):
                        zeros += 1
                        x = 0
                        o = 0
                    elif(self.state[i*n+j] == '1'):
                        x += 1
                        o = 0
                    elif(self.state[i*n+j] == '2'):
                        x = 0
                        o += 1
                    if(x == k):
                        winner = 1
                        break
                    elif(o == k):
                        winner = 2
                        break
                i -= 1
                j += 1
        for g in range(1, n):#termina os testes, abaixo da dioganal principal da matriz transposta
            i = m-1
            j = g
            x = 0
            o = 0
            while(i >= 0 and j < n):
                if winner == 0:
                    if(self.state[i*n+j] == '0'):
                        zeros += 1
                        x = 0
                        o = 0
                    elif(self.state[i*n+j] == '1'):
                        x += 1
                        o = 0
                    elif(self.state[i*n+j] == '2'):
                        x = 0
                        o += 1
                    if(x == k):
                        winner = 1
                        break
                    elif(o == k):
                        winner = 2
                        break
                i -= 1
                j += 1
        if winner == 0 and zeros > 0:
            return None
        elif winner == 0 and zeros == 0:
            return 0
        elif int(winner) == gamer:
            return 1
        else:
            return -1

    def resultTest(self, m, n, j, k):#testa o resultado (se ganhou, perdeu ou deu empate)
        #{-1 : defeat, 0 : draw, 1 : victory, None : nothing}
        possibilities = [self.vertical, self.horizontal, self.diagonal1, self.diagonal2]#lista de possibilidades para testar
        for p in possibilities:#percorre a lista de possibilidades
            if p(m, n, j, k) != None:#se perdeu, ganhou ou empatou, retorna o resultado
                return p(m, n, j, k)
        return None#se não, retorna none

    def max(self):#atualiza o valor do pai
        father = self.father
        Max = -1
        for i in father.sons:#percorre na lista de filhos do pai e procura o valor maximo para atualizar
            if i.result != None and i.result > Max:
                Max = i.result
        if(father.result == None):#se atualizar o valor, retorna verdadeiro
            father.result = Max
            return True
        if(father.result < Max):
            father.result = Max
            return True
        return False#se não atualizar retorna falso

    def min(self):#faz o mesmo que a função de cima, porem para o minimo
        father = self.father
        Min = 1
        for i in father.sons:
            if i.result != None and i.result < Min:
                Min = i.result
        if(father.result == None):
            father.result = Min
            return True
        elif(father.result > Min):
            father.result = Min
            return True
        return False

    def MinMax(self):#decide se é MIN ou MAX, e se o valor do pai for alterado, tenta atualizar o valor do pai do pai
        flag = False
        if self.result != None:
            if self.father != None:
                level = self.cost % 2
                if(level == 0):
                    flag = self.min()
                else:
                    flag = self.max()
                if flag:
                    self.father.MinMax()

    def setFather(self):#atualiza o resultado do pai
        self.father.result = self.result

    def pruning(self, node):#poda
        if self != node:
            for i in self.father.sons:#percorre os filhos do pai e faz a flag deles valer False
                i.flag = False
            self.father.pruning(node)
