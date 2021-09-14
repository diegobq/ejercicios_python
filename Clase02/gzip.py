# gzip.py
# Ejercicio 2.4: Archivos comprimidos
import gzip

with gzip.open('../Data/camion.csv.gz', 'rt') as file:
    print(file.read())
    