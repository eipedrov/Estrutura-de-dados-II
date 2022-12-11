#Aluno: Pedro Vinícius da Silva Ribeiro
#Matricula: 2019033903

#Heap
def maxHeapify(vector, i):
    left = 2 * i
    right = 2 * 1 + 1
    if left <= len(vector) -1 and vector[left] > vector[i]:
        maior = left 
    else:
        maior = i
    if right <= len(vector) -1 and vector[right] > vector[maior]:
        maior = right
    if maior != i:
        vector[i], vector[maior] = maior, vector[i]
        maxHeapify(vector, maior)

def buildHeap(vector):
    heapSize = len(vector)-1
    for i in range(heapSize // 2, -1, -1):
        maxHeapify(vector, i)

# -- Main --

vector = [8, 18, 14, 17, 12, 13, 11, 15, 16]
print(vector)
buildHeap(vector)
print(vector)

