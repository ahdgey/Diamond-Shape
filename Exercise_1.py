def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

num = input("\033[1;36mKindly type in an integer: ")

if num.isdigit():
    num = int(num)
    if is_prime(num):
        print("\033[1;32mPrime")
    else:
        print("\033[1;31mNot prime")
else:
    print("Invalid input. Please enter a valid integer.")
