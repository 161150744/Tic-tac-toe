from Node import *

class Tree:
    def __init__(self, m, n, j, k, state):
        self.dic = {}#dicionario para não gerar estados iguais
        self.heap = []#pilha
        self.raiz = Node(m, n, j, k, state, 0, None)#nodo raiz
        self.dic[str(state)] = True#adiciona o primeiro estado no dicionario para não gera-lo novamente
        self.m = int(m)#numero de linhas
        self.n = int(n)#numero de colunas
        self.j = int(j)#jogador
        self.k = int(k)#tamanho da sequencia

    def generateSon(self, node):#gera os filhos do nodo
        gamer = 0
        if(node.cost%2 == 0):#se o nivel atual for multiplo de 2, então é a vez do jogador passado pelo terminal
            gamer = self.j
        else:#se não, é a vez do outro jogador
            gamer = 3 - self.j
        for i in range(len(node.state)):#percorre o vetor estado
            if(node.state[i] == '0'):#acha uma posição jogavel
                newState = node.state.copy()#copia o estado
                newState[i] = str(gamer)#joga na posição jogavel no novo estado
                if not str(newState) in self.dic:#se o estado ja não existe no dicionario
                    self.dic[str(newState)] = True#adiciona no dicionario
                    node.addSon(self.m, self.n, self.j, self.k, newState)#adiciona no nodo

    def addSonToHeap(self, node):#adiciona os filhos do nodo na heap
        for i in node.sons:
            self.heap.append(i)

    def seeMin(self, node):#olha o estado MIN anterior
        Min = node.father.father
        if Min.result != None and Min.result < node.result:#se o resultado do MIN anterior for menor que o estado do MIN mais abaixo, então chama a função de poda
            node.pruning(Min)#função de poda
            self.pruningAlphaBetha(Min)#chama a função para decidir se é MIN ou MAX

    def seeMax(self, node):#mesma coisa da função anterior, porém para MAX
        Max = node.father.father
        if Max.result != None and Max.result > node.result:
            node.pruning(Max)
            self.pruningAlphaBetha(Max)

    def pruningAlphaBetha(self, node):#decide se é MIM ou MAX
        if node.father != None and node.father.father != None:#testa se o pai é vazio e se o pai do pai é vazio
            level = node.cost % 2#verifica se é um estado de MIN ou MAX
            if level == 0:
                self.seeMax(node)#se for MAX, chama a função de MAX
            if level == 1:
                self.seeMin(node)#se for MIN, chama a função de MIN

    def play(self):#função para jogar o jogo e dicidir
        self.heap.append(self.raiz)#adiciona a raiz na heap
        now = None#inicia o nodo atual
        while(self.heap):#enquanto a heap não estiver vazia
            now = self.heap.pop()#o atual vai ser o ultimo da pilha (busca em profundidade)
            if now.cost > 15:#limita a altura da arvore em 16
                break
            if(now.result == None):#se o atual ainda não tiver um resultado, gera os filhos dele
                if(now.flag):#se ele ainda não foi podado
                    self.generateSon(now)#gera os filhos
                    self.addSonToHeap(now)#coloca os filhos da heap
            else:
                self.pruningAlphaBetha(now)#poda estados
        for i in range(len(self.raiz.sons)):#verifica se algum valor dos filhos é igual ou valor da raiz
            if(self.raiz.result == self.raiz.sons[i].result):
                return self.raiz.sons[i].state#se for, retorna
        return self.raiz.state#se não tiver, retorna a raiz


