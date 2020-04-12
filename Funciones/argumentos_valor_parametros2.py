def estudiantes(valor):
    valor*=3
    
variable = 15
estudiantes(variable)
variable

def listas(numero):
    for x,i in enumerate(numero):
        numero[x] *= 3
        
lista = [50,100,150]
print(listas(lista[:]))

print(lista)

def estudiantess(valor):
    return valor*3

variable = 15
variable = estudiantess(variable)
print(variable)