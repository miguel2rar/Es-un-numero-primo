# Es un numero Primo

"""ESCRIBE UN PROGRAMA QUE SE ENCARGUE DE COMPROBAR SI UN NUMERO ES PRIMO O NO
HECHO ESTO ESCRIBE LOS NUMEROS PRIMOS ENTRE 1 Y 100"""


print("Introduce un numero:")
rer = int(input())
tigre= None
lista4 = []
for e in range (0, 100):
    if e == 2 or e == 3 or e == 5:
        lista4.append(e)
    if e % 2 != 0 and e % 3 != 0 and e % 5 !=0:
        lista4.append(e)        
if e == 99:
    print(lista4)
    for z, memoria in enumerate (lista4):
        
        if memoria == rer:
            tigre = memoria

    if tigre == rer:
        print("Es un numero primo")
    else:
        print("No es un numero primo o no esta en el rango de 100")