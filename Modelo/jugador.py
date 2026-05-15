from Modelo.personaje import Personaje

# Clase Jugador
# En el constructor se le suben los puntos de vida a 100, ataque a 10 y 5 pociones

# Clase jugador
class Jugador(Personaje):

  def __init__(self,**kwargs):
    #super().__init__(nombre, vida, vida_max, ataque, defensa, pociones)
    super().__init__(**kwargs) # Recoge los valores de la clase padre
    # No sobreescribir
    #self.vida = 100
    #self.vida_max = 100
    #self.ataque = 10
    #self.pociones = 5
    #self.contador_ataques = 0

  def ataque_cargado(self):
    print(f"{self.nombre} dispone de ataque cargado")

  def to_dict(self):
    return {
        "nombre": self.nombre,
        "vida": self.vida,
        "vida_max": self.vida_max,
        "ataque": self.ataque,
        "pociones": self.pociones,
        "estoyVivo": self.estoyVivo,
        "contador_ataques": self.contador_ataques
    }

  @staticmethod
  def from_dict(la_partida_guardada):
      return Jugador(**la_partida_guardada)