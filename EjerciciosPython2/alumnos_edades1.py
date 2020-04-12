edadAlumnos = 0
cantidadAlumnos = 0
contadorEdad = 0
prom = 0
continuar = 'si'

while continuar == 'si':

	edadAlumnos = int(input('Digite la edad del alumno\n'))

	if edadAlumnos < 18:
		contadorEdad = contadorEdad + edadAlumnos
		cantidadAlumnos = cantidadAlumnos +1
		prom = contadorEdad / cantidadAlumnos
	elif edadAlumnos >= 18:
		contadorEdad = contadorEdad + edadAlumnos
		cantidadAlumnos = cantidadAlumnos +1
		prom = contadorEdad / cantidadAlumnos - edadAlumnos

	continuar = input('Desea continuar ingre Si o de lo contrario el programa termina\n')
else:		
	print('El numero de alumnos ingresados es:', cantidadAlumnos)
	print('El total de las edades es:', contadorEdad)
	print('El promedio de edades menor a 18 es:', prom)