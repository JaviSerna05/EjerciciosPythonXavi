lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++" #Split

separador = "; "
resultado = lenguajes.split(separador) # resultado es una lista

nuevo_string = separador.join(resultado)

texto = """Este es un texto
con
saltos
de

linea"""
conclusion = texto.splitlines()
print(conclusion)

#print(resultado)
#print(nuevo_string)
#Con estos metodos se pueden convertir los strings a listas y viceversa