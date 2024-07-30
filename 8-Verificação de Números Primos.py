#Verificação de Números Primos
#Crie uma função que verifique se um número é primo.

def is_prime(n):
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

if __name__ == "__main__":
    test_numbers = [2, 3, 4, 5, 16, 17, 18, 19, 20]
    for num in test_numbers:
        print(f"{num} é primo? {is_prime(num)}")
