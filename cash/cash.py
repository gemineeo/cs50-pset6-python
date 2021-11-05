from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change > 0:
        break
cents = int(change * 100)
coins = 0

while cents > 0:
    if cents >= 25:
        coins += 1
        cents -= 25
    elif cents < 25 and cents >= 10:
        coins += 1
        cents -= 10
    elif cents < 10 and cents >= 5:
        coins += 1
        cents -= 5
    else:
        coins += 1
        cents -= 1

print(f"{coins}")