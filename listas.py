print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

numeros=[23,33,45,8,24,0,100]
print(numeros)

lista="["
for i in numeros:
    print(i)
    lista=lista+str(i)+", "
print(lista+"]")
 


 lista=""
for i in range(0, len(numeros )):
    lista+=f"{numeros[i]}, "
print(lista+"]")


lista=""
while i<= (numeros):
    print(i)
    lista=lista+
print("lista")



#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=["UTD,", "Tercer", "Cuatrimestre", "TI"]
palabra=input("Dame la palabra a buscar: ").strip()


if palabra in palabras
    print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")    


#2DA FORMA
palabras=["UTD,", "Tercer", "Cuatrimestre", "TI"]
palabra=input("Dame la palabra a buscar: ").strip()

for i in palabras:
    if i==palabra:

print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")


 
#3er FORMA

#Ejemplo 3 Añadir elementos a la lista
lista=[]

#opcion1
true=True
while true:
#input trae un string
#while de true or false lanza un si o un no
valor=input("Dame un valor: ").strip()
lista.append(valor)
true=input("Ingresa true/flase para continuar: ").strip()
if true=="False":
    true=False


#opcion2
true="True"
while true=="true":
#input trae un string
#while de true or false lanza un si o un no
valor=input("Dame un valor: ").strip()
lista.append(valor)
true=input("Ingresa true/flase para continuar: ").strip().lower()
if true=="false":
    true=false

    print(lista)
  

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
#multilistas
agenda=[
    ["Carlos", "6181234567"],
    ["Adrian", "6182332456"],
    ["Luis", "6182223444"]
]

print(agenda)

for i in agenda:
    print(i)
    for r in range (1, 3):
        for c in range (0, 2):
            print(agenda[r][c])

#columnas
listas=""
for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c]}, "
        lista+="\n"
        print(lista)


        
