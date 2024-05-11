#Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un total de n personas.
import random

mujeres=0
hombres=0

for i in range(50):
    genero= random.choice(["hombre", "mujer"])
    if genero == "hombre":
        hombres +=1
    elif genero == "mujer":
        mujeres +=1

print("Cantidad de hombres, ", hombres)
print("Cantidad de mujeres, ", mujeres)