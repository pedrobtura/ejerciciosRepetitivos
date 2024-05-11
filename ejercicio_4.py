#Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto.
numero=int(input("Ingrese el número del cual desea obtener la tabla de multiplicar " )) #Solicitar el numero por teclado
for i in range(1,11): #Iterar datos del 1 al 10 para realizar la tabla
    multipl=numero*i #Multiplicar el valor numero por el valor i en las iteraciones
    print(numero, "x", i, "=", multipl) #Solicitar la impresión de los valores