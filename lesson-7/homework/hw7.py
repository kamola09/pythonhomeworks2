def is_prime(n):
    if n <= 1:
        return "Tub son emas"
    for i in range(2, n):
        if n % i == 0:
            return "Tub son emas"
    return "Tub son"

# Funksiyani sinab ko‘rish
print(is_prime(8))   # Natija: Tub son emas
print(is_prime(7))   # Natija: Tub son


def digit_sum(k):
    total = 0
    for i in str(k):
        total += int(i)
    return total

# Funksiyani sinab ko‘rish
print(digit_sum(1234))   # Natija: 10
print(digit_sum(987))    # Natija: 24

def sonning_darajasi(k):
    for i in range(1, k):
        daraja = 2**i
        if daraja <= k:
            print(daraja, end=" ")

# Funksiyani sinab ko‘rish
sonning_darajasi(10)   # Natija: 2 4 8
