#se importa la libreria de random
import random

#se crean las variables
intentos = 0
numero = random.randint(1,10)
elejido = -1

print("Adivine el numero del 1 al 10!")
#se incrementa un bucle,mientras elejido sea distinto de numero se repetira una y otra vez
while elejido != numero:
    elejido = int(input("Ingrese un numero: "))
    #por cada que el usuario ingrese una respuesta se incrementara 1 al contador
    intentos = intentos + 1
    if elejido == numero:
        print(f"Usted Gano!,su numero de intentos es de: {intentos}")
    else:
        if numero > elejido:
            print("El numero es mayor")
        else:
            if numero < elejido:
                print("El numero es menor")
    





