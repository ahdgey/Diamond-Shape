# Alexza Jean R. Catanoy
# BSCPE 2-4
# Lab Activity: Delete Duplicates

# Define the function
def delete_duplicates(input_str):

    # Create a blank string from scratch to save the output
    output = ""

    for char in input_str:
        if input_str.count(char) == 1:
            output += char

    return output

try:
    # See how many strings are there
    n = int(input("Type in the number of strings: "))

    # Take each string and process it
    for _ in range(n):
        input_str = input("Type in a word: ")
        output_str = delete_duplicates(input_str)
        print("The new word is: " + output_str)

except ValueError:
    print("As the first input, kindly stype in a valid integer.")