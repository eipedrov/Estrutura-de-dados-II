### ----- ÁRVORE DE BUSCA BINÁRIA  ----- ###

# Estrutura do nó
class Node:
  def _init_(self, value=None):
    self.value = value
    self.left = None
    self.right = None

# Função de inserção
def insertNode(root, value):
  if root is None:
    return Node(value)
  else:
    if value < root.value:
      root.left = insertNode(root.left, value)
    elif value > root.value:
      root.right = insertNode(root.right, value)
  return root 
  

# PERCURSOS EM PROFUNDIDADE (DFS)
def preOrdem(root):
  if root:
    print(root.value, end=" ")
    preOrdem(root.left)
    preOrdem(root.right)

def inOrdem(root):
  if root:
    inOrdem(root.left)
    print(root.value, end=" ")
    inOrdem(root.right)

def posOrdem(root):
  if root:
    posOrdem(root.left)
    posOrdem(root.right)
    print(root.value, end=" ")
    

# PERCURSOS EM LARGURA (BFS)  
import queue
q = queue.Queue()

def levelOrder(root):
  if root is None: return None
  q.put(root)
  while not q.empty():
    current = q.queue[0]
    print(current.value, end=" ")
    if current.left is not None: q.put(current.left)
    if current.right is not None: q.put(current.right)
    q.get() 

# Função para imprimir mais "bonitinho"
def printTree(root, level=0):
  if root is not None:
    printTree(root.right, level+1)
    print(' ' *4*level + '->' +str(root.value))
    printTree(root.left, level+1)

# Outras funções    
def findMin(root):
  if root is None:
    return None
  while root.left != None:
    root = root.left
  return root
  
def findMax(root):
  if root is None:
    return None
  while root.right != None:
    root = root.right
  return root

def findHeight(root):
  if root is None:
    return -1
  leftH = findHeight(root.left)
  rightH = findHeight(root.right)
  return max(leftH, rightH) + 1

# Função de remoção  
def deleteNode(root, value):
  if root is None: return None
  elif value < root.value:
    root.left = deleteNode(root.left, value)
  elif value > root.value:
    root.right = deleteNode(root.right, value)
  else:
    # Caso 1: Nó folha
    if root.left and root.right is None:
      root = None
    # Caso 2: Nó tem um filho
    elif root.left is None:
      temp = root
      root = root.right
      temp = None  
    elif root.right is None:
      temp = root
      root = root.left
      temp = None  
    # Caso 3: Nó tem dois filhos
    else:
      minNode = findMin(root.right)
      root.value = minNode.value
      root.right = deleteNode(root.right, minNode.value)
  return root

# ------ Main --------
root = None
nums = [1, 2, 3]
for num in nums:
  root = insertNode(root, num)

printTree(root)
print("----------------------------")