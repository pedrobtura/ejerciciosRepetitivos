#Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos. Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja de todo el grupo.
import random

calificacion_maxima = float('-inf')
calificacion_minima = float('inf')# Inicializar variables para la calificación más alta y más baja
suma_calificaciones = 0

for i in range(20):
    calificacion= round(random.uniform(0.0, 5.0), 1) # Solicitar las calificaciones de los 20 alumnos
    
    print(calificacion) #Solicitar mostrar las calificaciones
    
    if calificacion > calificacion_maxima:
        calificacion_maxima = calificacion
    if calificacion < calificacion_minima:# Actualizar la calificación más alta y más baja
        calificacion_minima = calificacion
    
    # Sumar las calificaciones para calcular el promedio
    suma_calificaciones += calificacion

# Calcular el promedio
promedio = suma_calificaciones / 20

# Solicitar mostrar resultados
print("\nEl promedio de las calificaciones es:", promedio)
print("La calificación más alta es:", calificacion_maxima)
print("La calificación más baja es:", calificacion_minima)    