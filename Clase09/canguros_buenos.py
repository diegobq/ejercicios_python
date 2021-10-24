# Canguro bueno
class Canguro:
    def __init__(self, nombre, contenido_marsupio = []):
        self.nombre = nombre
        if not len(contenido_marsupio) == 0:
            self.contenido_marsupio = contenido_marsupio
        else:
            self.contenido_marsupio = []

    def meter_en_marsupio(self, nuevo):
        self.contenido_marsupio.append(nuevo)

    def __str__(self):
        t = []
        for obj in self.contenido_marsupio:
            s = obj.__str__()
            t.append(s)
        return f'{self.nombre}: [{",".join(t)}]'

    def __repr__(self):
        contenido_str = ''
        if not len(self.contenido_marsupio) == 0:
            t = []
            for obj in self.contenido_marsupio:
                s = obj.__repr__()
                t.append(s)
            contenido_str = f', [{",".join(t)}]'

        return f'Canguro(\'{self.nombre}\'{contenido_str})'

# Canguro Malo
# class Canguro:
#     """Un Canguro es un marsupial."""

#     # cuando pasamos un valor mutable como 'default' en una funcion...
#     # el argumento cambia cada vez que el valor se modifica...
#     # el valor por omision es diferente cada vez que la funcion es llamada.-
#     def __init__(self, nombre, contenido=None):
#         """Inicializar los contenidos del marsupio.

#         nombre: string
#         contenido: contenido inicial del marsupio, lista.
#         """
#         self.nombre = nombre
#         self.contenido_marsupio = [] if contenido == None else contenido

#     def __str__(self):
#         """devuelve una representación como cadena de este Canguro.
#         """
#         t = [ self.nombre + ' tiene en su marsupio:' ]
#         for obj in self.contenido_marsupio:
#             s = '    ' + object.__str__(obj)
#             t.append(s)
#         return '\n'.join(t)

#     def meter_en_marsupio(self, item):
#         """Agrega un nuevo item al marsupio.

#         item: objecto a ser agregado
#         """
#         self.contenido_marsupio.append(item)
