# CONTROLADOR QUE GESTIONA EL JUEGO

# Modelo
from Modelo.gestor_personajes import PERSONAJES, Gestor_personajes
from Modelo.combate import Combate
from Modelo.accion import Accion, Ataque, Ataque_Cargado, Usar_Pocion,Kame_Hame
from Modelo.jugador import Jugador
from Modelo.enemigo import Enemigo
from Modelo.gestor_guardado import GestorGuardado

# Vista
from Vista.mensajes import Mensajes
from Vista.vista_cli import Menus, Vista_CLI

class Controlador_juego:

    def __init__(self, vista):
        self.vista = vista
        self.combate = None

    def iniciar_juego(self):
        print("DRAGONES Y MAZMORRAS (el de los 80)")
        while True:
            opcion = self.vista.menu_iniciar_juego()
            if opcion == 1:
                self.nuevo_juego()
            elif opcion == 2:
                self.guardar_partida()
            elif opcion == 3:
                if not hasattr(self, "combate") or self.combate is None:
                #if (self.combate == None):
                    self.vista.imprimir_mensaje("No hay ninguna partida iniciada\nIniciando...")
                    self.nuevo_juego()
                else:
                    self.bucle_combate(self.combate)
            elif opcion == 4:
                self.cargar_partida()
            elif opcion == 0:
                self.vista.imprimir_mensaje("Adiós")
                if hasattr(self.vista, "cerrar"):#Para cerrar la GUI
                    self.vista.cerrar()
                break
            
    def guardar_partida(self):
        if self.combate is None:
            self.vista.imprimir_mensaje("No hay partida que guardar")
        else:
            GestorGuardado.guardar(self.combate)
            self.vista.imprimir_mensaje("Partida guardada")

    def cargar_partida(self):
        try:
            self.combate = GestorGuardado.cargar()
            self.vista.imprimir_mensaje("Partida cargada; ahora selecciona continuar partida")
        except FileNotFoundError:
            self.vista.imprimir_mensaje("No hay partida guardada")


    def preparar_personajes(self):
        #PRIMERA PARTE: Menú
        self.vista.imprimir_mensaje("Empezamos el juego: ELIJE TU JUGADOR: ")
        personajes_partida = Gestor_personajes()
        todos_los_personajes = personajes_partida.obtener_personajes_para_menu_CLI()
        # Aquí se recoge el índice del jugador desde la vista
        numero_jugador = self.vista.menu_elegir_jugador(todos_los_personajes)

        #SEGUNDA PARTE: separar jugador, enemigo (activo) y resto
        # Se saca al jugador del cesto de personajes
        jugador = Jugador(**personajes_partida.obtener_jugador(numero_jugador-1))
        self.tope_power_para_el_jugador(jugador)
        enemigo = Enemigo(**personajes_partida.obtener_enemigo())
        #resto_enemigos = personajes_partida.obtener_resto()
        resto_enemigos = [ #Para recuperar objetos y no diccionarios
            Enemigo(**datos)
            for datos in personajes_partida.obtener_resto()
        ]
        # Esto de abajo para borrar cuando vea que va
        print(enemigo.contador_ataques)
        self.vista.imprimir_mensaje(f'Has escogido a: {jugador.nombre} vida {jugador.vida}')
        self.vista.imprimir_mensaje(f'Tu adversario es: {enemigo.nombre} vida {enemigo.vida}')
        self.vista.imprimir_mensaje(f"{'='*50}\nEMPIEZA EL JUEGO\n{'='*50}")
        # Retornamos los jugadores
        return jugador, enemigo, resto_enemigos
    
    def tope_power_para_el_jugador(self,jugador):
        jugador.vida = 100
        jugador.vida_max = 100
        jugador.pociones = 5

    def nuevo_juego(self):
        # Cogemos los jugadores
        jugador, enemigo, resto_enemigos = self.preparar_personajes()
        
        # IMPORTANTE ENVIO AL ADMINISTRADOR DEL JUEGO DE LOS OBJETOS JUGADOR Y ENEMIGOS
        self.combate = Combate(jugador,enemigo, resto_enemigos) 
        # EMPIEZA LA BATALLA
        self.bucle_combate(self.combate)


    def bucle_combate(self,combate):
        self.combate = combate
        turno = True # Empieza siempre el jugador
        accion = None
        #contador = 0 # contador de las jugadas


        while True:
            self.combate.contador_turnos += 1 # vamos contando las jugadas a título informativo
            contador = self.combate.contador_turnos
            

            if (turno == True): # LE TOCA AL JUGADOR
                # SE DEFINEN LOS ROLES
                atacante = self.combate.jugador
                defensor = self.combate.enemigo

                # MOSTRAR INFORMACIÓN DEL TURNO JUGADOR
                self.vista.imprimir_mensaje(f"{'='*50}\nJugada nº {contador}: turno de {atacante.nombre}")
                self.mostrar_status(atacante, defensor)

                # EMPIEZA EL JUGADOR: SE LE PIDE UNA ACCIÓN
                # ARREGLADO PARA GUI
                acto = self.vista.menu_combate() 

                # Opciones del Menú PARA EL JUGADOR
                if (acto == 1):
                    accion = Ataque()
                    accion.ejecutar(atacante, defensor)

                elif (acto == 2):
                    accion = Ataque_Cargado()
                    accion.ejecutar(atacante, defensor,self.vista)

                elif (acto == 3):
                    accion = Usar_Pocion()
                    accion.ejecutar(atacante, defensor,self.vista)

                elif (acto == 4):
                    accion = Kame_Hame()
                    self.vista.imprimir_mensaje("KAAAAAAME HAAAAAME HAAAAA!!!!!!!")
                    accion.ejecutar(atacante, defensor)

                else: # SALIR DEL JUGADOR
                    print("Fin")
                    break
                

                # CAMBIAMOS EL TURNO
                turno = not turno

            # AHORA LE TOCA AL ENEMIGO
            else: # Cambian las tornas
                atacante = self.combate.enemigo
                defensor = self.combate.jugador

                # MOSTRAR INFORMACIÓN DEL TURNO ENEMIGO
                self.vista.imprimir_mensaje(f"{'='*50}\nJugada nº {contador}: turno de {atacante.nombre}")
                self.mostrar_status(atacante, defensor)
                
                acto = atacante.decidir_accion(atacante) # Se lo piensa
                if (acto == 1):
                    accion = Ataque()
                    accion.ejecutar(atacante, defensor)
                
                elif (acto == 2):
                    accion = Ataque_Cargado()
                    accion.ejecutar(atacante, defensor, self.vista)

                elif (acto == 3):
                    accion = Usar_Pocion()
                    accion.ejecutar(atacante, defensor, self.vista)

                turno = not turno

            #MOSTRAMOS LA ACCIÓN Y EL RESULTADO
            self.vista.imprimir_mensaje(f"--->El {atacante.nombre} ha hecho {accion.__class__.__name__}")
            self.mostrar_status(atacante, defensor)
            
            
            # HAY QUE VER SI ESTÁ VIVO
            if (combate.jugador.estar_vivo(combate.jugador.vida) == False):
                self.vista.imprimir_mensaje(f"{combate.jugador.nombre} HAS MUERTO\nFIN DEL JUEGO")
                break

            elif not combate.enemigo.estar_vivo(combate.enemigo.vida):
                self.vista.imprimir_mensaje(f">>>>>>>>EL POBRE {combate.enemigo.nombre} HA MUERTO")
                nuevo = combate.nuevo_enemigo()

                if not nuevo:
                    self.vista.imprimir_mensaje("¡¡¡HAS DERROTADO A TODOS LOS ENEMIGOS!!!")
                    break

                combate.enemigo = nuevo



    def mostrar_status(self, atacante, defensor):
            self.vista.imprimir_mensaje(f"--{atacante.nombre} vida: {atacante.vida}")
            self.vista.imprimir_mensaje(f"--{defensor.nombre} vida: {defensor.vida}")