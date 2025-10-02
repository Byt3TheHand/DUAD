import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for divisor in range(3, sqrt_n + 1, 2):
        if n % divisor == 0:
            return False
    return True

def filter_primes(numbers):

    return [num for num in numbers if is_prime(num)]

if __name__ == "__main__":
    list = [1, 4, 6, 7, 13, 9, 67]
    prime = filter_primes(list)
    print(f"Primos encontrados: {prime}")