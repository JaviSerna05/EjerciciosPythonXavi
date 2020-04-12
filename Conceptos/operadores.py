#Operadores relacionales se usan para obtener un true or false
variable_uno = 10
variable_dos = 18

mayor = variable_uno > variable_dos
menor = variable_uno < variable_dos
mayor_igual = variable_uno >= variable_dos
menor_igual = variable_uno <= variable_dos
igual = variable_uno == variable_dos
diferente = variable_uno != variable_dos


#print(mayor)
#print(menor)
#print(mayor_igual)
#print(menor_igual)
#print(igual)
#print(diferente)

#and --> Todas deben ser verdadero o falso
#or --> alguna de la condciones debe cumplir
#not --> me da el otro dato
#is --> me da igual al resultado que tenga
resultado = True and True and diferente
print(resultado)
