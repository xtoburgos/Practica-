"""
librerias a exportar 
delimitar espacios de los recuadros ?
definir posiciones del cursor y clicks
definir movimientos 
tiempo de espera para resetear el prog

"""

#librerias
import pyautogui
import time
import asyncio

#desactivar modo a prueba de errores
pyautogui.FAILSAFE = False

#posiciones del cursor y clicks
async def accion( pos_x, pos_y ):
    pyautogui.moveTo(pos_x, pos_y)
    await asyncio.sleep(1)
    pyautogui.click()
    time.sleep(3)

#continuidad de los movimientos 
continuar = True

#tiempo de cambio de pantalla
time.sleep(5)

#movimientos 
while continuar == True:
    episodio_sig = asyncio.run(accion(1785, 250))
    reproducir = asyncio.run(accion(735, 620))
    calidad = asyncio.run(accion(960, 960))
    calidad_seleccion = asyncio.run(accion(960, 730))
    pantalla_completa = asyncio.run(accion(1350, 960))
    reset = asyncio.run(accion(0, 0))
    #Duracion del anime o serie 
    time.sleep(1260)
    pyautogui.press('esc')



