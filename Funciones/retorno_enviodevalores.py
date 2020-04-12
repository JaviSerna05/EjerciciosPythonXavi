def estudiante():
    return "Mis estudiantes son unos genios"
estudiante()    

print(estudiante())

def estudiantes():
    return [5,6,4,7]

print(estudiantes()[0:2])   

def estudiantess():
    return "Alvaro Chirou",'Mis estudiantes',10,[5,6,4,7]

print(estudiantess())

a,b,c,d = estudiantess()

def suma(i,x):
    return i+x
print(suma(5,5))