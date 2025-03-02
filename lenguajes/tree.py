class Nodo:
    def __init__(self, datas, sons = None): #! posiblemente falte agregar el parametro padre(fath) y costo igual, lista nodo, nodo
        self.datas = datas
        self.costo = None
        self.fath = None
        self.set_sons(sons)

    def set_sons(self, sons):
        self.sons = sons
        if self.sons != None:
            for h in sons:
                h.sons = self

    def get_sons(self):
        return self.sons

    def get_fath(self):
        return  self.fath

    def set_datas(self, datas):
        self.datas = datas

    def set_costo(self, costo):
        self.costo = costo

    def same(self, nodo):
        return self.get_datas() == nodo.get_datas()
        #if self.get_datas() == nodo.get_datas():
        #    return True
        #else:
        #    return False
        

    def en_lista(self, lista_nodos):
        return any(self.same(n) for n in lista_nodos)
#        en_la_lista = False
#        for n in lista_nodos:
#            if self.igual(n):
#                en_la_lista =  True
#        return en_la_lista
    
    def __str__(self):
        return str(self.get_datas())
    
#    def __main__(self):
#        return str(self.get_datas(), self.get_fath())

#    print(f"ya finalizo")