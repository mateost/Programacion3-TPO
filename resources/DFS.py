import grafosPY as g

def DFS (origen,marca = {},padre = {}):
    marca[origen.obtenerId()]="Gris"
    for v in origen.obtenerConexiones():
        if marca.get(v.obtenerId())=="Blanco":
            padre[v.obtenerId()] = origen.obtenerId()
            DFS(v,marca,padre)
    marca[origen.obtenerId()]="Negro"

def DFS_Forest(G,marca,padre):
    for vertice in G.obtenerVertices():
        marca[vertice] = "Blanco"
    for vertice in G.obtenerVertices():
        if marca.get(G.obtenerVertice(vertice).obtenerId())=="Blanco":
            DFS(G.obtenerVertice(vertice),marca,padre)


if '__main__' == __name__:
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

    DFS_Forest(G,marca=marca,padre=padre)


    print(padre)
