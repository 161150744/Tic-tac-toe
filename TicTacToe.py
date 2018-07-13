from Tree import Tree
import sys

def getArgs():
    listArgs = []
    for param in sys.argv:
        listArgs.append(param)
    return listArgs

def main():
    args = getArgs()
    game = Tree(args[1], args[2], args[3], args[4], args[5:])
    print(game.play())

if __name__ == '__main__':
    main()