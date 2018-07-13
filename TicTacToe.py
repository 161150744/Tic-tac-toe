from Tree import *
import sys

def getArgs():
    listArgs = []
    for param in sys.argv:
        listArgs.append(param)
    return listArgs

def main():
    args = getArgs()
    game = Node(args[1], args[2], args[3], args[4], args[5:], 0)
    print(game.result)

if __name__ == '__main__':
    main()