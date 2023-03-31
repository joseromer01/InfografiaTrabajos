import time
import random

class Personaje:
    def __init__(self, nombre, vitalidad):
        self.nombre = nombre
        self.vitalidad = vitalidad
    
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def esta_vivo(self):
        return self.vitalidad > 0

class Jugador(Personaje):
    def __init__(self, nombre, vitalidad, habilidades):
        super().__init__(nombre, vitalidad)
        self.habilidades = habilidades
    
    def recibir_daño(self, daño):
        self.vitalidad -= daño

    def listar_habilidades(self):
        for h in self.habilidades:
            print(f"Puedo {h}")

    def contraatacar(self, enemigo):
        print(f"¡Contraataque exitoso! {self.nombre} ataca a {enemigo.nombre}")
        daño_base  = random.randint(1, 10)
        es_critico = random.choice([True, False])
        if es_critico:
            print("ataque crítico")
            daño_total = daño_base * 3  
        else:
            print("ataque normal")
            daño_total = daño_base 
        enemigo.vitalidad -= daño_total
        if not enemigo.esta_vivo():
            print(f"Enemigo {enemigo.nombre} ha sido derrotado")
            return False
        return True
       

class Enemigo(Personaje):
    def __init__(self, nombre, vitalidad, daño, ataque_esp):
        super().__init__(nombre, vitalidad)
        self.daño = daño
        self.ataque_esp = ataque_esp
    
    def atacar_jugador(self, jugador):
        daño_aleatorio = random.randint(1, 10)
        daño_total =  daño_aleatorio 
        print(f"Enemigo {self.nombre} atacando a jugador {jugador.nombre} con daño: {daño_total}")
        jugador.recibir_daño(daño_total)

jugador = Jugador("Juan", 100, ["atacar", "volar", "esquivar"])
jugador.listar_habilidades()
jugador.saludo()

enemigo = Enemigo("Raul", 100, 0, 70)

while jugador.esta_vivo():
    enemigo.atacar_jugador(jugador)
    print(f"vitalidad {jugador.nombre}: {jugador.vitalidad}")
    time.sleep(2)
    if not enemigo.esta_vivo():
        print(f"¡El jugador {jugador.nombre} ha ganado! El enemigo {enemigo.nombre} ha sido derrotado.")
        break

    jugador.contraatacar(enemigo)
    print(f"vitalidad {enemigo.nombre}: {enemigo.vitalidad}")
    time.sleep(2)

if jugador.esta_vivo():
    print(f"El jugador {jugador.nombre} ha derrotado al enemigo {enemigo.nombre}.")
else:
    print(f"El jugador {jugador.nombre} está muerto.")




# EJERCICIO:
# Modificar este programa para agregar las siguientes caracteristicas:
# 1. Agregar logica de daño aleatorio al enemigo.
# 2. Agregar lógica de contraataque del jugador.
# 3. Agregar posibilidad de daño crítico en contra ataque del jugador.