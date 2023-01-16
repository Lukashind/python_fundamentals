quantity = int(input())
days = int(input())
need_money = 0
points = 0

for c in range(1, days + 1):
    if c % 2 == 0:
        need_money += quantity * 2
        points += 5
    elif
