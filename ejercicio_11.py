# Inicialización de variables para acumular datos y contabilizar resultados
cantidad_hombres = cantidad_mujeres = altura_mayor_170 = altura_menor_150 = 0
suma_alturas = cantidad_alumnos = 0

# Bucle para ingresar datos de los alumnos
while True:
    edad = int(input("Ingrese la edad del alumno (0 para salir): "))
    if edad == 0:
        break
    
    sexo = input("Ingrese el sexo del alumno (hombre/mujer): ")
    altura = float(input("Ingrese la altura del alumno (en metros): "))
    
    # Contabilizar el sexo del alumno
    if sexo.lower() == 'hombre':
        cantidad_hombres += 1
    else:
        cantidad_mujeres += 1
    
    # Acumular datos para calcular el promedio de altura y contadores específicos
    suma_alturas += altura
    cantidad_alumnos += 1
    if altura > 1.70:
        altura_mayor_170 += 1
    elif altura <= 1.50:
        altura_menor_150 += 1

# Cálculo y presentación de resultados
if cantidad_alumnos > 0:
    print(f"Cantidad de hombres: {cantidad_hombres}")
    print(f"Cantidad de mujeres: {cantidad_mujeres}")
    print(f"Altura promedio: {suma_alturas / cantidad_alumnos:.2f}")
    print(f"Alumnos con altura mayor a 1.70 metros: {altura_mayor_170}")
    print(f"Alumnos con altura menor o igual a 1.50 metros: {altura_menor_150}")
else:
    print("No se ingresaron datos de alumnos.")
