# comprension.py
import csv

# Ejercicio 4.14: Fijando ideas
def leer_dowstocks(file_name):
    data = []
    with open(file_name, 'rt') as file:
        rows = csv.reader(file)
        headers = next(rows)
        types = [str, float, dateStr_as_tuple, str, float, float, float, float, int]
        for row in rows:
            converted_row = [converter(value) for converter, value in zip(types, row)]
            dict_row = dict(zip(headers, converted_row)) 
            data.append(dict_row)
        
    print(data[0])

def dateStr_as_tuple(dateStr):
    return tuple([int(value) for value in dateStr.split('/')])

leer_dowstocks('../Data/dowstocks.csv')
