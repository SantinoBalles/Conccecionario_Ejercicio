print("Bienvenidos al Piedra, Papel o Tijera")

player1 = input("player1: Elija Piedra, Papel o Tijera")
player2 = input("player2: Elija Piedra, Papel o Tijera")

if player2 == "Piedra" and player1 == "Papel":
    print("Ganador player 1")
elif player2 == "Piedra" and player1 == "Tijera":
    print("Ganador player2")
elif player2 == "Papel" and player1 == "Piedra":
    print("Ganador player2")
elif player2 == "Tijera" and player1 == "Piedra":
    print("Ganador player1")
elif player2 == "Papel" and player1 == "Tijera":
    print("Ganador player1")
elif player2 == "Tijera" and player1 == "Papel":
    print("Ganador player2")
else:
    print("lo siento tenes que elejir Piedra, Papel o Tijera")