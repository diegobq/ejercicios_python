# precio_naranja.py
# Ejercicio 2.3: Precio de la naranja

product_name = 'Naranja'
product_price = None
with open('../Data/precios.csv', 'rt') as file:
    next_line = next(file)
    while len(next_line.split(',')) > 1:
        if(product_name in next_line):
            product = next_line.split(',')
            product_price = float(product[1])
            next_line = ''
        else:
            next_line = next(file)

if product_price != None:
    print(f'El precio de la naranja es: {product_price}')
else:
    print(f'No hay "{product_name}" en el camión')
    