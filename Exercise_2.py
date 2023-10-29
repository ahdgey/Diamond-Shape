# Step 1: Input the size of the array
size = int(input("\033[1;33mEnter the size of the array: "))

# Step 2: Input the elements of the array
elements = input("\033[1;33mEnter the elements separated by space: ").split()
elements = [int(e) for e in elements]

# Step 3: Display the cube of each element
for element in elements:
    cube = element ** 3
    print(cube)
