#Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros
positivos= 0
negativos= 0 #Realizo 3 contadores donde se incluya positivos, negativos y neutros
neutros= 0

for i in range (-11,8): #Itero 20 datos donde hay datos negativos, neutros y positivos.
    if i<0: #Creo la primera condición en la que el número iterado sea menor a 0
        negativos +=1 #Si la condición se cumple se aumenta 1 en el contador negativos
    elif i == 0: #Creo la segunda condición en la que el número iterado sea igual a 0
        neutros +=1 #Si la condición se cumple se aumenta 1 en el contador neutros
    elif i>0: #Creo la primera condición en la que el número iterado sea mayor a 0
        positivos +=1 #Si la condición se cumple se aumenta 1 en el contador positivos
        
print("Los números positivos son ", positivos)
print("Los números negativos son ", negativos) #Se solicita la impresión de los valores obtenidos
print("Los números neutros son ", neutros)