#funciones recursivas --> Son aquellas que se llaman asi mismas se reutilizan asi mismas
#Nota hay que revisar sus limites

def atras(segundos):
    segundos -= 1
    if segundos >= 0:
        print(segundos)
        print(atras(segundos))
    else:
        print('Termino la cuenta') 

print(atras(10)) 

e = int("15")
print(e)

print(bin(15)) #Enteros a binarios
print(hex(15)) #Enteros a hexadeciamles
print(abs(-10)) # valor absolutos 
print(round(5.5)) #Redondear valores 
print(len("alvaro")) #Hallar la cantidad de caracteres
#help()
