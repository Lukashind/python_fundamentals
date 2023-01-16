budget = float(input())
flour_price = float(input())
loaves_count = 0
rest_budget = budget
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 * 0.25
loaves_price = flour_price + eggs_price + milk_price
colored_aggs_qt = 0

while 0 < rest_budget > loaves_price:
    rest_budget -= loaves_price
    loaves_count += 1
    colored_aggs_qt += 3
    if loaves_count % 3 == 0:
        colored_aggs_qt -= loaves_count - 2

print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_aggs_qt} eggs and {rest_budget:.2f}BGN left.")
