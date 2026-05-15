# Vista CLI - para la versión CLI... empezamos por aquí

from Modelo.validaciones import Validaciones


class Menus: #Métodos estáticos
  
  # Variables que contienen los menús para ejecutar con el método de esta clase y validaciones del Modelo
  menu_interfaz = {"texto": "Elige: 1-CLI / 2-GUI / 0-Salir", "lim": 2} # tipo de menu
  menu_iniciar_juego = {"texto": "Elige: 1-Iniciar juego / 2-Guardar partida / 3-Continuar partida /4-Cargar partida / 0-Salir", "lim": 4} # Controlador 
  menu_combate = {"texto": "Elige: 1-Ataque / 2-Ataque Cargado / 3-Pocion / 4-Kame-Hame / 0-Salir", "lim": 5} # Guardar/Cargar - JSON
  menu_personajes = {"texto": None, "lim": 0}

  # Método estático: generador de menús que llama a las validaciones en el Modelo
  @staticmethod
  def menu(menu_activo):

    sufijo = ": "

    opcion_menu = input(f'{menu_activo['texto']}{sufijo}')
    sufijo = ": "
    tipo_validado = Validaciones.validar_menu_en_rango(opcion_menu, menu_activo['lim'])
    while (tipo_validado == False):
      sufijo = ", otra vez: " # Sufijo del menú para indicar que es una reiteración
      opcion_menu = input(f'{menu_activo['texto']}{sufijo}')
      tipo_validado = Validaciones.validar_menu_en_rango(opcion_menu, menu_activo['lim'])
    return int(opcion_menu)
  

class Vista_CLI:

    def menu_interfaz(self):
      return Menus.menu(Menus.menu_interfaz)

    def menu_iniciar_juego(self):
      return Menus.menu(Menus.menu_iniciar_juego)


    def menu_elegir_jugador(self,menu):
      #return Menus.menu(Menus.menu_personajes)
      return Menus.menu(menu)
    
    def menu_combate(self):
      return Menus.menu(Menus.menu_combate)

    def imprimir_mensaje(self, mensaje): # En esta clase está el método para IMPRIMIR POR PANTALLA
      print(mensaje)

  