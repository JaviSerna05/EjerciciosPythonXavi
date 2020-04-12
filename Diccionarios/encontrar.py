diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}
#resultado = diccionario["a"] #Si coloco una llave que no existe me muestra error
#resultado = "z" in diccionario ##Sirve para ubicar llaves en los diccionarios
#resultado = diccionario.get("a")#Podemos indicar segundos valores puede ser cualquier tipo de dato; Forma recomendada 
resultado = diccionario.setdefault("z", {})

print(resultado)

