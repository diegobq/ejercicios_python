# diccionario_geringoso.py
# Ejercicio 2.14: Diccionario geringoso.

def geringoso_translator(cadena):
    '''
    Traduce una palabra al jeringoso

    Parameters
    ----------
    cadena : String
        Palabra que se quiere traducir al jeringoso.

    Returns
    -------
    Palabra en jeringoso.

    '''
    capadepenapa = ''
    vocales = 'aeiou'
    for c in cadena:
    	capadepenapa += c
    	if(c.lower() in vocales):
    		capadepenapa += 'p' + c
            
    return capadepenapa

def diccionario_geringoso(palabras):
    '''
    Traduce una lista de palabras al geringoso para hacer un diccionario

    Parameters
    ----------
    palabras : Array
        Lista de palabras a traducir.

    Returns
    -------
    Diccionario con k= palabra, v= palabra en geringoso
    '''
    
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = geringoso_translator(palabra)
    
    return diccionario

diccionario = diccionario_geringoso(['banana', 'manzana', 'mandarina'])
print(diccionario)

# {'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}
        