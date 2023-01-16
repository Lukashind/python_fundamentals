divisor = int(input())
max_number = int(input())
target_number = 0
for n in range(1, max_number + 1):
    if n % divisor == 0:
        target_number = n
print(target_number)


