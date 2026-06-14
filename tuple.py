"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis."""



print("\033c")

paises1=("Mexico", "Canada", "EUA")
paises2={"Mexico", "Canada", "EUA"}

print(paises1)
print(paises2)

for i in paises1:
  print(i)

  for i in paises2:
  print(i)

#segundaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

  paises1=("Mexico", "Canada", "EUA")
varios=("Hola", True,33,3.1416)

print(paises1)
print(varios)

for i in paises1:
  print(i) #cuando no me interesa saber posiciones


i=0
  while i<len(paises1):
  print(paises1[i])
i+=1 #no es necesario saber posiciones y beneficia en que se adapta a sus mejoras, como agrandar 


  print(f"El pais que inagura la copa del mundo 2026 es: {paises1[0]}")


edades=(23,24,20,18,23,24,18,19,24)
cuantos=edades.count(24)
print(cuantos)
num=int(input("Ingresa el numero que quieres saber su posicion: ").strip())
posicion=edades.index(numero)
print(f"El numero{numero} se encontro en la posicion: {posicion}")

numero=int(input(Dame el numero a buscar: ).strip())
posiciones=[]
for i in range(0,len(edades)):
  if edades[i]==numero:
    posiciones.append(i)
    posiciones=tuple(posiciones)
    for i in posiciones:
      print(f"El numero {numero} se encontro en la posicion: {i}")

#programando con tuplas