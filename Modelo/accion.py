
from Vista.mensajes import Mensajes

# Módulo para gestionar las acciones: ataques y curarse con la poción

# clase padre Accion(combate)
class Accion: # sin constructor
  def ejecucion(self):
    return

class Ataque(Accion):
  def ejecutar(self, atacante, defensor):
    # El ataque normal reduce un punto la vida del oponente
    defensor.vida -= 1 
    # El ataque normal suma uno el contador del ataque cargado salvo que ya haya alcanzado 3
    if (atacante.contador_ataques >=3):
      atacante.contador_ataques = 3 # Si tienes 3, te quedas con tres hasta que lo tires
    else:
      atacante.contador_ataques += 1
    
class Ataque_Cargado(Accion):
  def ejecutar(self, atacante, defensor,vista):
    # Si tienes el ataque cargado entonces le quitas 5 puntos de vida al oponente
    # y se te pone a cero el marcador
    if (atacante.contador_ataques > 2):
      defensor.vida -=5
      atacante.contador_ataques = 0
    else: # En caso contrario, no hace nada y pierdes el turno
      vista.imprimir_mensaje(f"Te falta/n {3-atacante.contador_ataques} Petit-Suis para tener el ataque cargado\nY pierdes el turno")
      #defensor.vida -= 1
      atacante.contador_ataques += 1

class Usar_Pocion(Accion):
  def ejecutar(self, atacante, defensor,vista):
    # Sólo hay dos pociones que devuelven 3 puntos de vida
    if (atacante.pociones > 0):
      atacante.pociones -= 1
      vista.imprimir_mensaje(f"Has gastado una poción. Te quedan {atacante.pociones} pociones")
      atacante.vida +=3
      if (atacante.vida > atacante.vida_max): # La poción no da más vida que la máxima
          atacante.vida = atacante.vida_max
      
    else:
      #print(f"No te quedan pociones") # Sin pociones pierdes el turno
      vista.imprimir_mensaje("No te quedan pociones")
      
    
    
class Kame_Hame(Accion): # El Easter Egg para pasar el juego rapidito
  def ejecutar(self, atacante, defensor):
    defensor.vida = 0

