from ARBOL import Nodo

def buscar_solucion_DFS_rec(nodo_inicial, solucion, visitados):
    nodo_incial = Nodo(estado_inicial)
    solucion = False
    visitados = []
    visitados.append(nodo_inicial.get_datos())
    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial 
    else:   #* Expandiremos los nodos sucesores
        dato_nodo = nodo_inicial.get_datos()
                                                #! Revisar si el valor de hijo con los valores de la posicion pueden ser con el mismo nombre
        hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]])
        hijo_central = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]])
        hijo_derecho = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])

        hijo_izquierdo.set_padre(nodo_inicial)
        hijo_central.set_padre(nodo_inicial)
        hijo_derecho.set_padre(nodo_inicial)

        nodo_inicial.set_hijos(hijo_izquierdo, hijo_central, hijo_derecho)

        for nodo_hijo in nodo_inicial.get_hijos():
            if not nodo_hijo.get_datos() in visitados:  #* LLamada recursiva
                sol = buscar_solucion_DFS_rec(nodo_hijo, solucion, visitados)   #! ********
                if sol != None:
                    return sol

#return None

if __name__ == "__main__":
    estado_inicial = [4,3,2,1]
    solucion = [1,2,3,4]
    nodo_solucion = None
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    sol = buscar_solucion_DFS_rec(nodo_inicial, solucion, visitados)

    #* Mostrar el resultado 
    resultado = []
    while Nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)