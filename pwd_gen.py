#generador de contraseñas 

from random import *
import string

def contraseña (rango):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(choice(caracteres) for i in range(rango)) 
    return contraseña

def main ():
    print("Bienvenido al generador de contraseñas")
    rango = int(input("Seleccione el numero de caracteres de su contraseña 8-16 \n => "))
    while rango > 16 or rango < 8:
        print("La constraseña  no cuenta con los caracteres necesarios, intentelo de nuevo")
        rango = int(input("Seleccione el numero de caracteres de su contraseña 8-16 \n => "))
    print(f"Su contraseña es : {contraseña(rango)}")

if __name__ == "__main__":
    try:
        main()
    except:
        pass 


    