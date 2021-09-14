# buscar_precio.py
# Ejercicio 2.7: Buscar precios

def buscar_precio(fruta):
    '''
    Muestra por pantalla el precio de la fruta indicada.
    Los precios los obtiene del archivo precios.csv

    Parameters
    ----------
    fruta : String
        Nombre de la fruta que se desea saber el precio.

    Returns
    -------
    None

    '''
    
    product_price = None
    with open('../Data/precios.csv', 'rt') as file:
        next_line = next(file)
        while len(next_line.split(',')) > 1:
            if(fruta in next_line):
                product = next_line.split(',')
                product_price = float(product[1])
                next_line = ''
            else:
                next_line = next(file)
    
    if product_price != None:
        print(f'El precio de un cajón de {fruta} es: {product_price}')
    else:
        print(f'{fruta} no figura en el listado de precios.')

buscar_precio('Frambuesa')
buscar_precio('Kale')

# El precio de un cajón de Frambuesa es: 34.35
# Kale no figura en el listado de precios.
