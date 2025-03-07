class Nodo:
    def __init__(self, datos, hijos=None):  # Corregido el constructor (__init__)
        self.datos = datos  
        self.padre = None
        self.costo = None
        self.set_hijos(hijos)

    def set_hijos(self, hijos):
        self.hijos = hijos if hijos is not None else []  # Asegura que hijos sea una lista
        for h in self.hijos:
            h.padre = self

    def get_hijos(self):
        return self.hijos 

    def get_datos(self):
        return self.datos

    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos
    
    def set_costo(self, costo):
        self.costo = costo

    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()

    def en_lista(self, lista_nodos):
        return any(self.igual(n) for n in lista_nodos)

    def __str__(self):  # Corregido el método (__str__)
        return str(self.get_datos())
