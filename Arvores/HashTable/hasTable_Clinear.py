class HashLinearColisao:

     def __init__(self,tam):
          self.tab = {}
          self.tam_max = tam

     def funcaohash(self, chave):
          v = int(chave)
          return (v%int(self.tam_max))

     def cheia(self):
          return len(self.tab) == self.tam_max

     def imprime(self):
          for i in self.tab:
               print("Hash[%d] = " %i, end="")
               print (self.tab[i])

     def apaga(self, chave):
          pos = self.busca(chave)
          if pos != -1:
               del self.tab[pos]
               print("-> Item da posicao %d apagado" %pos) 
          else:
               print("-> Item nao encontrado")

     def busca(self, chave):
          pos = self.funcaohash(chave)
          if self.tab.get(pos) == None: # se esta posição não existe
               return -1 #saida imediata
          if self.tab[pos] == chave: # se o item esta na posição indicada pela função hash
               return pos
          else:
               for i in self.tab: # busca do item em toda hash (pois ele pode ter sido inserido apos colisão)
                    if self.tab[i]==chave:
                         return i
          return -1

     def insere(self, item):
          if self.cheia():
               print("-> ATENÇÃO Tabela Hash CHEIA")
               return
          pos = self.funcaohash(item)
          if self.tab.get(pos) == None: # se posicao vazia
               self.tab[pos] = item
               print("-> Inserido HASH[%d]" %pos)
          else: # se posicao ocupada
               print("-> Ocorreu uma colisao na posicao %d" %pos)
               while True:
                    if self.tab[pos] == item: # se o item ja foi cadastrado
                         print("-> ATENCAO Esse item ja foi cadastrado")
                         return
                    if pos == (self.tam_max - 1):
                         pos = -1
                    pos = pos + 1 # incrementa mais uma posição
                    if self.tab.get(pos) == None:
                         self.tab[pos] = item
                         print("-> Inserido apos colisao HASH[%d]" %pos)
                         break              
# fim Classe HashLinearColisao

tamanhoHash = 7
tab = HashLinearColisao(tamanhoHash)
print("\n****************************************************")
print("      Tabela HASH Colisoes Linear (%d itens) " %tamanhoHash)
print("****************************************************")
for i in range (0,tamanhoHash,1):
     print("\nInserindo item %d" %(i + 1));
     item = input(" - Forneca valor: ")
     tab.insere(item)
item = input("\n - Forneca valor para buscar: ")
pos = tab.busca(item)
if pos == -1:
     print("-> Item nao encontrado")
else:
     print("-> Item encontrado na posicao: ", pos)
item = input("\n - Forneca valor para apagar: ")
tab.apaga(item)
print("\nImprimindo conteudo")
tab.imprime()
print("\n")