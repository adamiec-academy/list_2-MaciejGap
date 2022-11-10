def is_diabolic(n):
    return "666" in str(n)


def is_prime(n):
    if n < 2:
        return False
    for number in range(2, n):
        if n % number == 0:
            return False
    return True


for i in range(1, 100001):
    if is_diabolic(i) and is_prime(i):
        print(i)
