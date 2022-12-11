#Aluno: Pedro Vinícius da Silva Ribeiro
#Matricula: 2019033903

# Checa se o vetor passado é um max-heap
def maxHeapCheck(arr):
    max_i = len(arr) - 1

    for i in range(max_i):
        left = 2 * i + 1
        right = 2 * (i + 1)

        if left <= max_i:
            if arr[i] < arr[left]:
                return False
        
        if right <= max_i:
            if arr[i] < arr[right]:
                return False

    return True

# Fila de prioridade usando max-heap
class PriorityQueue():
    def __init__(self):
        self.size = -1
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * (i + 1)

    def getMax(self):
        return self.heap[0]

    def shiftUp(self, i):
        while (i > 0 and self.heap[self.parent(i)] < self.heap[i]):
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def shiftDown(self, i):
        max_i = i

        l = self.left(i)
        r = self.right(i)

        if l <= self.size and self.heap[l] > self.heap[max_i]: 
            max_i = l

        if r <= self.size and self.heap[r] > self.heap[max_i]: 
            max_i = r

        if i != max_i:
            self.heap[i], self.heap[max_i] = self.heap[max_i], self.heap[i]
            self.shiftDown(max_i)
        
    def extractMax(self):
        result = self.heap[0]

        self.heap[0] = self.heap.pop(-1)
        self.size -= 1

        self.shiftDown(0)

        return result

    def insertKey(self, value):
        self.size += 1
        self.heap.append(value)

        self.shiftUp(self.size)

    def deleteKey(self, i):
        self.heap[i] = self.getMax() + 1
        self.shiftUp(i)
        self.extractMax()

    def changePriority(self, i, new_value):
        old_priority = self.heap[i]
        self.heap[i] = new_value

        if new_value > old_priority:
            self.shiftUp(i)
        else:
            self.shiftDown(i)

    def printPQ(self):
        print("| HEAP | Size = {} | ".format(self.size + 1), end="")
        print(self.heap)

# Função Main
def main():
    pq = PriorityQueue()

    pq.insertKey(95)
    pq.insertKey(60)
    pq.insertKey(78)
    pq.insertKey(39)
    pq.insertKey(28)
    pq.insertKey(66)
    pq.insertKey(70)
    pq.insertKey(33)

    pq.printPQ()

    print()
    print("Extracted max from PQ =", pq.extractMax())
    print()

    pq.printPQ()

    pq.insertKey(50)

    print()
    print("Added node with value 50!")
    print()

    pq.printPQ()

    pq.changePriority(5, 10)

    print()
    print("Changed priority of the node with index 5 to 10!")
    print()

    pq.printPQ()

    pq.deleteKey(6)

    print()
    print("Deleted node with index 6!")
    print()

    pq.printPQ()

main()