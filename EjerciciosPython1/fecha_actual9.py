import datetime

fechaActual = datetime.datetime.now()
print('Fecha actual', fechaActual.date())

fechaNacio = input('Digite su fecha de nacimiento (aaaa-mm-dd)\n')
fechaNacimiento = datetime.datetime.strptime(fechaNacio, '%Y-%m-%d')
print('Fecha nacimiento:', fechaNacimiento.date())

diferencia = fechaActual - fechaNacimiento
print('Entre las 2 fechas hay:', diferencia.days, 'dias')