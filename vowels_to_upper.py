def vowelsToUpper(input_string):
    vowels = "aeiou"
    result = ""

    for char in input_string:
        if char in vowels:
            result += char.upper()
        else:
            result += char

    return result

print(vowelsToUpper(""))
print(vowelsToUpper("Hello, world!"))  
print(vowelsToUpper("hello hi bye"))  
