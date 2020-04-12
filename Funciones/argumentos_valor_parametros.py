def funciones(a,b):
    return a-b

print(funciones(2,2))

print(funciones(b=2,a=1))
print(funciones(2,1))

def nulos(x=None,i=None):
    if x == None or i == None:
        print('Amigo,debes ingresar los dos numeros')
        return
    return x/i

print(nulos(2,2))