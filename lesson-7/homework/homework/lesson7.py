1. is_prime(n) funksiyasi
Bu funksiya n > 0 bo‘lishi sharti bilan berilgan sonning tub (prime) yoki yo‘qligini tekshiradi.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Misollar:
print(is_prime(4))  # False
print(is_prime(7))  # True

2.
def digit_sum(k):
    return sum(int(digit) for digit in str(k))

# Misollar:
print(digit_sum(24))   # 6 (2 + 4)
print(digit_sum(502))  # 7 (5 + 0 + 2)
3.
def print_powers_of_two(N):
    k = 1
    result = []
    while (2 ** k) <= N:
        result.append(2 ** k)
        k += 1
    print(*result)

# Misol:
print_powers_of_two(10)  # Natija: 2 4 8
