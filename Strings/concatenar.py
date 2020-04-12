#Para conactenar se  usa el simbolo +
curso = "Curso de Python"

#curso = "c" + curso[1:] + " " + " en Codigo Facilito"
curso = "c" + curso[1:] + str(3) + " " + " en Codigo Facilito"
#Para numeros se usa str(aqui va el numero)

curso = "Python"
version = "3"

#resultado = "Curso de %s %s" %(curso, version)
#resultado = "Curso de {} {} ".format( curso, version)
resultado = "Curso de {a} {b} ".format( a=curso, b=version)

print(resultado)
print(curso) 