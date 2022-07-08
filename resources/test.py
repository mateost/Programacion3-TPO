import grafosPY as g
import Kruskal as k
import DFS as d

#RECOMIENDO PROBAR CADA ALGORITMO DESDE SU ARCHIVO (AUNQUE SE PUEDE PROBAR DESDE ACA TAMBIEN PERO SE VAN A SUPERPONER LAS PRUEBAS DE AMBOS)

#PARA PROBAR DFS

G = g.Grafo()#creo el grafo con el que probaremos. es el mismo del ppt!! facil de comparar ;)
G.agregarVertice('u')
G.agregarVertice('v')
G.agregarVertice('w')
G.agregarVertice('x')
G.agregarVertice('y')
G.agregarVertice('z')

G.agregarArista('u','v')
G.agregarArista('u','x')
G.agregarArista('v','y')
G.agregarArista('w','y')
G.agregarArista('w','z')
G.agregarArista('x','v')
G.agregarArista('y','x')
G.agregarArista('z','z')

padre = {}
marca = {}

for vertice in G.obtenerVertices():
    padre[vertice] = None

d.DFS_Forest(G,marca=marca,padre=padre)


print(padre)

#PARA PROBAR KRUSKAL

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

k.Kruskal(G)
