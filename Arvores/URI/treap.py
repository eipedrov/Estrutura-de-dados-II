
# Aluno: Pedro Vinícius da Silva Ribeiro
# Matricula: 2019033903
# Disciplina: DCC405 - Estruturas de Dados II
# Professor: Acauan Ribeiro
# beecrowd: 1675 - Construção de Procura Binária de Heap

import sys

sys.setrecursionlimit(10**6)


class Treap(): #estrutura da treap
    def __init__(self, priority, label):
        self.priority = priority
        self.label = label
        self.left = None
        self.right = None


def rightRotate(root): #rotação simples a direita
    x = root.left
    y = x.right

    x.right = root
    root.left = y

    return x


def leftRotate(root): #rotação simples a esquerda
    x = root.right
    y = x.left

    x.left = root
    root.right = y

    return x

#inserção
def insert(root, priority, label): 
    if root is None: #verifica se nulo
        return Treap(priority, label)

    if label <= root.label:
        root.left = insert(root.left, priority, label) #se menor ou igual fazer rotação a esquerda de acordo com a prioridade

        if root.left.priority > root.priority: #se maior fazer rotação a direita de acordo com a prioridade
            root = rightRotate(root)
    else:
        root.right = insert(root.right, priority, label)#se igual fazer rotação a direita de acordo com a prioridade

        if root.right.priority > root.priority: #se maior ou igual fazer rotação a esquerda de acordo com a prioridade
            root = leftRotate(root)

    return root


def printTreap(root): #print da estrutura como e pedido no exercicio
    print("(", end="")

    if root.left is not None:
        printTreap(root.left)

    print("{}/{}".format(root.label, root.priority), end="")

    if root.right is not None:
        printTreap(root.right)

    print(")", end="")


def main():
    while True:
        values = input().split()

        if int(values[0]) == 0:
            break

        t = None

        for i in range(1, int(values[0]) + 1):
            t = insert(t, int(values[i].split("/")[1]),
                       values[i].split("/")[0])

        printTreap(t)
        print()


main()
