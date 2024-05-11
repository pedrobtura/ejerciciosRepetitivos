contamarilla=0
controsa=0
controja=0
contverde=0
contazul=0

for i in range(20):
    placaFinal = int(input("Ingrese el último número de su placa: "))
    if placaFinal == 1 or placaFinal == 2:
        contamarilla +=1
    elif placaFinal == 3 or placaFinal == 4:
        controsa +=1
    elif placaFinal == 5 or placaFinal == 6:
        controja +=1
    elif placaFinal == 7 or placaFinal == 8:
        contverde +=1
    elif placaFinal == 9 or placaFinal == 0:
        contazul +=1
        
print("Las calcomanias amarillas de los autos son: ", contamarilla)
print("Las calcomanias rosas de los autos son: ", controsa)
print("Las calcomanias rojas de los autos son: ", controja)
print("Las calcomanias verdes de los autos son: ", contverde)
print("Las calcomanias azules de los autos son: ", contazul)