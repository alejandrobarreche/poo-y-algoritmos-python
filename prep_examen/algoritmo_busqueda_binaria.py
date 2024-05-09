import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


class Busqueda_binaria():
    def __init__(self, lista, objetivo):
        self.lista = lista
        self.num_inicio = 0
        self.num_fin = len(self.lista) - 1
        self.objetivo = objetivo

    @property
    def inicio(self):
        return self.num_inicio

    @inicio.setter
    def inicio(self, nuevo_inicio):
        if isinstance(nuevo_inicio, int) and 0 <= nuevo_inicio < len(self.lista):
            self.num_inicio = nuevo_inicio

    @property
    def fin(self):
        return self.num_fin
    
    @fin.setter
    def fin(self, nuevo_fin):
        if isinstance(nuevo_fin, int) and self.inicio < nuevo_fin < len(self.lista):
            self.num_fin = nuevo_fin
            
    def busqueda_binaria(self):
        while self.inicio <= self.fin:
            self.medio = (self.inicio + self.fin) // 2
            if self.lista[self.medio] == self.objetivo:
                return True
            elif self.lista[self.medio] < self.objetivo:
                self.inicio = self.medio + 1
            elif self.lista[self.medio] > self.objetivo:
                self.fin = self.medio - 1
        return False
                
            


        


lista = [1, 3, 5, 7, 9]
objetivo = 9

intento = Busqueda_binaria(lista, objetivo)
# print(intento.inicio)
# intento.inicio = 1   # Para cambiar el atributo inicio escribiendo el setter de esa manera
# print(intento.inicio)
# print(intento.fin)
# intento.fin = 5

print(intento.fin)

print(intento.busqueda_binaria())



# if __name__ == '__main__':
#     tamano_de_lista = int(input('De que tamano es la lista? '))
#     objetivo = int(input('Que numero quieres encontrar? '))

#     lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

#     encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

#     print(lista)
#     print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')