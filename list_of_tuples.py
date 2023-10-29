def create_list_of_tuples(list1, list2):
    listOfTuples = list(zip(list1, list2))
    return listOfTuples

list1 = [1, 2, 3]
list2 = ["mark", "alice", "john"]
result = create_list_of_tuples(list1, list2)
print(result) 
