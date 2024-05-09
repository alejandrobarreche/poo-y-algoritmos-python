def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


class Buble_sort():
    def __init__(self, lista):
        self._lista = lista
        self.tamaño = len(self.lista)

    
    @property
    def lista(self):
        return self._lista
    
    def algoritmo_ordenar(self):
        for i in range(self.tamaño):
            for j in range(self.tamaño - i - 1):
                if self.lista[j] > self.lista[j + 1]:
                    self.lista[j], self.lista[j+1] = self.lista[j + 1], self.lista[j]
        return self.lista
    

lista = [1, 3, 5, 2, 5, 7, 12, 71, 13]
ordenacion = Buble_sort(lista)
print(ordenacion.algoritmo_ordenar())