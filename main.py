import os

#Controlador
from Controlador.controlador_juego import Controlador_juego

#Modelo
from Modelo.validaciones import Validaciones

#Vista
from Vista.mensajes import Mensajes
from Vista.vista_cli import Menus, Vista_CLI
from Vista.vista_gui import Vista_GUI



def main():
    os.system("cls")

    vista_temp = Vista_CLI()
    interfaz = vista_temp.menu_interfaz()

    #Provisional
    #print(Mensajes.TITULO)
    #interfaz = Menus.menu(Menus.menu_interfaz)
    #while True: # Bucle provisional ---- ES PROVISIONAL

    if (interfaz == 1):
        vista = Vista_CLI()
        controlador = Controlador_juego(vista)
        controlador.iniciar_juego()
        
    elif (interfaz == 2):
        vista = Vista_GUI()
        controlador = Controlador_juego(vista)
        
        # Lanzar el juego sin bloquear la GUI
        vista.root.after(100, controlador.iniciar_juego)
        vista.iniciar()


    else:
        print("Adiós. No hay partida")

    # Del menú CLI provisional   
    #controlador = Controlador_juego(vista)
    #controlador.iniciar_juego()

if __name__ == "__main__":
    main()