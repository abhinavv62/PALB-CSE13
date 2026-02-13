def factorial_digits(n):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return list(map(int, str(result)))


print(factorial_digits(10))
