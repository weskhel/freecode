import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

call_1, call_2 = input().split()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


if call_1 == call_2:
    print(f"Empate")
elif call_1 == "ROCK":
    if call_2 == "SCISSORS":
        print("PLAYER1")
    else:
        print("PLAYER2")

elif call_1 == "PAPER":
    if call_2 == "ROCK":
        print("PLAYER1")
    else:
        print("PLAYER2")

elif call_1 == "SCISSORS":
    if call_2 == "PAPER":
        print("PLAYER1")
    else:
        print("PLAYER2")
