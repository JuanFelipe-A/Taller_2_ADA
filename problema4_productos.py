class Nodo:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
 
class HashTable:
 
    def __init__(self, Q):
        self.capacity = Q
        self.size = 0
        self.table = [None] * Q
 
    def func_hash(self, key):
        return hash(key) % self.capacity
 
    def insert(self, key, val):
        idx = self.func_hash(key)
        if self.table[idx] is None:
            self.table[idx] = Nodo(key, val)
            self.size += 1
        else:
            actual = self.table[idx]
            while actual:
                if actual.key == key:
                    actual.value = val
                    return
                if actual.next is None:
                    break
                actual = actual.next
            actual.next = Nodo(key, val)
            self.size += 1
 
    def search(self, k):
        idx = self.func_hash(k)
        current = self.table[idx]
        while current:
            if current.key == k:
                return current.value
            current = current.next
        raise KeyError(k)
 
 
def main():
    n = int(input())
    tabla = HashTable(100)
 
    for _ in range(n):
        linea = input().split()
        operacion = linea[0]
 
        if operacion == "VENDER":
            producto = linea[1]
            cantidad = int(linea[2])
            try:
                actual = tabla.search(producto)
                tabla.insert(producto, actual + cantidad)
            except KeyError:
                tabla.insert(producto, cantidad)
 
        elif operacion == "CONSULTAR":
            producto = linea[1]
            try:
                print(tabla.search(producto))
            except KeyError:
                print(0)
 
        elif operacion == "TOTAL":
            total = 0
            for bucket in tabla.table:
                current = bucket
                while current:
                    total += current.value
                    current = current.next
            print(total)
 
 
main()