"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

print("\033c")
set1={"Hola", "123", "Mexico", "Holanda", 123, 3.1416}
print(set1)

set1.add("ganador")
print(set1)

set1.pop()
print(set1) 


#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
def registrar_alumnos_v1():
    correos_utd = []
    
    print("Registro de Alumnos UTD: ")
    print("Escribe 'salir' para terminar de introducir correos: ")
    
    while True:
        email = input("Introduce el email del alumno: ").strip().lower()
        
        if email == 'salir':
            break
            
        
        if not email.endswith("@utd.edu.mx"): 
            print("Error: El correo debe pertenecer a la UTD (@utd.edu.mx).")
        elif email in correos_utd:
            print("Este correo ya fue registrado anteriormente.")
        else:
            correos_utd.append(email)
            print("Correo agregado con éxito.")

    
    print("Lista de Correos UTD")
    if not correos_utd:
        print("No se registraron correos.")
    else:
        for i, correo in enumerate(correos_utd, 1):
            print(f"{i}. {correo}")


registrar_alumnos_v1()



#Solucion 2
def registrar_alumnos_v2():
    lista_recibida = []
    
    while True:
        email = input("Introduce el email del alumno: ").strip().lower()
        
        if email == 'salir':
            break
            
        if email.endswith("@utd.edu.mx"):
            lista_recibida.append(email)
            print("Correo recibido.")
        else:
            print("Error: Correo no válido para la UTD.")

    
    correos_unicos = list(set(lista_recibida))

    
    print("Lista de Correos UTD ")
    if not correos_unicos:
        print("No se registraron correos.")
    else:
        for i, correo in enumerate(correos_unicos, 1):
            print(f"{i}. {correo}")


registrar_alumnos_v2()
  



