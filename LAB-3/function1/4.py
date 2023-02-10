def filter_prime(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]
numbers=[1,2,3,4,5,6,7,8,9]
x=filter_prime(numbers)
print(x)