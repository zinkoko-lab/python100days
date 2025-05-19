def is_prime(num):
    # list of numbers except num and 1
    other_numbers = list(range(2, num))
    check_prime = sum([True for _ in other_numbers if num % _ == 0])
    if check_prime > 0:
        return False
    else:
        return True

print(is_prime(73))

print(is_prime(75))
