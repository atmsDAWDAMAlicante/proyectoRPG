from Modelo.personaje import Personaje


# Clase Enemigo

class Enemigo(Personaje):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    #self.contador_ataques = 0


  def decidir_accion(self,atacante): # Aquí viene lo bueno

    if (atacante.vida + 3 < atacante.vida_max) and (atacante.pociones > 0):
      return 3 # Tomate la poción

    elif (atacante.contador_ataques >= 3):
      return 2 # Tira el Ataque Cargado
    
    elif (atacante.vida + 3 > atacante.vida_max) and (atacante.pociones > 0) and (atacante.contador_ataques >=3):
      return 2 # Tira el Ataque Cargado
    
    else: # En los demás casos ¡ATACA!
      return 1


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
      return Enemigo(**la_partida_guardada)