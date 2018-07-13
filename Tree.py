from Node import *

class Tree:
    raiz = None
    m = 0
    n = 0
    j = 0
    k = 0

    def __init__(self, m, n, j, k, state):
        self.raiz = Node(m, n, j, k, state, 0, None)
        self.m = int(m)
        self.n = int(n)
        self.j = int(j)
        self.k = int(k)

    def play(self):
        pass

