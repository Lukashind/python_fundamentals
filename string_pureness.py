n = int(input())

for x in range(1, n + 1):
    input_line = input()
    for chr in input_line:
        if chr == "." or chr == "," or chr == "_":
            print(f"{input_line} is not pure!")
            break
    else:
        print(f"{input_line} is pure.")


