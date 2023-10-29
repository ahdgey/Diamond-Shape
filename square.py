n = int(input("\033[1;35mEnter the side length of the square: "))

if n <= 0:
    print("\033[1;35mKindly enter a positive side length.")
else:
    for i in range(n):
        if i == 0 or i == n - 1:
            print("x" * n)
        else:
            print("x" + " " * (n - 2) + "x")
