from Node import *

class Grafo:
    adj = {}
    raiz = None

    def __init__(self, state):
        self.raiz = Node(0, state)
        self.adj[str(self.raiz)] = []
        self.adj[str(self.raiz)].append()

    def createAdj(self, nodeFather, nodeSon):
        if not str(nodeFather) in self.adj:
            self.adj[str(nodeFather)] = []
        self.adj[str(nodeFather)].append(nodeSon)

