# Alexza Jean R. Catanoy
# BSCPE 2-4
# Lab Activity: Diamond Shape

# Define 
def print_diamond(n):
    if n % 2 == 0:
        return "Kindly type in an odd integer."
    
    for i in range(n):
        if i < n // 2:
            print(' ' * ((n // 2) - i) + '*' * (2 * i + 1))

        else:
            print(' ' * (i - (n // 2)) + '*' * (2 * (n - i) - 1))

# Print the output for n = 5
print(print_diamond(5))