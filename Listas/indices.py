cursos = ["python","django", "flask", "C", "C++", "C#", "java", "php"]

cursos = cursos [0:4:2]
print(cursos)

cursos = cursos [::-1] # Esto sirve para observar todo de fin a principio
print(cursos)

"""
Sub-listas
[:]--> Todo los elementos
[start:]--> Todos los elementos desde el indice establecido
[:end]--> Todos los elementos desde el indice cero hasta el indice establecido
[start:end]--> Todos los elementos de un rango indices
[start:end:step]--> Todos los elementos de un rango de indices con saltos
De igual forma, este listado es aplicable a las tuplas y los strings 
"""