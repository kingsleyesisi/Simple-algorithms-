""" Binary Search algorithm """
import time
def binary_search(list, target):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        middle = (first + last) // 2
        
        if list[middle] == target:
            return middle
        elif list[middle] < target:
            first = middle + 1
        else:
            last = middle - 1
    return None

# Test the function
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
result = binary_search(numbers, 10)
verify(result)
#  end of the function
end_time = time.perf_counter()

runtime = (end_time - start_time) * 1000
print(f"Runtime: {runtime} miliseconds ")