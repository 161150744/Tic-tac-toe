class Node:
    state = str('')
    cost = 0

    def __init__(self, cost, state):
        self.cost = cost
        self.state = state

    def __str__(self):
        return self.state