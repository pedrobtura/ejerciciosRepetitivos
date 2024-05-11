suma_edades_hombres = 0
suma_edades_mujeres = 0
contador_hombres = 0
contador_mujeres = 0

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

for _ in range(cantidad_alumnos):
    edad = int(input("Ingrese la edad del alumno: "))
    genero = input("Ingrese el género del alumno (h para hombre, m para mujer): ").lower()
    
    if genero == 'h':
        suma_edades_hombres += edad
        contador_hombres += 1
    elif genero == 'm':
        suma_edades_mujeres += edad
        contador_mujeres += 1
    else:
        print("Género no válido. Se ignorará este alumno.")

promedio_edad_hombres = suma_edades_hombres / contador_hombres 
promedio_edad_mujeres = suma_edades_mujeres / contador_mujeres 
promedio_edad_total = (suma_edades_hombres + suma_edades_mujeres) / cantidad_alumnos

print("Promedio de edad de hombres:", promedio_edad_hombres)
print("Promedio de edad de mujeres:", promedio_edad_mujeres)
print("Promedio de edad total del grupo:", promedio_edad_total)
