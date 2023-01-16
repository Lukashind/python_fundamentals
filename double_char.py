while True:
    input_line = input()
    if input_line == "End":
        break
    if input_line == "SoftUni":
        continue
    for chr in input_line:
        print(f"{chr}{chr}", end="")
    print()






