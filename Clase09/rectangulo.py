class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto1.x - self.punto2.x)
    
    def altura(self):
        return abs(self.punto1.y - self.punto2.y)
    
    def area(self):
        return self.base() * self.altura()

    def desplazar(self, desplazamiento):
        self.punto1 += desplazamiento
        self.punto2 += desplazamiento
    
    def rotar(self):
        base = 0
        return base
    
    def __str__(self):
        return f'[({self.punto1.x}, {self.punto1.y}), ({self.punto2.x}, {self.punto2.y})]'

def imprimir(rectangulos):
    print(f'{"Rectangulo":30s}{"Base":<10s}{"Altura":<10s}{"Area":<10s}')
    for nombre, rect in rectangulos.items():
        print(f'{nombre:6s} {rect.__str__():23s}{rect.base():<10d}{rect.altura():<10d}{rect.area():<10d}')


if __name__ == '__main__':
    ul = Punto(0, 2)
    lr = Punto(1, 0)
    ll = Punto(0, 0)
    ur = Punto(1, 2)
    a = Punto(-1, 0)
    b = Punto(-5, 2)
    rect1 = Rectangulo(ul,lr)
    rect2 = Rectangulo(ll,ur)
    rect3 = Rectangulo(a,b)
    rectangulos = {"rect1": rect1, "rect2": rect2, "rect3": rect3}
    imprimir(rectangulos)
    for rect in rectangulos.values():
        rect.desplazar(Punto(1, 1))
    imprimir(rectangulos)