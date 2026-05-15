



class Combate:
    def __init__(self, jugador, enemigo, resto_enemigos):
        self.jugador = jugador
        self.enemigo = enemigo
        self.resto_enemigos = resto_enemigos
        self.contador_turnos = 0

    def nuevo_enemigo(self):
        if len(self.resto_enemigos) > 0:
            return  self.resto_enemigos.pop(0)
            #return True
        #return False
