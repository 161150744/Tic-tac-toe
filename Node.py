class Node:
    state = str('')
    cost = 0
    sons = []
    result = 0

    def __init__(self, m, n, j, k, state, cost):
        self.cost = int(cost)
        self.state = state
        self.result = self.resultTest(int(m), int(n), int(j), int(k))

    def __str__(self):
        return self.state
    
    def addSon(self, node):
        self.sons.append(node)

    def vertical(self, m, n, jogador, k):
        x = 0
        o = 0
        winner = 0
        zeros = 0
        for j in range(n):
            x = 0
            o = 0
            if winner == 0:
                for i in range(m):
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
        elif int(winner) == jogador:
            return 1
        else:
            return -1

    def horizontal(self, m, n, jogador, k):
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
        elif int(winner) == jogador:
            return 1
        else:
            return -1

    def diagonal1(self, m, n, jogador, k):
        x = 0
        o = 0
        winner = 0
        zeros = 0
        for g in range(m):
            i = g
            j = 0
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
        for g in range(n):
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
        elif int(winner) == jogador:
            return 1
        else:
            return -1

    def diagonal2(self, m, n, jogador, k):
        pass
        # x = 0
        # o = 0
        # winner = 0
        # zeros = 0
        # for g in range(m):
        #     i = g
        #     j = 0
        #     x = 0
        #     o = 0
        #     while(i < m and j < n):
        #         if winner == 0:
        #             if(self.state[i*n+j] == '0'):
        #                 zeros += 1
        #                 x = 0
        #                 o = 0
        #             elif(self.state[i*n+j] == '1'):
        #                 x += 1
        #                 o = 0
        #             elif(self.state[i*n+j] == '2'):
        #                 x = 0
        #                 o += 1
        #             if(x == k):
        #                 winner = 1
        #                 break
        #             elif(o == k):
        #                 winner = 2
        #                 break
        #         i += 1
        #         j += 1
        # for g in range(n):
        #     i = 0
        #     j = g
        #     x = 0
        #     o = 0
        #     while(i < m and j < n):
        #         if winner == 0:
        #             if(self.state[i*n+j] == '0'):
        #                 zeros += 1
        #                 x = 0
        #                 o = 0
        #             elif(self.state[i*n+j] == '1'):
        #                 x += 1
        #                 o = 0
        #             elif(self.state[i*n+j] == '2'):
        #                 x = 0
        #                 o += 1
        #             if(x == k):
        #                 winner = 1
        #                 break
        #             elif(o == k):
        #                 winner = 2
        #                 break
        #         i += 1
        #         j += 1
        # if winner == 0 and zeros > 0:
        #     return None
        # elif winner == 0 and zeros == 0:
        #     return 0
        # elif int(winner) == jogador:
        #     return 1
        # else:
        #     return -1

    def resultTest(self, m, n, j, k):
        #{-1 : defeat, 0 : draw, 1 : victory, None : nothing}
        return self.diagonal2(m, n, j, k)