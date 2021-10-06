from datetime import datetime

def strptime(fecha_str):
    return datetime.strptime(fecha_str, '%d/%m/%Y')

def dia_primavera(anio):
    return strptime(f'21/09/{anio}')

def dias_proxima_primavera():
    '''
    Calcula la cantidad de días para la próxima primavera.-
    Si la primavera ya pasó este año, calcula la primavera del año próximo.-

    Returns
    -------
    segs : TYPE float
        DESCRIPTION.

    '''
    hoy = datetime.now()

    anio_primavera = hoy.year
    primavera = dia_primavera(anio_primavera)
    if primavera < hoy:
        anio_primavera += 1

    proxima_primavera = strptime(f'21/09/{anio_primavera}')
    dif = proxima_primavera - hoy

    return dif.days