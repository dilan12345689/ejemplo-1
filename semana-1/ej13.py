import random

player = input("Tu jugada: ").lower()
machine = random.choice(["piedra", "papel", "tijera"])

print(player, machine)

if player == machine:
    print("Empate")
elif (player == "piedra" and machine == "tijera") or \
     (player == "tijera" and machine == "papel") or \
     (player == "papel" and machine == "piedra"):
    print("Ganaste")
else:
    print("perdiste")