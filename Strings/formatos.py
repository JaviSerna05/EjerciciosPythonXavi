#texto = "  curso de Python 3, Python basico   " 

#resultado = texto.capitalize()-->Pone las palabras en mayusculas a su inicio
#resultado = texto.swapcase()-->Pone las palabras minisculas en mayusculas y viceversa
#resultado = texto.upper() #--> Ponerlas las palabras en mayusculas 
#resultado = texto.lower() #--> Ponerlas las palabras en minusculas
#resultado = texto.title() #Pone las palabras en modo titulo
#resultado = texto.replace("Python", "Java", 1) #Sirve para reemplazar y con un numero se puede decir la cantidad de veces que lo quiero reemplazar
#resultado = texto.strip() # Sirve para quitar los espacios en los strings
#print(resultado.isupper()) # Es un Boolean
#print(resultado.islower()) # Es un Boolean

#print(resultado)


curso = "Python"
version = "3"

#resultado = "Curso de %s %s" %(curso, version)
#resultado = "Curso de {} {} ".format( curso, version)
resultado = "Curso de {a} {b} ".format( a=curso, b=version)

print(resultado)