def square_of_odd_integers(input_list):
    squared_odds = [x ** 2 for x in input_list if x % 2 != 0]
    return squared_odds

print(square_of_odd_integers([2, 4, 3]))  
print(square_of_odd_integers([0, 0, 1, 1]))  
