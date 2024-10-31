#DEFINICION DE UNA LISTA

lista = [] #esto es una lista vacia
lista1 = ["este es un texto"] #una lista con un elemento
lista2 = ["una cadena",123] #una lista de dos elementos
lista3 = [1, 2, 3,4,5,"hola","a"] #una lista de seis elementos

print(lista)
print(lista1)
print(lista2)
print(lista3)

lista5 = [0,1,2,3]
lista6 = ["A","B","C"]
lista7 = [lista5,lista6]
print(lista7)
print(lista7[0]) #muestra lista5
print(lista7[1]) #muestra lista6
print(lista7[1][0]) #muestra lista6 elemento indice 0

#OPERACIONES CON LISTAS
#concatenacion
lista8 = ["A","B","C","E"]
lista9 = [1,2,3,4,5]
lista10 =lista8 + lista9
print(lista10)
print(lista10[2])

#el metodo extend agrega un alista al final de otra lista, la operacion afecta la lista invocante
nombres1 = ["Antonio","Maria","Mabel"]
nombres2 = ["Barry","John","Guttag"]
#nombres3 = ["Barry","John","Guttag"]
nombres1.extend(nombres2)
print(nombres1)
print(nombres2)

#Repetir
lista11 = [1,2,3,4,5]
lista12 = lista11 * 3
print(lista12)

# Comparacion
    # #Usando los operadores convencionales(<, <=,>,>=,==,!=)
print(["Rojas", 123] < ["Rosas", 123])
print(["Rosas", 123] == ["rosas", 123])
print(["Rosas", 123] > ["Rosas", 23])

    # Es posible determinar si un elemento se encuentra en una lista
lista13 = ["cien", "años", "de", "soledad"]
if "de" in lista13:
    print("si esta en la lista")
else:
    print("No esta en la lista")

    #Iterando una lista
lista15 = ["hola", "amigos", "mios"]
for palabra in lista15: #para cada palabra de la lista
    print(palabra, end=",") #parametro end evita salto de linea