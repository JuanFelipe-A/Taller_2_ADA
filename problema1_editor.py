class Stack:
    def __init__(self, top=-1):
        self.e = []
        self.tope = top

    def top(self):
        return self.e[self.tope]

    def push(self, x):
        self.e.append(x)
        self.tope += 1

    def pop(self):
        v = self.e.pop(-1)
        self.tope -= 1
        return v

    def size(self):
        return self.tope + 1

    def isEmpty(self):
        return self.tope < 0


def main():
    n = int(input())
    pila = Stack()

    for _ in range(n):
        linea = input().split()
        operacion = linea[0]

        if operacion == "ESCRIBIR":
            palabra = linea[1]
            pila.push(palabra)

        elif operacion == "DESHACER":
            if not pila.isEmpty():
                pila.pop()

        elif operacion == "MOSTRAR":
            if pila.isEmpty():
                print("VACIO")
            else:
                # e[0] es el fondo (primera palabra), e[tope] es la última
                print(" ".join(pila.e))


main()