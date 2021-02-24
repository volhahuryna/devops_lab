number = int(input())
factorial = 1
for element in range(1, number + 1):
    if element > 0:
        factorial = factorial * element
    else:
        factorial == 1
print(factorial)
