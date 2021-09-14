# tablamult.py
# Ejercicio 3.17: Tablas de multiplicar

def imprimir_header(num_columnas):
    header_str = f'{"":3s}'
    for index in range(num_columnas):
        index_str = str(index)
        header_str += f' {index_str:>5s}'
    print(header_str)
    print('-' * len(header_str))


def imprimir_tablas(num_filas, num_columnas):
    for digito in range(num_filas):
        digito_str = str(digito) + ':'
        row_str = f'{digito_str:3s}'
        acumulador = 0
        acumulador_str = str(acumulador)
        for digito_row in range(num_columnas):
            row_str += f' {acumulador_str:>5s}'
            acumulador += digito
            acumulador_str = str(acumulador)
            
        print(row_str)


def tablamult(num_filas, num_columnas):
    imprimir_header(num_columnas)
    imprimir_tablas(num_filas, num_columnas)

tablamult(10, 10)