

# Aquí está la clase padre Personaje
# Se produce la herencia
# Esta es la clase padre de Jugador y Enemigo



# Clase padre Personaje
class Personaje:
  def __init__(self, nombre, vida, vida_max, ataque, pociones, estoyVivo, contador_ataques=0):
    self.nombre = nombre
    self.vida = vida
    self.vida_max = vida_max
    self.ataque = ataque
    self.pociones = pociones
    self.estoyVivo = estoyVivo
    self.contador_ataques = contador_ataques

  def recibir_daño():
    pass

  def usar_pocion():
    pass

  def estar_vivo(self, vida): #Este método informa si el personaje sigue vivo o ha muerto
    if (vida <= 0):
      return False
    else:
      return True

# Probando el constructor
nuevo = Personaje("guerrero",1,2,3,4,True)
print(nuevo.__dict__)

