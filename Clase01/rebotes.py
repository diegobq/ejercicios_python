# rebotes.py
# Ejercicio 1.5: La pelota que rebota

altura = 100
perdida = 3/5
rebotes = 10
rebote = 1

while rebote <= rebotes:
	altura = altura * perdida
	print(f'{rebote: 3d} {round(altura, 4):7.4f}')
	rebote = rebote + 1
