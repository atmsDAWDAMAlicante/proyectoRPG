import json

from Modelo.jugador import Jugador
from Modelo.enemigo import Enemigo
from Modelo.combate import Combate

class GestorGuardado:
    #MÉTODO ÉSTÁTICO PARA GUARDAR
    @staticmethod
    def guardar(combate, ruta ="partida.json"): # RUTA: donde está el main
        la_partida_guardada = {
            "jugador": combate.jugador.to_dict(),
            "enemigo": combate.enemigo.to_dict(),
            "resto_enemigos":[el_resto.to_dict() for el_resto in combate.resto_enemigos],
            "contador": combate.contador_turnos
        }

        with open(ruta,"w") as f:
            json.dump(la_partida_guardada, f, indent=4)
    
    #MÉTODO ÉSTÁTICO PARA CARGAR
    @staticmethod
    def cargar(ruta="partida.json"):
        with open(ruta, "r") as f:
            la_partida_guardada = json.load(f)

        jugador = Jugador.from_dict(la_partida_guardada["jugador"])
        enemigo = Enemigo.from_dict(la_partida_guardada["enemigo"])
        resto = [Enemigo.from_dict(el_resto) for el_resto in la_partida_guardada["resto_enemigos"]]

        combate = Combate(jugador, enemigo, resto)
        combate.contador_turnos = la_partida_guardada["contador"]

        return combate