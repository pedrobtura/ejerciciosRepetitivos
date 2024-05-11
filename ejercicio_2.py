#Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos números.
cont= 0 #Se crea un contador 
for i in range(-15,-4): #Se leen 10 números negativos
    i *= -1 #Para poder convertir los números de negativos a positivos se multiplica cada iteración por -1
    cont +=i #En el contador vamos sumando los números iterados previamente convertidos a positivo
    print(i) #Se imprimen los números en positivo
print("La suma de los números en positivo es: ", cont) #Se imprime la suma de los números en positivo