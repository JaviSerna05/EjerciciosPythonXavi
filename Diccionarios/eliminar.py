diccionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5,"f": 6,"g": 7,"h": 8}

del diccionario["a"]#1 forma de eliminar
valor = diccionario.pop("b")#2 forma de eliminar
diccionario= {}#3 forma de eliminar (todo)
diccionario.clear()


print(valor)
print(len(diccionario))
print(diccionario)