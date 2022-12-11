graph = {
    '1':['2','3','4'],
    '2':['1','3','5'],
    '3':['1','2'],
    '4':['1'],
    '5':['2']
    }

def bfs(G,s):
    visited = [] # lista de vertices visitados, set todos brancos
    queue = [] # inicializa a fila

    visited.append(s) #set como cinza
    queue.append(s)

    while queue:
        u = queue.pop(0)
        for v in G[u]:
            if v not in visited: #verifica se branco
                visited.append(v)
                queue.append(v)
        print(u, end=" ") #set como preto

#main
bfs(graph, '5')


