califmenor50= 0
calif50menor70= 0
calif70menor80= 0
califmayor80menor100= 0

for i in range (23):
    calificacion= int(input("Ingrese su calificación: "))
    
    if calificacion <= 50:
        califmenor50 +=1
    elif calificacion >= 50 and calificacion <70:
        calif50menor70 +=1
    elif calificacion >= 70 and calificacion <80:
        calif70menor80 +=1
    elif calificacion >= 80 and calificacion <101:
        califmayor80menor100 +=1
        
print("La cantidad de calificaciones menores a 50 son: ", califmenor50)
print("La cantidad de calificaciones entre 50 y 70 son: ", calif50menor70)
print("La cantidad de calificaciones entre 70 y 80 son: ", calif70menor80)
print("La cantidad de calificaciones entre 80 y 100 son: ", califmayor80menor100)