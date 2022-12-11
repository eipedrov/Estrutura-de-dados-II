## ARVORE BINARIA 
## PEDRO VINICIUS 
## MATRICULA: 2019033903

# Estrutura do nó

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def insertNode(root, value):
    if root is None: #verificação se nulo
        return Node(value)
    else:
        if value < root.value: #valores menores que a raiz a esquerda
            root.left = insertNode(root.left, value) #comparação do valor com a raiz
        elif value > root.value:#valores menores que a raiz a direita
            root.right = insertNode(root.right, value)#comparação do valor com a raiz
    return root

# Função de imrpessão da arvore

def printTree(root, level=0):
    if root is not None:
        printTree(root.right, level+1)
        print(' ' * 4*level + '->' + str(root.value))
        printTree(root.left, level+1)

# FUNÇÕES DO EXERCÍCIO 
# MINIMO
# função para achar o menor valor
# que será o nó mais a esquerda
def findMin(root):
    if root is None: #Verifica se nulo
        return None
    while root.left != None:# O ultimo nó aponta pra nulo
        root = root.left
    return root

# MAXIMO
# função para achar o maior valor
# que será o nó mais a direita
def findMax(root):
    if root is None: #Verifica se nulo
        return None
    while root.right != None:# O ultimo nó aponta pra nulo
        root = root.right
    return root

# ALTURA
# função para achar a altura de uma arvore
# formula dada em aula = h(x)=MAX(h(x*left), h(x*right))+1
def findHeight(root):
  if root is None: #verificação se nulo
    return -1 #quando um nó é vazio o seu valor é -1 (VERIFICAR SE DA CERTO)
  leftH = findHeight(root.left)
  rightH = findHeight(root.right)
  return max(leftH, rightH) + 1 #implementação da formula

# REMOÇÃO
# Função de remoção 
# a função de remoção possui 3 condições
# no unico, no com um filho, no com mais de um filho
# o terceiro caso e resolvido usando os 2 anteriores

def deleteNode(root, value):
  if root is None: return None #verificação se nulo
  elif value < root.value:
    root.left = deleteNode(root.left, value)
  elif value > root.value:
    root.right = deleteNode(root.right, value)
  else:
    # Caso 1: condição de nó unico (sem filhos, folha)
    if root.left and root.right is None:
      root = None
    # Caso 2: condição de nó com um filho
    # remoção pela esquerda
    elif root.left is None:
      temp = root # variavel temporaria para armazenar o valore que sera substituido
      root = root.right
      temp = None  
    # remoção pela esquerda
    elif root.right is None:
      temp = root # variavel temporaria para armazenar o valore que sera substituido
      root = root.left
      temp = None  
    # Caso 3: Condição de nó com dois filhos
    else:
      minNode = findMin(root.right)
      root.value = minNode.value
      root.right = deleteNode(root.right, minNode.value)
  return root


# SETING DA ARVORE
root = None
root = insertNode(root, 10)
root = insertNode(root, 5)
root = insertNode(root, 2)
root = insertNode(root, 35)
root = insertNode(root, 8)
root = insertNode(root, 40)
root = insertNode(root, 38)
root = insertNode(root, 51)
root = insertNode(root, 9)

#IMPRESSÕES E TESTES

print("----------------------------")
printTree(root)
print("----------------------------")
print("Min: ", findMin(root).value)
print("----------------------------")
print("Max: ", findMax(root).value)
print("----------------------------")
print("Altura: ", findHeight(root))
print("----------------------------")
deleteNode(root, 9)
printTree(root)
