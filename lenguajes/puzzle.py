    #* Puzzle lineal con busqueda en amplitud
from tree import nodo

def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while(not solucionado) and len(nodos_frontera !=0):
        nodo = nodos_frontera.pop(0)    #! por que es pop en fifo
        # Extraer nodo y agregarlo a visitados
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            # Solucion encontrada
            solucion = True
            return nodo
        else: 
            # Expandir los nodos hijo
            dato_nodo = nodo.get_datas()
            
            # Operador izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_left = nodo(hijo)
            if not hijo_left.en_lista(nodos_visitados) and not hijo_left.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_left)    #! homework, programar hijo central e hijo derecho

            # Operador central
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_center = nodo(hijo)
            if not hijo_center.en_lista(nodos_visitados) and not hijo_center.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_center) 

            # Operador derecho
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_rigth = nodo(hijo)
            if not hijo_rigth.en_lista(nodos_visitados) and not hijo_rigth.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_rigth) 