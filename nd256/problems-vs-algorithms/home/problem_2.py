def rotated_array_search(input_list: list[int], number: int) -> int:
    """
    Find the index by searching in a rotated sorted array

    Args:
    input_list (list[int]): Input array to search
    number (int): Target number to find

    Returns:
    int: Index of the target number or -1 if not found
    """
    low, high = 0, len(input_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if input_list[mid] == number:
            return mid
        
        # If the left side is sorted
        if input_list[low] <= input_list[mid]:
            if input_list[low] <= number < input_list[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # If the right side is sorted
        else:
            if input_list[mid] < number <= input_list[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

# Test function using provided test cases
def test_function(test_case: list[list[int], int]) -> None:
    input_list: list[int] = test_case[0]
    number: int = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

def linear_search(input_list: list[int], number: int) -> int:
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

if __name__ == '__main__':
    # Edge case: Empty input list
    test_function([[], 5])
    # Expected output: Pass

    # Edge case: Large input list
    test_function([[i for i in range(1000000, 2000000)] + [i for i in range(1000000)], 1500000])
    # Expected output: Pass

    # Edge case: Number not in the list
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 5])
    # Expected output: Pass

    # Normal case: Number at the beginning of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 4])
    # Expected output: Pass

    # Normal case: Number at the end of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 2])
    # Expected output: Pass

    # Normal case: Number in the middle of the list
    test_function([[4, 5, 6, 7, 0, 1, 2], 6])
    # Expected output: Pass