calificaciones = {"calculo": 10, "dibujo": 5}

sumaCalificaciones = calificaciones.get("calculo") + calificaciones.get("dibujo")
totalNota = sumaCalificaciones / 2
print("El promedio mayor es calculo: ", calificaciones.get("calculo"), '\n', calificaciones.get("dibujo"), '\n', totalNota) 