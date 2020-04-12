def argu(*tu): #el asterisco sirve para especificar que nosabemos el numero de valores que vamos asignar a la funcion
    for tus in tu:
        print(tus)
print(argu(1,2,4,5,"nombre",'juli'))

def nombre_diccionario(*tu,**lo):
    b = 0
    for tus in tu:
        b+=tus
    print(b)
    for x in lo:
        print(x, " ",lo[x])

print(nombre_diccionario(1,2,3,4,alvaro='Chirou',Estudiantes='Genios',calificaciones=[7,8,9]))        