# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        # print(f"number = {number}", end=': ')
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

end = 20
fizz_buzz(end)
