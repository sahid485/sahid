# Programa de un Conjunto de saludos en donde el usuario ingresa su nombre
# Librerias
import random
# Contenido
print("")
print(" Conjunto de Saludos ")
print("")
# Captura de Datos
nombre = input (" Ingrese Su Nombre Por Favor: ")
saludos = [
    " Bienvenido " + nombre + " , Un Cordial Saludo ",
    " Hola " + nombre + " , ¿ En Que Te Podemos Servir ? ",
    " Es Un Placer Tenerte Nuevamete " + nombre,
    " Hola " + nombre + " , ¿ Cómo Estás ? ",
    " Hola " + nombre + ", ¿ Cómo Te Va ? "
]
# Impresion del conjunto de saludos de forma aleatoria
indice=random.randint(0,len(saludos)-1)
print(saludos[indice])
