#piedra papel o tijera 
import random


def jugador ():
    eleccion_jugador = input("Selecciona piedra papel o tijera \n") 
    return eleccion_jugador

def npc ():
    eleccion_npc = random.choice(["piedra","papel","tijera"])
    print (eleccion_npc)
    return eleccion_npc
    
    
def condiciones (jugador , npc):
    if jugador == npc :
        print ("Es un empate")
    else:
        if jugador == "piedra" and npc == "tijera":
            print("Felicidades has ganadado")
        else:
            if jugador == "papel" and npc == "piedra":
                print("Felicidades has ganadado")
            else:
                if jugador == "tijera" and npc == "papel":
                    print("Felicidades has ganadado")
                else:
                    if jugador == "tijera" and npc == "piedra":
                        print("Felicidades has ganadado")
                    else:
                        if jugador == "piedra" and npc== "papel":
                            print("Felicidades has ganadado")
                        else: 
                            if jugador == "papel" and npc== "tijera":
                                print("Felicidades has ganadado")
                
        

def main ():
    print("Jueguemos piedra papel o tijeras las reglas son simples: ")
    print("Puedra > Tijera, Tijera > Papel, Papel > Piedra")
    cond = "s" 
    while cond == "s" :
        jug = jugador()
        non = npc()
        condiciones (jug,non)
        cond = input("Jugamos de nuevo? [s/n] \n")
    

if __name__ == "__main__":
    try:
        main()
    except:
        pass