#Aluno: Pedro Vinícius da Silva Ribeiro
#Matricula: 2019033903

class Node:
	def __init__(self, value, left = None, right = None):
		#definição da estrutura básica da arvore
		self.val = value
		self.left = left
		self.right = right
	
	def countSubTree(self, root, count):
		#funcao do contador de arvore univall
		if root is None:
			return True #verificacao da raiz 
		left = self.countSubTree(root.left, count)
		right = self.countSubTree(root.right, count)
		# sequencia que verifica e compara a raiz e os filhos
		# para verificar se fazem parte de uma arvore univall
		if left == False or right == False:
			return False 
		if root.left != None and (root.left != root.left.val and root.val != root.left.val):
			return False #verificacao de nodo nulo e comparacao
		if root.right != None and (root.right != root.right.val and root.val != root.right.val):
			return False #verificacao de nodo nulo e comparacao
		# caso seja, esse contador sera encrementado
		count[0] += 1
		return True

	def countTrees(self):
		count = [0]
		#funcao para manter a recursividade da chamada
		self.countSubTree(self, count)
		return count[0]

#seting da arvore
root = Node(0)
root.right = Node(0)
root.left = Node(1)
root.right.right = Node(0)
root.right.left = Node(1)
root.right.left.right = Node(1)
root.right.left.left = Node(1)

#impressao
print(f'A quantidade de arvores univais e: {root.countTrees()}')



