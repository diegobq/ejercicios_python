# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()

    def to_string(self, valor):
        tipo = type(valor)
        valor_str = str(valor)
        if tipo == float:
            valor_str = f'{valor:.2f}'

        return valor_str

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            dato = self.to_string(d)
            print(dato, end=' ')
        print()

    def to_string(self, valor):
       valor_str = super().to_string(valor)
       return f'{valor_str:>10s}'

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        data_fila_str = [self.to_string(d) for d in data_fila]
        print(','.join(data_fila_str))


class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        data_array = [f'<th>{h}</th>' for h in headers]
        data_array.insert(0, '<tr>')
        data_array.append('</tr>')
        print(''.join(data_array))

    def fila(self, data_fila):
        data_array = [f'<td>{self.to_string(d)}</td>' for d in data_fila]
        data_array.insert(0, '<tr>')
        data_array.append('</tr>')
        print(''.join(data_array))
        
def crear_formateador(fmt):
    # Elige formato
    if fmt == 'txt':
        formateador = FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = FormatoTablaCSV()
    elif fmt == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    
    return formateador
