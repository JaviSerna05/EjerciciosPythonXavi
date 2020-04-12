#Palabra reservada es def 

def estudiantes():
    print("Genios mis estudiantes parte de mi familia digital")
estudiantes()

def tabla_del_7():
    for x in range(10):
        print("7 * {} = {}".format(x,x*7))
tabla_del_7()

def advierto():
    global variable #Con global me permite usar una variable de manera amplia y sin limites pero su ejecucion siempre va ser valor que yo le asigne en la funcion
    variable = 'alvaro'
    print(variable)
advierto()

variable='Chirou'
advierto()
print(variable)
