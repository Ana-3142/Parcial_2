#1.- Funcion que no recibe parametros y no regresa valor

import modulos

def modulos.borraPantalla():
    def modulos.funcion1()

def funcion1():
    nombre=input("Nombre: ").upper().strip()
    apellidos=input("Apellidos: ").upper().strip()
    print(f"El nombre del alumno es: {nombre} {apellidos}")

 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nom,ape):
    nombre=nom
    apellidos=ape
    print(f"El nombre del alumno es: {nombre} {apellidos}")

 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    nombre=input("Nombre: ").upper().strip()
    apellidos=input("Apellidos: ").upper().strip()
    return nombre,apellidos
 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
    nombre=nom
    apellidos=ape
    return nombre,apellidos
#Invocar las funciones
funcion1()

nombre=input("Nombre: ").upper().strip()
apellidos=input("Apellidos: ").upper().strip()
funcion3(nombre,apellidos)

nombre,apellidos=funcion2()
print(f"El nombre del alumno es: {nombre} {apellidos}")

nom=input("Nombre: ").upper().strip()
ape=input("Apellidos: ").upper().strip()
nombre,apellidos=funcion4(nom,ape)
print(f"El nombre del alumno es: {nombre} {apellidos}")# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

