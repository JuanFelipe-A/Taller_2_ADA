class Nodo:
    def __init__(self, k):
        self.key = k
        self.next = None
 
class SingleLinkedList:
 
    def __init__(self):
        self.head = None
        self.tail = None
 
    def insert_at_end(self, x):
        n = Nodo(x)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
 
    def insert_at_position(self, pos, x):
        n = Nodo(x)
        # Lista vacía o posición 0
        if self.head is None or pos == 0:
            n.next = self.head
            self.head = n
            if self.tail is None:
                self.tail = n
            return
        current = self.head
        i = 0
        while current.next is not None and i < pos - 1:
            current = current.next
            i += 1
        # Insertar después de current
        n.next = current.next
        current.next = n
        if n.next is None:
            self.tail = n
 
    def delete_first_occurrence(self, x):
        if self.head is None:
            return
        if self.head.key == x:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.key == x:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return
            current = current.next
 
    def print_list(self):
        if self.head is None:
            print("LISTA VACIA")
            return
        result = []
        current = self.head
        while current:
            result.append(current.key)
            current = current.next
        print(" ".join(result))
 
 
def main():
    n = int(input())
    lista = SingleLinkedList()
 
    for _ in range(n):
        linea = input().split()
        operacion = linea[0]
 
        if operacion == "AGREGAR":
            cancion = linea[1]
            lista.insert_at_end(cancion)
 
        elif operacion == "INSERTAR":
            pos = int(linea[1])
            cancion = linea[2]
            lista.insert_at_position(pos, cancion)
 
        elif operacion == "ELIMINAR":
            cancion = linea[1]
            lista.delete_first_occurrence(cancion)
 
        elif operacion == "MOSTRAR":
            lista.print_list()
 
 