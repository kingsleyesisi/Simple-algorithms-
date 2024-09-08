import time
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
        print("Target found at index: ", index)
    else:
        print("Target not found in list ")

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


start_time = time.perf_counter() # Start time of the function
#  call the function
result = linear_search(numbers, 8)
verify(result)
#  end of the function
end_time = time.perf_counter()

runtime = (end_time - start_time) * 1000
print(f"Runtime: {runtime} miliseconds ")