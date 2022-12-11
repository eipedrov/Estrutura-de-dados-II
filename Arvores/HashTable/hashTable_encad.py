#Aluno: Pedro Vinícius da Silva Ribeiro
#Matricula: 2019033903
#Acauan Ribeiros
#Estrutura de dados II

class Node:
    def __init__(self, value) -> None:
        self.value = value
        # nÃ³ de colisao
        self.next = None

    def free(self):
        self.swapNext()

    def isEmpty(self):
        return self.value == None

    def addNext(self, node):
        self.next = node

    def swapNext(self):
        if self.next != None:
            self.value = self.next.value
            self.next.swapNext()
        else:
            self.value = None
            self.next = None


    def __str__(self) -> str:
        return f'Node({self.value})'

class HashTable:

    def __init__(self, size) -> None:        
        # inicializa o vetor de dados
        self.data = [Node(None)] * size

    def hashing(self, value):
        return value % len(self.data)

    def add(self, value):
        # cria o novo no a ser inserido
        node = Node(value)
        # codigo de hashing
        hash = self.hashing(node.value)
    
        if self.data[hash].isEmpty(): # posicao vazia
            self.data[hash] = node
        else: # colisao
            collision = self.data[hash]
            while collision.next != None:
                collision = collision.next   
            collision.addNext(node)

    def find(self, value):
        hash = self.hashing(value)
        node = self.data[hash]
        if node.isEmpty(): # elemento nao existe
            print('Elemento nao existe')
            return None
        else: # existe elemento
            if node.value == value:
                return node
            else:
                collision = node.next
                while not collision.isEmpty():
                    if collision.value == value:
                        return collision  
                    collision = collision.next
                print('Elemento nao encontrado')  
                return None            

    def delete(self, value):
        node = self.find(value)
        node.free()
        
    def show(self):
        for i in range(len(self.data)):
            node = self.data[i]
            print(f'\ntable[{i}]: {node}')
            collision = node.next            
            while collision != None and collision.value:
                print(f'{collision} ->', end='')
                collision = collision.next

h = HashTable(10)
for i in range(30):
    h.add(i)

print('Elementos')
h.show()
print('Removendo o 3')
h.delete(3)
print('Elementos')
h.show()