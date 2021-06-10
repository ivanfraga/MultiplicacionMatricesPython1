'''altura = float(input("Dime tu altura: "))
peso = float(input("Dime tu peso: "))
imCorporal = round(peso/altura, 2)

print("Tu indice de masa corporal es: "+ str(imCorporal))
type(imCorporal)'''
#comentario = " Soy un cacahuateeee siii! "
'''
print(comentario)
print(comentario[4:])
print(comentario[:4])
print(comentario[-5:])
print(comentario[:-5])
print(comentario[5:11])'''
#print(comentario.replace("siii", "nooo"))
'''print(comentario.strip())
a= [1, 2, 5]
b= ['f', 'g','h']
x= [a, b]
print(x)
print(x[0][2])
a = [1,5,6,4,1,8]
b= ['perro', 'rata', 'raposa']'''

import numpy
import sys
print("MULTIPLICACIÓN DE MATRICES")
#Ingreso de número de filas y columnas de las 2 matrices
fila1 = int(input('Ingresa el numero de filas de la matriz 1: '))
colum1 = int(input('Ingresa el numero de columnas de la matriz 1: '))
fila2 = int(input('Ingresa el numero de filas de la matriz 2: '))
colum2 = int(input('Ingresa el numero de columnas de la matriz 2: '))
#Verificación si la multiplicación es posible
if (colum1 == fila2):
    matriz1= numpy.zeros((fila1,colum1))
    matriz2 = numpy.zeros((fila2, colum2))
    matrizr = numpy.zeros((fila1, colum2))
    print("Introduce los elementos de la matriz 1: ")
    for r in range(0,fila1):
        for c in range (0,colum1):
            matriz1[r,c]= int(input(f"Elemento a[{r+1}, {c+1}]: "))
    print("Introduce los elementos de la matriz 2: ")
    for r in range(0, fila2):
        for c in range(0, colum2):
            matriz2[r, c] = int(input(f"Elemento b[{r + 1}, {c + 1}]: "))
    #Multiplicacion de las matrices

    for r in range (0, fila1):
        for c in range (0, colum2):
            for k in range(0,fila2):
                matrizr[r,c]+= matriz1[r,k] * matriz2[k,c]
    print(matrizr)
else:
    print("Las columnas de la matriz 1 y las filas de la matriz 2 deben ser iguales")

