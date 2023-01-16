number_orders = int(input())
total_price = 0
for _ in range(1, number_orders + 1):
    capsule_price = float(input())
    days = int(input())
    capsule_per_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsule_per_day < 1 or capsule_price > 2000:
        continue

    cost = capsule_price * days * capsule_per_day
    total_price += cost
    print(f"The price for the coffee is: ${cost:.2f}")
print(f"Total: ${total_price:.2f}")
