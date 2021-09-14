# preliminares.py
# Ejercicio 2.1: Preliminares sobre lectura de archivos

print('**********file.read()*********')
with open('../Data/camion.csv', 'rt') as file:
    print(file.read())

print('**********for in*********')
with open('../Data/camion.csv', 'rt') as file:
    for line in file:
        print(line) 

print('**********for in without first line*********')
file = open('../Data/camion.csv', 'rt')
headers = next(file)
print(headers)

for line in file:
    print(line)
    
file.close()
