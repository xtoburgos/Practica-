#adivina el numero

import random

def introduccion ():
    print("Jueguemos a adivina el numero")
    print("Tendras que adivinar un numero en el rango de  1 - 100 ")

def seleccion():
    seleccion = random.randint(1,100)
    return seleccion 

def condiciones (seleccion):
    intento = int(input("Adivina! \n =>"))
    contador = 2
    while contador != 0:
        if seleccion > intento:
            print(f"El numero que selecciono es menor , te quedan {contador} intentos")
            intento = int(input("Adivina! \n =>"))
        elif seleccion < intento :
            print (f"el nuemro que selecciono es mayor, te quedan {contador} intentos")
            intento = int(input("Adivina! \n =>"))
        else:
            break
        contador = contador -1
    if seleccion == intento:
        print ( "Usted ha adivinado el numero")
    else :
        print(f"Lo sentimos pero el numero correcto era : {seleccion}")

def main ():
    condicion = "s"
    introduccion()
    while condicion == "s":
        selec = seleccion()   
        condiciones(selec)
        condicion = input("Quieres jugar de nuevo [s/n]")
        
if __name__=="__main__":
    try :
        main()
    except:
        pass



