import sys
import random

stake = int(sys.argv[1])
goal = int(sys.argv[2])
trails = int(sys.argv[3])
wins = 0
bets = 0

for t in range(trails):
    cash = stake
    while cash > 0 and cash < goal:
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1
print("chance :" + str(100 * wins // trails) + "%")
print("trails :" + str(bets // trails) + " times")
