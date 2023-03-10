import datetime
def dia_semana():
    ahora = datetime.datetime.now()
    dia_semana_numero = ahora.weekday()
    return dia_semana_numero

