#Aluno: Pedro Vinícius da Silva Ribeiro
#Matricula: 2019033903

class TreeNode:
    #definição da estrutura básica da arvore
    def __init__(self,data, left = None, right = None):
        self.value = data
        self.left = left
        self.right = right
class FindSum:
    #funcao que vai somar todas as chaves
    def recurse(self,node):
        value = node.value #variavel que irá salvar o valor do nodo
        if node.left:
            value += self.recurse(node.left) #soma os nodos da esquerda
        if node.right:
            value += self.recurse(node.right) #soma os nodos da direita
        return value
    def solve(self,root):
        #funcao para a verificação da raiz
        if not root:
            return 0
        return self.recurse(root)
#setar a arvore e printar a saida

total = FindSum()
root = TreeNode(2)
root.right = TreeNode(3)
root.left = TreeNode(4)
root.left.right = TreeNode(6)
root.left.left = TreeNode(5)

#print do total da saida
saida = total.solve(root)
print(f'A soma total de chaves e: {total.solve(root)}')
