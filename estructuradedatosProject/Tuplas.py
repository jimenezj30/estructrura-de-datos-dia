#tuplas
tupla1 = () #definicion de una tupla vacia
print(tupla1)

print("-----------------------------------")

tupla2 = ("una caseta",123,4.9,True) #una tupla heterogenea
print(tupla2)
print(tupla2[1]) #accede al elemecnto de la tupla
print(tupla2[2])
print(tupla2[3])

print("-----------------------------------")

#enlazar tuplas
tupla3 = (0,1,2,3)
tupla4 = ("A","B","C")
tupla5 = (tupla3,tupla4)
print(tupla5)
print(tupla5[1][1])#muestra de la tupla 2 el elemento em el indice 1
print(tupla5[1][0])#muestra de la tupla 2 el elemento em el indice 0
print(tupla5[0][3])#muestra de la tupla 1 el elemento em el indice 3

print("-----------------------------------")

#operaciones con tuplas
tupla6 = ("A","B","C","D","E")
tupla7 = (1,2,3,4,5)
tupla8 = tupla6 + tupla7 #comcatenar
print(tupla8)
print(tupla8[8])

print("-----------------------------------")

#repetir una tupla
tupla9 = (1,2,3,4,5)
tupla10 = tupla9 * 3
print(tupla10)

print("-----------------------------------")

#comparar una tupla
tupla11 = ("Rojas",)
tupla12 = (123,)
tupla13 = ("Rosas",)
tupla14 = ("rosas",)

print((tupla11,tupla12) < (tupla13,tupla14))

print("-----------------------------------")

print((tupla13,tupla14) == (tupla11,tupla12))











