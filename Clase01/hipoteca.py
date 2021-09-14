# hipoteca.py
# Ejercicio 1.11: Bonus

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses = 1
mes_inicio_adelanto = 61
mes_fin_adelanto = 108
pago_extra = 1000

while saldo > 0:
	pago = pago_mensual
	if (meses >= mes_inicio_adelanto and meses <= mes_fin_adelanto):
		pago = pago + pago_extra
	nuevo_saldo = saldo * (1+tasa/12)
	if (nuevo_saldo > pago):
		saldo = nuevo_saldo - pago
		total_pagado = total_pagado + pago
	else:
		saldo = 0
		total_pagado = total_pagado + nuevo_saldo
	mensaje = f'{meses:3d} {round(total_pagado, 2):10.2f} {round(saldo, 2):10.2f}'
	print(mensaje)
	meses = meses + 1

print('Total pagado', round(total_pagado, 2))
print('Meses:', meses - 1)
