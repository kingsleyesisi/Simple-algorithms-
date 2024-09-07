def linear_search(list,  target):
    """
    Returns the index position of the target if found, else returns None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    """
    Verifies if the index is within the bounds of the list
    """
    if index is not None:
        print("Rarget found at index: ", index)
    else:
        print("Traget not found in list ")

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

result = linear_search(numbers, 10)
verify(result)


