    #* Puzzle lineal con busqueda en amplitud
from tree import Nodo

def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while not ( solucionado) and len(nodos_frontera)!=0:
        nodo = nodos_frontera.pop(0)    #! por que es pop en fifo
        # Extraer nodo y agregarlo a visitados
        nodos_visitados.append(nodo)
        if nodo.set_datas() == solucion:
            # Solucion encontrada
            solucionado = True
            return nodo
        else: 
            # Expandir los nodos hijo
            dato_nodo = nodo.get_datas()
            
            # Operador izquierdo
            hijo_left = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_left.fath = nodo
            if not hijo_left.en_lista(nodos_visitados) and not hijo_left.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_left)    #! homework, programar hijo central e hijo derecho 

            # Operador central
            hijo_center = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_center.fath = nodo
            if not hijo_center.en_lista(nodos_visitados) and not hijo_center.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_center) 

            # Operador derecho
            hijo_rigth = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_rigth.fath = nodo
            if not hijo_rigth.en_lista(nodos_visitados) and not hijo_rigth.en_lista(nodos_frontera):    #! Estudiar mas cawn
                nodos_frontera.append(hijo_rigth) 

if __name__ == "__main__":
    estado_inicial=[4,2,3,1]
    solucion=[1,2,3,4]
    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)

    #*Mostrar REsultados
    resultado = []
    nodo = nodo_solucion
    while nodo.get_fath()!=None:
        resultado.append(nodo.get_datas())
        nodo = nodo.get_fath()
    resultado.append(estado_inicial)
    print(resultado)

    #*[[4,2,3,1], [2,4,3,1], [2,3,1,4], [2,1,3,4], [1,2,3,4]]