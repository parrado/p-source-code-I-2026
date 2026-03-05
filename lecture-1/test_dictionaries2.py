# Función para lanazar los dados
def lanzar_dados():
    import random
    return random.randint(1, 6), random.randint(1, 6)

# Lista de jugadores con sus fichas y posiciones
players = [
    {
        "nombre": "Helena",
        "color": "rojo",
       "fichas": [-1,-1,-1,-1 ],
        "fichas_finalizadas": 0
    },
    {
        "nombre": "Alejandro",
        "color": "azul",
        "fichas": [-1,-1,-1,-1 ],
        "fichas_finalizadas": 0
    },
    {
        "nombre": "Viviana",
        "color": "verde",
        "fichas": [-1,-1,-1,-1 ],
        "fichas_finalizadas": 0
    }
]

# Conjuntos que almacena los nombres de todos los jugadores
draw0={player["nombre"] for player in players}

# Ciclo para determinar quién inicia el juego
while len(draw0) > 1:
        highest_score = 0
        # Actualiza el sorteo con los jugadores que empataron en la ronda anterior
        draw1=draw0.copy()
        for player in draw1:
                dice0, dice1 = lanzar_dados()
                if dice0 > highest_score:
                        highest_score = dice0
                        turn=player
                        draw0.clear()
                        draw0.add(player)
                elif dice0 == highest_score:
                        draw0.add(player)


print(f"Es el turno de {turn}!")

# Lanzar los dados para el turno del jugador
dice0, dice1 = lanzar_dados()
print(f'{turn} sacó {dice0} y {dice1}')

# Si sacó dobles, mueve la ficha 0 a la posición 0
if dice0 == dice1:
       for player in players:
              if player["nombre"] == turn:
                     player["fichas"][0] = 0
                     print(f"{turn} mueve ficha 0 a posición 0")
       