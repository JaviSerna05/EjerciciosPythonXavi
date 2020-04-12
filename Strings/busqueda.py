mensaje = "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"

#resultado = mensaje.count("texto")#Devuelve un valor entero
#resultado = "texto" in mensaje #Devuelve un valor booleano
#resultado = mensaje.find("texto") #Devuelve la posicion
#resultado = mensaje[resultado: resultado + len("texto")]# Se usa para imprimir en pantalla "Texto"
#resultado = mensaje.find("codigo")#Me devuelve un -1 quiere decir no existe
#resultado = mensaje.startswith("Este")#Nos retorna un valor booleano
resultado = mensaje.endswith("e")#

print(resultado)