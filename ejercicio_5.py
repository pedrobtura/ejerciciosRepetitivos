#Una persona debe realizar un muestreo con 50 personas para determinar el promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona. Las categorías se determinar de acuerdo a la siguiente tabla:
import random

contNiños=0
sumaPesoNiños=0
contJovenes=0
sumaPesoJovenes=0
contAdultos=0
sumaPesoAdultos=0
contAncianos=0
sumaPesoAncianos=0

for i in range (1,51):
    edad=random.randint(1,90)
    pesoNiños=random.randint(4,30)
    pesoJovenes= random.randint(31,60)
    pesoAdultos= random.randint(61,70)
    pesoAncianos= random.randint(70,80)
    if edad <12:
        contNiños +=1
        sumaPesoNiños +=pesoNiños
    elif edad >12 and edad <30:
        contJovenes +=1
        sumaPesoJovenes +=pesoJovenes
    elif edad >30 and edad <60:
        contAdultos +=1
        sumaPesoAdultos +=pesoAdultos
    elif edad >60:
        contAncianos +=1
        sumaPesoAncianos +=pesoAncianos
        
promedioNiños=sumaPesoNiños/contNiños
promedioJovenes= sumaPesoJovenes/contJovenes
promedioAdultos= sumaPesoAdultos/contAdultos
promedioAncianos= sumaPesoAncianos/ contAncianos

print("El peso promedio de los niños es: ", promedioNiños, "Kg")
print("El peso promedio de los jovenes es: ", promedioJovenes, "Kg")
print("El peso promedio de los adultos es: ", promedioAdultos, "Kg")
print("El peso promedio de los ancianos es: ", promedioAncianos, "Kg")