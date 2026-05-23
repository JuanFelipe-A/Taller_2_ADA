class Queue:

    def __init__(self):
        self.head = 0
        self.tail = -1
        self.e = []

    def enqueue(self, x):
        self.e.append(x)
        self.tail += 1

    def dequeue(self):
        if len(self.e) == 0:
            return None
        else:
            v = self.e.pop(0)
            self.tail -= 1
            return v

    def first(self):
        return self.e[0]

    def last(self):
        return self.e[-1]

    def size(self):
        return len(self.e)

    def isEmpty(self):
        return len(self.e) == 0


def main():
    n = int(input())
    cola = Queue()

    for _ in range(n):
        linea = input().split()
        if not linea:
            continue
        operacion = linea[0]

        if operacion == "LLEGA":
            nombre = linea[1]
            cola.enqueue(nombre)

        elif operacion == "ATIENDE":
            if cola.isEmpty():
                print("SIN PACIENTES")
            else:
                print(cola.dequeue())

        elif operacion == "SIGUIENTE":
            if cola.isEmpty():
                print("COLA VACIA")
            else:
                print(cola.first())


main()