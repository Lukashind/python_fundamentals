input_line = input()
coffe_count = 0
while input_line != "END":
    if input_line == "coding" or input_line == "dog" or input_line == "cat" or input_line == "movie":
        coffe_count += 1
    elif input_line == "CODING" or input_line == "DOG" or input_line == "CAT" or input_line == "MOVIE":
        coffe_count += 2
    input_line = input()


if coffe_count > 5:
    print("You need extra sleep")
else:
    print(coffe_count)

