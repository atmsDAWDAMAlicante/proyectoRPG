# Modelo
from Modelo.jugador import Jugador
from Modelo.enemigo import Enemigo

# Los personajes de Dragones y Mazmorras

PERSONAJES = [
    {"nombre": "Arquero", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Barbaro", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Acrobata", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Mago",  "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Ladrona", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True},
    {"nombre": "Caballero", "vida":10, "vida_max":10, "ataque":2, "pociones":2,"estoyVivo": True}
]

class Gestor_personajes:
    def __init__(self):
        self.lista_personajes = self.lista_personajes = [p.copy() for p in PERSONAJES]
        
    def obtener_personajes_para_menu_CLI(self):
        texto_menu = ""
        # Usamos enumerate para obtener el índice y el diccionario del personaje
        for i, personaje in enumerate(self.lista_personajes):
            # i + 1 para que el menú empiece con uno
            # Se forma el string pero con salto de línea para que se vea más bonito
            texto_menu += f"{i + 1} - {personaje['nombre']}\n"
            # Ahora se devuelve un diccionario que es lo que habrá que mandar a la Vista para el menú
        return {"texto":texto_menu,"lim":len(self.lista_personajes)}

    # Devuelve el jugador según el índice
    def obtener_jugador(self, indice_jugador):
        return self.lista_personajes.pop(indice_jugador)

    # Devuelve el primer enemigo del resto de la lista
    def obtener_enemigo(self):
        return self.lista_personajes.pop(0)

    # Devuelve el resto de la lista actualizada
    def obtener_resto(self):
        if (len(self.lista_personajes) > 0):
            return self.lista_personajes.copy()
        else:
            return None
