class Node:
    def __init__(self, initJ, state, condition, j, level, m, n, k):
        self.state=state
        # print(state)
        self.condition=condition
        self.children=[]
        self.j=j
        self.level=level
        self.score=self.test_score(initJ, m, n, k)
        if(self.score==None):
            self.play(initJ, m, n, k)
    def __str__(self):
        return str(self.state)
    def empty(self):
        _empty=[]
        for i in range(len(self.state)):
            if(self.state[i]=='0'):
                _empty.append(i)
        return _empty
    def play(self, initJ, m, n, k):
        _empty=self.empty()
        for i in _empty:
            newState=self.state[:]
            newState[i]=str(self.j)
            self.children.append(Node(initJ, newState, -self.condition, -self.j, self.level+1, m, n, k))
    def diagonalNormal(self, jogador, inicialI, inicialJ, m, n, k): # Verifica vitoria na diagonal
        cont = 0

        for j in range(n):
            if (inicialI + j) < m and (j+inicialJ) < n:
                if self.state[((inicialI+j)*n)+j+inicialJ] == str(jogador):
                    cont += 1
                else:
                    cont = 0
                if cont == k:
                    return True
            else:
                break

        return False

    def diagonalInversa(self, jogador, inicialI, inicialJ, m, n, k): # Verifica vitoria na diagonal ao contrario
        cont = 0
        while inicialI < m and inicialJ >= 0:
            if self.state[(inicialI*n)+inicialJ] == str(jogador):
                cont += 1
            else:
                cont = 0
            if cont == k:
                return True

            inicialI += 1
            inicialJ -= 1

        return False

    def winDiagonal(self, jogador, m, n, k): # Verifica vitoria em dois tipos de diagonais
        for i in range(n): # Oscila a posicao inicial na Linha
            if self.diagonalNormal(jogador, 0, i, m, n, k):
                return True

        for i in range(m): # Oscila a posicao inicial na Coluna
            if self.diagonalNormal(jogador, i, 0, m, n, k):
                return True

        for i in range(m): # Oscila a posicao inicial na Linha e na Coluna
            for j in range(n-1, -1, -1):
                if self.diagonalInversa(jogador, i, j, m, n, k):
                    return True

        return False

    def verificaEmpate(self): # Verifica empate
        if '0' in self.state: # Caso possua algum zero nao foi empate
            return False

        return True # Por conta da posicao onde eh chamada pode apenas retornar Ture caso o self.state nao possua nenhum zero

    def winHorizontal(self, jogador, m, n, k): # Percorre e procura vitoria na horizontal do self.state
        for i in range(m):
            cont = 0
            for j in range(n):
                if self.state[(i*n)+j] == str(jogador):
                    cont += 1
                else:
                    cont = 0
                if cont == k:
                    return True

        return False

    def winVertical(self, jogador, m, n, k): # Percorre e procura vitoria na vertical do self.state
        for i in range(n):
            cont = 0
            for j in range(m):
                if self.state[(j*n)+i] == str(jogador):
                    cont += 1
                else:
                    cont = 0
                if cont == k:
                    return True

        return False

    def test_score(self, initJ, m, n, k): # determina chamando outras funcoes qual o valor de um self.state
        j2 = 0

        if initJ == 1:
            j2 = -1
        else:
            j2 = 1

        if self.winDiagonal(initJ, m, n, k) or self.winHorizontal(initJ, m, n, k) or self.winVertical(initJ, m, n, k):
            return 1 # Jogador do primeiro movimento ganhou
        elif self.winDiagonal(j2, m, n, k) or self.winHorizontal(j2, m, n, k) or self.winVertical(j2, m, n, k):
            return -1 # Jogador do primeiro movimento perdeu
        elif self.verificaEmpate():
            return 0 # Empate entre os jogadores
        else:
            return None # Ainda existem movimentos possiveis
    def minimax(self):
        if(self.score!=None):
            return self.score
        else:
            scores=[]
            for i in self.children:
                scores.append(i.minimax())
                if(scores[-1]==1 and self.condition==1):
                    self.score=1
                    return self.score
                elif(scores[-1]==-1 and self.condition==-1):
                    self.score=-1
                    return self.score
            if(self.condition==1):
                self.score=max(scores)
                return max(scores)
            else:
                self.score=min(scores)
                return min(scores)

    def make_the_move(self):
        self.score=self.minimax()
        print(self.score)
        # print(self.score)
        for i in self.children:
            if(i.score == self.score):
                return i.state
