from datetime import datetime

def vida_en_segundos(fecha_nac_str):
    '''
    Calcula la cantidad de segundos vividos hasta el día de hoy.-
    Pre: considera que nació a las 00hs de la fecha indicada.-

    Parameters
    ----------
    fecha_nac_str : TYPE
        DESCRIPTION. fecha de nacimiento con formato DD/MM/AAAA

    Returns
    -------
    segs : TYPE float
        DESCRIPTION.

    '''
    hoy = datetime.now()
    fecha_nac = datetime.strptime(fecha_nac_str, '%d/%m/%Y')
    dif = hoy - fecha_nac

    return dif.total_seconds()
