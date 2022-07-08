import grafosPY as g

def buscarIndexConjunto(v,conjuntos):
    for conjunto in conjuntos:
        if v in conjunto:
            return conjuntos.index(conjunto),conjunto

def Kruskal(G):
    bosque = []
    aristas = []
    resultadoAristas = [] #este sera el arreglo que devuelva el algoritmo y contendra las aristas necesarias para armar el ARM
    for idVertice in G.obtenerVertices():
        bosque.append(set(idVertice))
        vertice = G.obtenerVertice(idVertice)
        for vecino in vertice.obtenerConexiones():
            idVecino = vecino.obtenerId()
            arista = [vertice.obtenerPonderacion(vecino),{idVertice,idVecino}]
            if arista not in aristas:
                aristas.append(arista)
    aristas.sort(key=lambda tup: tup[0]) #ordena aristas por ponderacion
    print(bosque) #imprime el bosque con todos los nodos separados que es como empieza el algoritmo
    print(aristas) #imprime lista de aristas ordenadas por ponderacion
    print(resultadoAristas) # se imprimira el arreglo resultado
    while len(bosque) > 1 and len(aristas) >= 1:
        arista = aristas.pop(0)
        v1 = arista[1].pop()
        v2 = arista[1].pop()
        peso = arista[0]
        conj1Ind, conj1 = buscarIndexConjunto(v1,bosque)
        conj2Ind, conj2 = buscarIndexConjunto(v2,bosque)
        if conj1Ind != conj2Ind: #entonces los nodos estan en arboles distintos ytengo que agregar esta arista y unir los arboles que contengan los dos nodos
            arista[1].add(v1)
            arista[1].add(v2)
            resultadoAristas.append(arista)
            union = bosque[conj1Ind].union(bosque[conj2Ind])
            bosque.insert(0,union)
            bosque.remove(conj1)
            bosque.remove(conj2)
    print(bosque) #imprime conjunto de nodos que volvio a unir
    print(aristas) #imprime las aristas que le sobraron
    print(resultadoAristas)


G = g.GrafoNoDir()#creo el grafo con el que probaremos. es el mismo del ppt!! facil de comparar ;)
G.agregarVertice('1')
G.agregarVertice('2')
G.agregarVertice('3')
G.agregarVertice('4')
G.agregarVertice('5')
G.agregarVertice('6')

G.agregarArista('3','2',5)
G.agregarArista('3','4',5)
G.agregarArista('3','5',6)
G.agregarArista('3','6',4)
G.agregarArista('3','1',1)
G.agregarArista('2','1',6)
G.agregarArista('1','4',5)
G.agregarArista('4','6',2)
G.agregarArista('6','5',6)
G.agregarArista('5','2',3)

Kruskal(G)
