class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

    def get_items(self):
        return self.items

class TorreDeControl:
    def __init__(self):
        self.arribos = Cola()
        self.partidas = Cola()

    def ver_estado(self):
        arribos = f'Vuelos esperando para aterrizar: {",".join(self.arribos.get_items())}'
        partidas = f'Vuelos esperando para despegar: {",".join(self.partidas.get_items())}'
        estado = [arribos, partidas]
        return '\n'.join(estado)

    def nuevo_arribo(self, numero_vuelo):
        self.arribos.encolar(numero_vuelo)

    def nueva_partida(self, numero_vuelo):
        self.partidas.encolar(numero_vuelo)

    def asignar_pista(self):
        resultado = 'No hay vuelos en espera.'

        if not self.arribos.esta_vacia():
            numero_vuelo = self.arribos.desencolar()
            resultado = f'El vuelo {numero_vuelo} aterrizó con éxito.'
        elif not self.partidas.esta_vacia():
            numero_vuelo = self.partidas.desencolar()
            resultado = f'El vuelo {numero_vuelo} despegó con éxito.'

        return resultado
