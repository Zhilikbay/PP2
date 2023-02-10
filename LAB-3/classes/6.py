def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

numbers = [12, 17, 19, 21, 25, 29.31,32]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers) 